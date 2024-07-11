import random
# from datetime import datetime
# there was a rubric
# i forgot it
# it smthing ab loops
# so we do kitty
app.amount = 10
app.size = 100
app.minSize = 99
app.sillyModeEnabled = False
# a step every 500ms 
# important later
# default is 30 which is (3.33 (inf))
# app.stepsPerSecond = 10
# date time lib dont work :(
app.time = 0
app.background = gradient(rgb(7,7,7),rgb(55,55,55) )
sillykittyUrls = [
  "https://cdn.saahild.com/u/eba88f29-c210-45d4-94b6-c60b3da77bf0.jpg",
  "https://cdn.saahild.com/u/4c004f2a-2ce5-4586-8ecc-ba0833722e3a.jpg",
  "https://cdn.saahild.com/u/2af8df1e-bcc0-4e78-9265-e7d26bcb8786.jpg",
  "https://cdn.saahild.com/u/ca52a681-8dcc-415c-9f05-82429a83bf3d.jpg",
  "https://cdn.saahild.com/u/cdac4cb2-5d5b-40e9-aa7c-6ba7577d89c0.jpg",
  "https://cdn.saahild.com/u/%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B",
  "https://cdn.saahild.com/u/selfish%20tattered%20northernseahorse.png",
  "https://cdn.saahild.com/u/myNK92.jpg",
  "https://cdn.saahild.com/u/AtBMEi.jpg",
  "https://cdn.saahild.com/u/myNK92.jpg",
  "https://cdn.saahild.com/u/AtBMEi.jpg",
  "https://c.lleon.dev/u/44KYJG.jpg",
  "https://cdn.saahild.com/u/ofgs1Q.jpg",
  "https://c.lleon.dev/u/m4iy8Q.jpg",
  "https://c.lleon.dev/u/V7c9AJ.jpg",
  "https://c.lleon.dev/u/0r4hNL.jpg",
  "https://cdn.saahild.com/u/GnPoAQ.jpg",
  "https://c.lleon.dev/u/kSPQ2p.jpg",
  "https://cdn.saahild.com/u/tYeDXQ.jpg",
  "https://cdn.saahild.com/u/P06Sjk.jpg",
  "https://c.lleon.dev/u/hkMe1L.jpg",
  "https://cdn.saahild.com/u/6T4DNg.jpg",
  "https://c.lleon.dev/u/ryH84r.jpg",
  "https://c.lleon.dev/u/KzZazo.jpg",
  "https://cdn.saahild.com/u/YFU1qm.jpg",
  "https://c.lleon.dev/u/yq8z9W.jpg",
  "https://c.lleon.dev/u/1BrIuM.jpg",
  "https://cdn.saahild.com/u/fcoCBW.jpg",
  "https://c.lleon.dev/u/gFcBoa.jpg",
  "https://c.lleon.dev/u/JjwkMT.jpg"
]

nyeheheList = [
    'http://cdn.saahild.com/u/8QOKWz.mp3',
    'https://cdn.saahild.com/u/EjG6nc.mp3',
    'https://cdn.saahild.com/u/Xi1yMR.mp3'
    ]
app.nyeheheIndex = 0
musicSong = Sound('https://cdn.saahild.com/u/vaU7gk.mp3')
musicSong.play(loop=True)
musicSong.playing = True
# def waitSecs(a,f):
#     timeBeforeLoop = app.time
#     while app.time >= timeBeforeLoop + a:
#         print('loop', app.time, timeBeforeLoop + a )
#         f(app.time)
kittys = Group()
gui = Group()
timeText = Label('0s',30,10, fill='white')
gui.add(timeText)
def playNyehe():
    # musicSong.pause()
    Sound(nyeheheList[app.nyeheheIndex]).play()
    # musicSong.play(loop=True)
def drawImage(url,x,y,h,w):
    i = Image(url,x,y)
    # i.centerX = x
    # i.centerY = y
    i.height = h
    i.width = w
    return i
# centerCircle = Circle(200,200,30,fill=gradient('red', 'black'))
# gui.add(centerCircle)
def drawSilyKitty(x,y):
#   g = Group()
   i = drawImage(choice(sillykittyUrls),x,y, random.randint(app.minSize,app.size), random.randint(app.minSize,app.size))
   i.doTheRotate = False
   i.manRotate = False
   i.rotatedBack = True
#   l = Line(200,200,x,y,fill=gradient('snow', 'white'))
#   l.toBack()
#   lines.add(l)
#   g.add(i)
#   g.add(l)
   kittys.add(i)
   return i
def drawSillyKittys(amount):
    checkArr = []
    for i in range(amount):
        if i % 2 == 0:
            k = drawSilyKitty(random.randint(0,300) - i, random.randint(0,300) - i)
            checkArr.append(k)
        else:
             drawSilyKitty(random.randint(0,300) + i,  random.randint(0,300) + i)
    
    if app.sillyModeEnabled:
             for k in checkArr:
                for kit in kittys:
                    if k.hitsShape(kit):
                        k.visible = False
             for k in kittys:
                for kit in kittys:
                    hitShape = k.hitsShape(kittys)
                    if hitShape:
                        if kit.centerX != k.centerX:
                            # print(k, 'hits', kit)
                            # print(app.amount)
                            if k in checkArr:
                                k.visible = False
                            else:
                                kit.visible = False
                checkArr.append(k)
    app.amount = len(list(set(checkArr)))
# def onStep():
#         if app.amount != 0:
#             drawSillyKittys(app.amount)
def onStep():
    # print(chr(27)+ '[2J')
    # print(f'Steps per second: {app.stepsPerSecond}')
    # print(f'The time is {app.time // 1}s')
    timeText.value = f'{app.time // 1}s'
    # if app.stepsPerSecond == 2:
    #     app.time += .5
    # elif app.stepsPerSecond == 10:
    #     app.time += .1
    app.time += app.stepsPerSecond / 1000
    # print(f'its been {app.time}s')
    # if app.amount != 0:
            # drawSillyKittys(app.amount)
    if len(kittys.children) > 1:
        # kittys.remove(kittys.children[0])
        if kittys.children[0].manRotate == False:
            if kittys.children[0].doTheRotate == False:
                kittys.children[0].rotateAngle = 0
            kittys.children[0].doTheRotate = True
    else:
        # lines.clear()
        drawSillyKittys(10)
    for k in kittys:
        # k = kk.children[0]
        if k.rotatedBack == False:
            # print('not rot back', k.rotateAngle)
            k.rotateAngle -= 1
            if k.rotateAngle <= 1:
                k.rotatedBack = True
            
        if k.doTheRotate:
           if k.rotatedBack:
                k.rotateAngle += 15
                # print('BYE BYE', k.rotateAngle)
                if k.opacity > 10:
                    k.opacity -= 15
                elif k.opacity > 1:
                    k.opacity -= 1
                if k.rotateAngle > 300:
                    kittys.remove(k)
        # k.height = 
    for g in gui:
        g.toFront()

def onKeyPress(key):
    if key == 'up':
        if app.size < 300:
            app.size += 1
    elif key == 'down':
        if app.minSize > 2:
            app.minSize -= 1
    elif key == 'left':
       if app.stepsPerSecond > 10:
           app.stepsPerSecond -= 1
    elif key == 'right':
        app.stepsPerSecond += 1
    elif key == 'm':
        if musicSong.playing:
            musicSong.pause()
            musicSong.playing = False
        else: 
            musicSong.play(loop=True)
            musicSong.playing = True
    elif key == 'n':
        if app.nyeheheIndex < len(nyeheheList) -1:
            app.nyeheheIndex += 1
    elif key == 's':
        if app.sillyModeEnabled:
            app.sillyModeEnabled = False
        else:
            app.sillyModeEnabled = True

def onMousePress(x,y):
    played = False
    for kitty in kittys:
        # kitty = kittyy.children[0]
        if kitty.hits(x,y):
            if played == False:
                playNyehe()
                kitty.borderWidth = 10
                kitty.border = 'white'
                kitty.rotateAngle = 0
                kitty.opacity = 100
                played = True
def onKeyHold(keys):
    for key in keys:
        if key == 'r':
            for kitty in kittys:
                kitty.manRotate = True
                kitty.rotatedBack = False
                # kitty.doTheRotate = False
                kitty.rotateAngle += 5
def onKeyRelease(key):
    if key == 'r':
        for kitty in kittys:
            kitty.manRotate = False
drawSillyKittys(20)




