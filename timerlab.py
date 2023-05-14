from kivy.uix.label import Label
from kivy.clock import Clock

class Sec(Label):
    def __init__(self, total, final_text, finish_func, **kwargs):
        self.total = total
        self.final = final_text
        self.finish = finish_func
        self.current = 0
        self.finished = False
        my_text = "seconds passes: " + str(self.current)
        super().__init__(text = my_text)
    
    def start(self):
        Clock.schedule_interval(self.change, 1)
    
    def change(self, dt):
        self.current += 1
        self.text = "seconds passed: " + str(self.current)
        if self.current >= self.total:
            self.finish()
            return False