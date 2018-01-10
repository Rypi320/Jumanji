from processing import *

width = 550
height = 509

game_start = False
brickList = []
score = 0
ball = {
    'x': 280,
    'y': 380,
    'r': 10,
    'vel_x': 5,
    'vel_y': 4,
}    
paddle = {
    'x': 250,
    'y': height - 20,
    'w': 100,
    'h': 15,
    'vel': 7,
    'move': 0
}

def setup():
    size(width, height)
    for row in range(4):
        for column in range(6):
            brick = {
                'x': 90 * column + 10,
                'y': 60 * row + 60,
                'w': 75,
                'h': 20
            }
            brickList.append(brick)
def draw():
    background(0, 0, 0)
    
    for brick in brickList:
        fill(23, 0, 70)
        stroke(25, 70, 23)
        rect(brick['x'], brick['y'], brick['w'], brick['h'])
    if len(brickList) == 0:
        fill(0, 255, 0)
        textSize(40)
        text("You Win...", 180, 227)
        exitp()
    fill(255, 255, 25)
    stroke(0, 102, 255)
    ellipse(ball['x'], ball['y'], 2*ball['r'], 2*ball['r'])
    
    fill(25, 204, 0)
    stroke(255, 23, 0)
    rect(paddle['x'], paddle['y'], paddle['w'], paddle['h'])
    textSize(14)
    text("Score : " + str (score), 10, 20, 50)
    moveBall()
    movePaddle()
    
def moveBall():
    if game_start:
        ball['x'] = ball['x'] + ball['vel_x']
        ball['y'] = ball['y'] + ball['vel_y']
    else:
        ball['x'] = paddle['x'] + paddle ['w']/2
        ball['y'] = paddle['y'] - ball['r']
    
    if (ball['y'] - ball['r'] <= 0):
        ball['vel_y'] = -ball['vel_y']
    
    elif ball['y'] + ball['r'] >= height: 
        fill(255, 0, 0)
        textSize(40)
        text("Game Over!", 180, 227)
        exitp()
    if (ball['x'] + ball['r'] >= width or
        ball['x'] - ball['r'] <= 0):
        ball['vel_x'] = -ball['vel_x']
        
    checkCollisions()
    
def checkCollisions():
    global score
    if (ball['x'] >= paddle['x'] and
        ball['x'] <= paddle['x'] + paddle['w'] and
        ball['y'] + ball['r'] >= paddle['y']):
        ball['vel_y'] = -ball['vel_y']
        ball['y'] = paddle['y'] - ball['r']
        
    collision_index = None
    for i in range(len(brickList)):
        brick = brickList[i]
        brick_top = brick['y']
        brick_bottom = brick['y'] + brick['h']
        brick_left = brick['x']
        brick_right = brick['x'] + brick['w']
        
        if (ball['x'] >= brick_left and 
            ball ['x'] <= brick_right):
            if ((ball['vel_y'] < 0 and
                 ball['y'] - ball['r'] <= brick_bottom and
                 ball ['y'] > brick_bottom) or
                (ball['vel_y'] > 0 and
                 ball['y'] + ball['r'] >= brick_top and
                 ball['y'] < brick_top)):
                collision_index = i
                ball['vel_y'] = -ball['vel_y']
                break
                
    if collision_index is not None:
        del brickList[collision_index]
        score = score + 1

def keyPressed():
    global game_start
    if keyboard.keyCode == LEFT:
        paddle['move'] = -1
    elif keyboard.keyCode == RIGHT:
        paddle['move'] = 1
    if keyboard.keyCode == 32:
        game_start = True 
        
def keyReleased():
    if keyboard.keyCode in [LEFT, RIGHT]:
        paddle['move'] = 0
    
    
def movePaddle():
    paddle['x'] += paddle['vel'] * paddle['move']
    
    if paddle['x'] <= 0:
        paddle['x'] = 0
        
    if paddle['x'] + paddle['w'] >= width:
        paddle['x'] = width - paddle['w']
                            
run()

