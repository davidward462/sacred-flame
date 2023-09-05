import pygame # is this needed?

# Keep track of the current state of the game, and other data
class Game():
    def __init__(self):
        self.currentState = 'title'
        
        transitions = {
                'title': {'spaceInput': 'running'},
                'running': {'pInput': 'paused', 'playerDeath': 'gameOver', 'success': 'gameWin'},
                'paused': {'pInput': 'running'}
        }

    def Transition(self, currentState, event):
            if currentState in transitions and event in transitions[currentState]:
                return transitions[currentState, event]
            else:
                return currentState

    def Update(self, event):
        self.currentState = Transition(self.currentState, event)

    # check state
    def IsPaused(self):
        if self.currentState == 'paused':
            return True
        else:
            return False

    # check state
    def IsRunning(self):
        if self.currentState == 'running':
            return True
        else:
            return False

    # check state
    def IsTitle(self):
        if self.currentState == 'title':
            return True
        else:
            return False



