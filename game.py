import pygame # is this needed?

# Keep track of the current state of the game, and other data
class Game():
    def __init__(self):
        self.currentState = 'running'
        
        self.transitions = {
                'title': {'spaceInput': 'running'},
                'running': {'pInput': 'paused', 'playerDeath': 'gameOver', 'success': 'gameWin'},
                'paused': {'pInput': 'running'}
        }

    def Transition(self, currentState, event):
            if currentState in self.transitions and event in self.transitions[currentState]:
                return self.transitions[currentState][event]
            else:
                return currentState

    def Update(self, event):
        self.currentState = self.Transition(self.currentState, event)

    def GetState(self):
        return self.currentState

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



