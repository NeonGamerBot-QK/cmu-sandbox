# a timer

timerText = Label("00:00:00", 200,200,size=60)
timerAmount = app.getTextInput('How long in (HH:MM:SS) format')
[hours,minutes,seconds] = timerAmount.split(":")
app.hours = int(hours)
app.minutes = int(minutes)
app.seconds = int(seconds)
app.stepsPerSecond = 1
def onStep():
    # print(1)
    if app.seconds > 0:
       app.seconds -= 1
    else:
        if app.minutes > 0:
            app.minutes -= 1 
            app.seconds = 59
        else: 
            if app.hours > 0:
                app.hours -= 1 
                app.minutes = 59
            else:
                print("Time Done !!!")
                app.stop()
                
    timerText.value = renderValue()
            
        
    
    pass

def renderValue():
    # h = len(str(app.hours))
    h= app.hours
    s = app.seconds
    m = app.minutes
    if len(str(h)) == 1:
        h = f"0{h}"
    if len(str(m)) == 1:
        m = f"0{m}"
    if len(str(s)) == 1:
        s = f"0{s}"
    return f"{h}:{m}:{s}"