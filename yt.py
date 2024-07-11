app.songs = []
try:
    app.url = app.getTextInput('YT URL')
except:
    print('No URL')
    app.stop()
app.playing = True

sound = Sound('https://port8000.saahild.com/download?url='+app.url)
sound.play()

def createThumbnail():
    thumbnail = Image('https://port8000.saahild.com/thumbnail?url='+app.url, 200, 200)
    thumbnail.height = 300
    thumbnail.width = 300
    thumbnail.opacity = 90
    thumbnail.centerX = 200
    thumbnail.centerY = 200
    return thumbnail
def pausePlay():
    if app.playing:
        sound.pause()
        app.playing = False
    else:
        sound.play()
        app.playing = True
def onStep():
    if app.playing:
        thumbnail.opacity = 90
    else:
        thumbnail.opacity = 75
def onMousePress(x,y): 
    if thumbnail.hits(x,y):
        pausePlay()
def onKeyPress(k):
    if k == 'space':
         pausePlay()