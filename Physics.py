
# https://academy.cs.cmu.edu/sharing/antiqueWhiteHorse6130
# This is some sort of physics simulation I made. The ball can move, gain velocity, and move based upon the momentum of the object. Friction then slows it down.

# dynamic velocity demo

dbg = Label("accelX: 0, accelY: 0, speed: 0", 200, 10)
goFast = Circle(375,375,15, fill='green')
goFast.visible=False
goSlow = Circle(340,375,15, fill='red')
goSlow.visible=False
slippery = Circle(305,375,15, fill='lightSkyBlue')
slippery.visible=False
object = Circle(200, 200, 10, fill='white', border='black')
object.velocityX = 0
object.velocityY = 0
object.accelerationRate = 0.25
object.maxSpeed = 5
object.frictionRate = .1
app.goFast = False
app.goSlow = False
app.slippery = False
# def onStep():
#     print('on step')
   
def onKeyPress(key):
    if key == 'q':
        goFast.visible = True
        # app.goFast = True
    if key == 'e':
        goSlow.visible = True
    
    if key == 'f':
        slippery.visible = True
    if key == 't':
        #  tp to center
        object.centerX = 200
        object.centerY = 200
def onKeyRelease(key):
    if key == 'q':
        goFast.visible = False
        app.goFast = False
        object.accelerationRate -= .15
        object.maxSpeed -= 2
    if key == 'f':
        slippery.visible = False
        app.slippery = False
        object.frictionRate += 0.05
    if key == 'e':
        goSlow.visible = False
        app.goSlow = False
        object.accelerationRate += .05
        object.maxSpeed *= 2
         
def onKeyHold(keys):
    if 'w' in keys:
        if abs(object.velocityX) + abs(object.velocityY) <= object.maxSpeed:
            object.velocityY -= object.accelerationRate
    if 's' in keys:
        if abs(object.velocityX) + abs(object.velocityY) <= object.maxSpeed:
            object.velocityY += object.accelerationRate
    if 'a' in keys:
        if abs(object.velocityX) + abs(object.velocityY) <= object.maxSpeed:
            object.velocityX -= object.accelerationRate
    if 'd' in keys:
        if abs(object.velocityX) + abs(object.velocityY) <= object.maxSpeed:
            object.velocityX += object.accelerationRate

def onStep():
    if app.goFast == False and goFast.visible:
        # print('going fast')
        # double speed
        object.accelerationRate += .15
        object.maxSpeed += 2
        app.goFast = True
    if app.goSlow == False and goSlow.visible:
        print('going slow')
        # double speed
        object.accelerationRate -= .05
        object.maxSpeed = object.maxSpeed/2
        app.goSlow = True
    if app.slippery == False and slippery.visible:
        # print('going slow')
        # double speed
        object.frictionRate -= 0.05
        app.slippery = True
        
        
    dbg.value = f"accelX: {pythonRound(object.velocityX)}, accelY: {pythonRound(object.velocityY)}, speed: {pythonRound(object.velocityX + object.velocityY)}"
    object.centerX += object.velocityX
    object.centerY += object.velocityY
    
    if object.velocityX < 0 and object.velocityX != 0:
        object.velocityX += object.frictionRate
    elif object.velocityX > 0 and object.velocityX != 0:
        object.velocityX -= object.frictionRate

    if object.velocityY < 0 and object.velocityY != 0:
        object.velocityY += object.frictionRate
    elif object.velocityY > 0 and object.velocityY != 0:
        object.velocityY -= object.frictionRate