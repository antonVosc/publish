class Attempts:
    def __init__(self, lst):
        self.attempts = lst
        self.inv = False
        self.game = True

    def list_attempts(self):
        if self.inv == False:
            print("Previous attempts:")
            if len(self.attempts) == 0:
                print('No previous attempts')
            else:
                self.attempts.reverse()
                for attempt in self.attempts:
                    print(attempt)