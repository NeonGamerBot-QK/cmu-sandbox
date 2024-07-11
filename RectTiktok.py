# also based of another tiktok
# fun fact if its at speed 300 its very cool
app.speed = 1
# app.speed = 300
app.rwidth = 220
app.rheight = 220
app.Xdir = 1
app.Ydir = 1
app.background = 'black'
# bg = Rect(0,0,400,400,fill=None, border='lime', borderWidth=30)
mc = Rect(140,140,app.rwidth, app.rheight, fill='lime')
def UpdateMC():
    mc.centerX += (app.Xdir * app.speed) #+ (app.drift * app.Xdir)
    mc.centerY -= (app.Ydir * app.speed) #+ (app.drift * app.Ydir)
    
def onHitCorner(corner):
    if corner == 'right':
        app.Xdir = -1
        # lines[2].add(Line(400,mc.centerY,450, 450, visible=False))   
    if corner == 'top':
        app.Ydir = -1
        # lines[0].add(Line(mc.centerX,0,-50, -50,visible=False))
    if corner == 'bottom':
        app.Ydir = 1
        # lines[1].add(Line(mc.centerX,400,450, 450,visible=False))
    if corner == 'left':
        app.Xdir = 1
        # lines[3].add(Line(0,mc.centerY,-50, -50, visible=False))   
    if app.speed < 10:
         app.speed += .5
    else:
         app.speed += .2
         
        #  its supposed to be 1 but i want to see the rect
    if app.rwidth > 5:
        app.rwidth -= 1
    if app.rheight > 5:
        app.rheight -= 1
    
    # if app.radius > 1:
        # app.radius -= 1
    # else:
        # app.paused = True
        
    pass
def onStep():
    UpdateMC()
    mc.width = app.rwidth
    mc.height = app.rheight
    if mc.right > 400:
        onHitCorner('right')
    if mc.top <= 0:
        onHitCorner('top')
    if mc.bottom >= 400:
        onHitCorner('bottom')
    if mc.left <= 0:
        onHitCorner('left')
    # mc.centerX += app.speed
    # mc.centerY += app.speed
    