# ANOTHER TIKTOK VIDEO
import random
app.background = 'black'
app.speed = 3
app.Xdir = 1
app.Ydir = 1
app.Xdir1 = 1
app.Ydir1 = 1
app.drift = 0
app.di = 0
app.ddi = 1
# app.stepsPerSecond = 3
app.setMaxShapeCount(9999)
app.mc =  Rect(100,200,20,20,fill='blue',border='grey',borderWidth=1)
app.mc1 =  Rect(300,200,20,20,fill='orange',border='grey',borderWidth=1)
def onHitCorner(corner, mc):
    isTheNewRect = mc.fill == 'orange'
    # print('corner', corner, mc, isTheNewRect)
    if corner == 'right':
        if isTheNewRect:
            app.Xdir1 = -1
        else:
            app.Xdir = 1
        # lines[2].add(Line(400,mc.centerY,450, 450, visible=False))   
    if corner == 'top':
        if isTheNewRect:
            app.Ydir1 = -1
        else:
            app.Ydir = 1
        # lines[0].add(Line(mc.centerX,0,-50, -50,visible=False))
    if corner == 'bottom':
        # print('b')
        if isTheNewRect:
            app.Ydir1 = 1
        else:
            # print('updated')
            app.Ydir = -1
        # lines[1].add(Line(mc.centerX,400,450, 450,visible=False))
    if corner == 'left':
        if isTheNewRect:
            app.Xdir1 = 1
        else:
            # print('updated left rect')
            app.Xdir = -1
        # lines[3].add(Line(0,mc.centerY,-50, -50, visible=False))   
    # app.speed += 1e
    # else:
        # app.paused = True
    updateDrift(isTheNewRect)
    # app.
    pass
def updateDrift(e):
    app.drift = random.randint(0,2)
    mc = app.mc
    mc1 = app.mc1
   
    if e:
        mc1.centerX += app.drift * app.Xdir1
        mc1.centerY += app.drift * app.Ydir1
    else:
        mc.centerX += app.drift * app.Xdir
        mc.centerY += app.drift * app.Ydir
def UpdateMC():
    oldPosMC = [app.mc.centerX,app.mc.centerY]
    oldPosMC1 = [app.mc1.centerX,app.mc1.centerY]
    app.mc = Rect(-50,-50,20,20,fill='blue',border='grey',borderWidth=1)
    app.mc1 = Rect(-50,-50,20,20,fill='orange',border='grey',borderWidth=1)
    app.mc.centerX = oldPosMC[0] + (-app.Xdir * app.speed) #+ (app.drift * app.Xdir)
    app.mc.centerY = oldPosMC[1] + (app.Ydir * app.speed) #+ (app.drift * app.Ydir)
    app.mc1.centerX = oldPosMC1[0] + (app.Xdir1 * app.speed) #+ (app.drift * app.Xdir)
    app.mc1.centerY = oldPosMC1[1] + (-app.Ydir1 * app.speed) #+ (app.drift * app.Ydir)
def onStep():
    if app.mc.hitsShape(app.mc1):
        print('hits at', app.mc.centerX,app.mc.centerY)
        app.paused = True
    # mc = Rect(-50,-50,1,1,fill)
    # print(app.mc.centerX, app.mc.centerY,app.mc1.centerX, app.mc1.centerY, app.di)
    if app.di > 50:
        app.group.remove(app.group.children[0])
        app.di = 0
        
        if app.ddi < 3:
            app.ddi += 1
        else:
            print('starting 1945')
            while app.group.hitTest(app.mc.centerX,app.mc1.centerY) != None:
                print('1945 moment')
                app.group.remove(app.group.hitTest(app.mc.centerX,app.mc1.centerY))
    
    UpdateMC()
    app.di += 1 * app.ddi 
    
    # mc = app.mc
    # mc1 = app.mc1
    for mc in [app.mc, app.mc1]:
        if mc.right > 400:
            onHitCorner('right', mc)
        if mc.top <= 0:
            onHitCorner('top', mc)
        if mc.bottom >= 400:
            onHitCorner('bottom', mc)
        if mc.left <= 0:
            onHitCorner('left', mc)
    