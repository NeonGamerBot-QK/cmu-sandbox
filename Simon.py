
import random
app.background = 'black'
app.stepsPerSecond = 3

answerlist =[]
base = Group(
    Arc(195, 195, 425, 425, 270, 90, fill='red', opacity=50),
    Arc(205, 195, 425, 425, 0, 90, fill='blue', opacity=50),
    Arc(195, 205, 425, 425, 180, 90, fill='limeGreen', opacity=50),
    Arc(205, 205, 425, 425, 90, 90, fill='yellow', opacity=50)
    )

startScreen = Group(
    Rect(0, 0, 400, 400, fill='white'),
    Circle(200, 200, 85),
    Label('SIMON', 200, 200, fill='white', size=35, font='monospace', bold=True),
    Label('Press space to play!', 200, 50, size=20, font='monospace', bold=True),
    )

def onKeyPress(key):
    if key == "space":
        startScreen.visible=False

def createSimonCommand():
    colorList = [ 'red', 'blue', 'limeGreen', 'yellow' ]
    if startScreen.visible==False:
        for _ in range(3):
            command = random.choice(colorList)
            answerlist.append(command)
            for color in colorList:
                if color == command:
                 
                 
                    pass
       
       

       
           
           
                pass
def onStep():
    createSimonCommand()
    for i in base:
        if i.opacity == 100:
            sleep(0.1)
            i.opacity==50
   
   
def onMousePress(x, y):
    for i in base:
        if i.hits(x, y):
            i.opacity=100
            sleep(0.5)
            i.opacity =50
       
def onMouseRelease(x, y):
    for i in base:
        if i.hits(x, y):
            i.opacity=50