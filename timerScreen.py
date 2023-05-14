from timerlab import Sec
from kivy.app import App
from kivy.uix import button, boxlayout, screenmanager, label, textinput

class TimerScreen(screenmanager.Screen):
    def __init__(self, name, sec):
        super().__init__(name = name)
        self.timer = Sec(sec, final_text="Timer finished", finish_func = self.finish)
        self.timer.start()
        self.btn = button.Button(text = "Go back")
        self.btn.on_press = self.switch_back
        self.layout = boxlayout.BoxLayout()
        self.layout.add_widget(self.timer)
        self.add_widget(self.layout)
    
    def finish(self):
        self.layout.add_widget(self.btn)
    
    def switch_back(self):
        self.manager.transition.direction = "left"
        self.manager.current = "2"
        self.manager.remove_widget(self)