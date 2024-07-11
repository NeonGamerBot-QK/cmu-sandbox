notes =  [ Note('C', 2, 1/4), Note('G', 2, 1/4), Note('E', 2, 1/4) ]
sequencer1 = Sequencer(tuple(notes))
def playChopsticks():
    sequencer1.play()
    
def onSignal(noteSignals):
    print(noteSignals)
    print()
