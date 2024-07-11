import random
app.background = gradient('red', 'black', 'blue', 'yellow', 'green', 'green', 'black', 'black')
colors = ['red', 'green', 'blue']
platform = Rect(175,340,60,40, fill=gradient('snow', 'white'),border='gray')
def moveLeft():
    if platform.left > 0:
        platform.centerX -= 5

def moveRight():
    if platform.right < 400:
        platform.centerX += 5
    
def onKeyPress(k):
    if k == 'left':
        moveLeft()
    elif k == 'right':
        moveRight()
        
def onKeyHold(keys):
    for k in keys:
        if k == 'left':
            moveLeft()
        elif k == 'right':
            moveRight()
            
            
            
blocks = Group()
def drawBlock(x,y,color):
    block = Group(
        Rect(200,200,80,40,fill=color)
        )
    block.centerX = x
    block.centerY = y
for i in range(3):
        color = colors[i]
        for j in range(5):
            drawBlock(j * 20,i * 20, color)
        pass