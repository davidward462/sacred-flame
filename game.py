import pygame # is this needed?

# Keep track of the current state of the game, and other data
class Game():
    def __init__(self):
        # TODO: start on 'title' state
        self.currentState = 'title'
        
        self.transitions = {
                'title': {'space': 'running'},
                'running': {'esc': 'paused', 'death': 'playerDead', 'flameOut': 'darkness', 'success': 'gameWin'},
                'paused': {'esc': 'running'},
                'playerDead': {'r': 'title'},
                'darkness': {'r': 'title'}, # flame has gone out
                'gameWin': {'r': 'title'},
                }

    def Transition(self, currentState, event):
            # If there is a transition for the current state, and the event exists for the current state.
            if currentState in self.transitions and event in self.transitions[currentState]:
                # do trasition
                return self.transitions[currentState][event]
            else:
                # else if there is no transition available
                return currentState

    # Give the game an event and try to perfrom a state transition if possible.
    def Update(self, event):
        self.currentState = self.Transition(self.currentState, event)

    # Return the current state
    def GetState(self):
        return self.currentState

    # check state
    def IsPaused(self):
        if self.currentState == 'paused':
            return True
        else:
            return False

    # check state
    def IsDarkness(self):
        if self.currentState == 'darkness':
            return True
        else:
            return False

    # check state
    def PlayerIsDead(self):
        if self.currentState == 'playerDead':
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



