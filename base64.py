import json
import base64
app.lastRect = None
app.rotateAngle = 0
exampleString = 'Hey this is now going into base64'
exampleEncodedJsonNoBase64 = '{"name":"test"}'
exampleSchema = {
    "name":"test",
    "sound": "https://cdn.saahild.com/u/EREtmk.mp3",
    "isRunning": False,
    "isLoaded": False,
    "SoundEl": None,
    "ButtonEl": None
}
encodedStr= 'eyJuYW1lIjogInRlc3QiLCAic291bmQiOiAiaHR0cHM6Ly9jZG4uc2FhaGlsZC5jb20vdS9FUkV0bWsubXAzIiwgImlzUnVubmluZyI6IGZhbHNlLCAiaXNMb2FkZWQiOiBmYWxzZSwgIlNvdW5kRWwiOiBudWxsLCAiQnV0dG9uRWwiOiBudWxsfQ=='

def onStep():
    r = Rect(200,200,50,50,fill='red', rotateAngle=app.rotateAngle)
    app.rotateAngle += 1
    if app.lastRect != None:
        app.lastRect.visible = False
    app.lastRect = r
    
def encodeIt():
    jsonStr = json.dumps(exampleSchema)
    binaryStr = base64.encodebytes(jsonStr.encode())
    return binaryStr
    
    
def decodeStr():
    d = base64.b64decode(encodedStr.encode())
    # print(f'{d.decode()}')
    # print(d.decode())
    j = json.loads(d.decode())
    return j