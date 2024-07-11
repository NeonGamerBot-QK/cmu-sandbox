
# lists that hold the names and scores
leaderNames= []
leaderScores= []

#initial speed of the game
app.stepsPerSecond = 30

#leaderboard code
leaderBoard=Group(Label("", 200, 100, size = 20 ), Label("", 200, 150, size = 20), Label("", 200, 200, size = 20), Label("", 200, 250, size = 20))
leaderBoard.visible = False
restart = Group(Rect(250, 300, 100, 50, fill = 'blue'), Label("Restart", 300, 325, size = 20))
restart.visible = False

# paddle and ball
paddle = Rect(150,350,100,10)
ball = Circle(200, 200, 10)
ball.dx = 10
ball.dy = 8

#keeps track of score
app.count = 0

#start screen
start = Group(Rect(0,0,400,400), Label("Click to Start",200,200, size = 20, fill = 'white'))
app.play = False

def onStep():
    if app.play:
        ball.centerX += ball.dx
        ball.centerY += ball.dy
         # if it is time to play then move the ball
        # if the ball hits a wall
        #   - speed up app.stepsPerSecond
        #   - change balls direction
        if ball.right >= 400:
            ball.dx = -ball.dx
            app.stepsPerSecond +=1
        if ball.bottom >= 400:
            ball.dy = -ball.dy
            app.stepsPerSecond +=1
        if ball.left <= 0:
            ball.dx = -ball.dx
            app.stepsPerSecond +=1
        if ball.top <= 0:
            ball.dy = -ball.dy
            app.stepsPerSecond +=1
           
        # if the ball hits the paddle then your score increases
        if ball.hitsShape(paddle):
            ball.dy = -ball.dy
            app.count += 1
    # pass
       
   
   
  
   
    # if the bottom reaches the bottom of the screen game over
        if ball.bottom >= 400:
            app.play = False
            
    # user types their name and then check the leaderboard
        if app.play == False:
            displayLeaderBoard(True)
    pass

def check(player):
    # create an index
   
    # loop over the scores to see if you made it on the board
    # if you do . . . insert the score and name in the right spot
    # pop last item off the list
    # display the leaderboard
   
    pass
   
def displayLeaderBoard(appendName):
    if appendName:
        leaderNames.append(app.getTextInput("Name:"))
        leaderScores.append(app.count)
    index = 0
    for label in leaderBoard:
      try:
            label.value = leaderNames[index] + " . . . " + str(leaderScores[index])
            index += 1
      except:
          print('n u. uh')
    leaderBoard.visible = True
    restart.visible = True
   
def onMouseMove(x,y):
    if app.play:
        paddle.centerX = x
    # moves the paddle
   
    pass
paddle.dy = 5
def onKeyPress(_e):
    if paddle.centerY <= 0:
        paddle.dy = -paddle.dy
    elif paddle.centerY >= 400:
        paddle.dy = -paddle.dy
        
    paddle.centerY += paddle.dy
    
def onMousePress(x,y):
    #if the start screen is visible make it invisible and play becomes true
    # if app.play == False:
    #     start.visible = False
    # if start.visible == False:
    #     app.play = True
    if start.hits(x,y):
        if start.visible:
            start.visible = False
            app.play = True
        
   
    #if the user clicks on the restart button then
    # 1 - leaderboard is no longer visible
    # 2 - restart button is no longer visible
    # 3 - play becomes true
    # 4 - ball is reset to center
    # 5 - app.stepsPerSecond is set back to 30
    # 6 - coutner is reset
    if restart.hits(x,y):
        
        app.count = 0
        ball.centerX = 200
        ball.centerY = 200   
        app.stepsPerSecond = 30
        restart.visible = False
        leaderBoard.visible = False
        app.play = True
    pass