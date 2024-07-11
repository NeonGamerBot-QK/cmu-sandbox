


# # background
app.background = 'black'

Circle(200, 200, 150, fill='white')

# ears
earFluff = Group(Polygon(261, 158, 305, 132, 280, 195, fill='tan',
        border=rgb(53, 31, 22), borderWidth=6),
Polygon(139, 158, 95, 132, 120, 195, fill='tan',
        border=rgb(53, 31, 22), borderWidth=6))
TopOfEars = Group(Polygon(227, 129, 305, 133, 264, 160, border=rgb(55, 30, 20), borderWidth=6),
Polygon(173, 129, 95, 133, 136, 160, border=rgb(55, 30, 20), borderWidth=6))
ears = Group()
ears.add(earFluff,
        TopOfEars
        )


# face and body
Oval(200, 276, 120, 130, border=rgb(55, 30, 20), borderWidth=6)
Circle(200, 200, 80, border=rgb(55, 30, 20), borderWidth=8)

# plate
# Oval(200, 323, 140, 45, fill='beige', border=rgb(55, 30, 20), borderWidth=3)
# Oval(200, 312, 200, 50, fill='white', border=rgb(55, 30, 20), borderWidth=4)
# Oval(200, 317, 150, 30, fill=None, border=rgb(170, 185, 55), borderWidth=3)





#mouth
 
m1 = Oval(200,245,50,30,fill = 'brown')
m2 = Oval(200,235,50,30,fill = 'black')











# hands
leftArm = Oval(165, 285, 30, 35, border=rgb(55, 30, 20), borderWidth=5, rotateAngle=-20, fill = 'brown')
rightArm = Oval(235, 285, 30, 35, border=rgb(55, 30, 20), borderWidth=5, rotateAngle=20,fill = 'brown')

# eyes and tears
Oval(163, 193, 75, 100, fill='beige', border=rgb(55, 30, 20), borderWidth=4,
     rotateAngle=5)
Oval(237, 193, 75, 100, fill='beige', border=rgb(55, 30, 20), borderWidth=4,
     rotateAngle=-5)
     
     

leftEye = Oval(165, 185, 45, 55, border=rgb(55, 30, 20), borderWidth=4)
rightEye = Oval(235, 185, 45, 55, border=rgb(55, 30, 20), borderWidth=4)



leftTear = Oval(150, 240, 25, 15, fill='lightCyan', border=rgb(85, 130, 125), visible=False)
rightTear = Oval(250, 240, 25, 15, fill='lightCyan', border=rgb(85, 130, 125), visible=False)

# message
message = Label('plz', 200, 90, fill='black', size=25, bold=True)

# food
food = Circle(200, 30, 10, fill='snow', border='brown')

def onMousePress(mouseX, mouseY):
    PLUHSound = Sound('https://c.lleon.dev/u/EREtmk.mp3')
    m2.centerY -= 10
    leftEye.fill = rgb(70,40,70)
    rightEye.fill = rgb(70,40,70)
    message.value = "PLUH🗣"
    PLUHSound.play()
    pass


def onMouseDrag(mouseX,mouseY):
    food.centerX = mouseX
    food.centerY = mouseY
    leftEye.centerX = 155 + (mouseX / 20)
    leftEye.centerY = 180 + (mouseY / 20)
    rightEye.centerX = 225 + (mouseX / 20)
    rightEye.centerY = 180 + (mouseY / 20)
    
    ## Move arm 
    # leftArm.rotateAngle = 165 + (mouseX / 20)
    # leftArm.bottom = 285 + (mouseY / 20)
    # rightArm.centerX = 225 + (mouseX / 20)
    # rightArm.centerY = 180 + (mouseY / 20)
def onMouseRelease(x,y):
    leftEye.fill = 'black'
    rightEye.fill = 'black'
    m2.centerY += 10
    message.value = 'plz'
def onMouseMove(mouseX, mouseY):
    leftEye.centerX = 155 + (mouseX / 20)
    leftEye.centerY = 180 + (mouseY / 20)
    rightEye.centerX = 225 + (mouseX / 20)
    rightEye.centerY = 180 + (mouseY / 20)
    food.centerX = mouseX
    food.centerY = mouseY
   
   