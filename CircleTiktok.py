import random
# made from a tiktok
app.background = 'yellow'
app.radius = 120
app.speed =1
app.Xdir = 1
app.Ydir = 1
app.drift = 0
# change steps per sec here
# app.stepsPerSecond = 50
# top bottom right left
lines = [Group(Line(200,0,-50, -50)),Group(Line(200,400,-50, -50)),Group(Line(400,200,-50, -50)),Group(Line(0,200,-50, -50))]
mc = Circle(200,200,app.radius,fill='red')
# def applyDrift():
def updateLines():
    updateMethod = [[mc.centerX,mc.top], [mc.centerX,mc.bottom],[mc.right,mc.centerY], [mc.left,mc.centerY]]
    i = 0
    for j in lines:
        # print(j)
        for line in j:
            # line.toBack()
            line.fill = 'red'
            line.x2 = updateMethod[i][0]
            line.y2 =  updateMethod[i][1]
            line.visible = True
        i += 1
def onHitCorner(corner):
    if corner == 'right':
        app.Xdir = -1
        lines[2].add(Line(400,mc.centerY,450, 450, visible=False))   
    if corner == 'top':
        app.Ydir = -1
        lines[0].add(Line(mc.centerX,0,-50, -50,visible=False))
    if corner == 'bottom':
        app.Ydir = 1
        lines[1].add(Line(mc.centerX,400,450, 450,visible=False))
    if corner == 'left':
        app.Xdir = 1
        lines[3].add(Line(0,mc.centerY,-50, -50, visible=False))   
    app.speed += 1
    if app.radius > 1:
        app.radius -= 1
    # else:
        # app.paused = True
        
    pass
def updateDrift():
    app.drift = random.randint(0,2)
    mc.centerX += app.drift * app.Xdir
    mc.centerY += app.drift * app.Ydir
def UpdateMC():
    mc.centerX += (app.Xdir * app.speed) #+ (app.drift * app.Xdir)
    mc.centerY -= (app.Ydir * app.speed) #+ (app.drift * app.Ydir)
def onStep():
    mc.radius = app.radius
    updateDrift()
    UpdateMC()
    updateLines()
    if mc.right > 400:
        onHitCorner('right')
    if mc.top <= 0:
        onHitCorner('top')
    if mc.bottom >= 400:
        onHitCorner('bottom')
    if mc.left <= 0:
        onHitCorner('left')
