# gravity
# equations for velocity:
# v = u + a*t
# d = s*t
app.stepsPerSecond = 20
c = Rect(200,40,20,20)
def gravity(char):
    # yes i am chance
    if char.centerY < 380:
        char.centerY += 3.2
    elif char.centerY >= 380:
        char.centerY = 380
def jump(c):
    if c.centerY == 380:
        c.centerY -= 20
def onKeyPress(e):
    if e == 'space':
        jump(c)
    if e == 'right':
        c.centerX += 5
    
def onStep():
    gravity(c)
    # gravity(c)

