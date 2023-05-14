from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

class Sec(Label):
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        my_text = "seconds passes: " + str(self.current)
        super().__init__(text = my_text)
    
    def start(self):
        Clock.schedule_interval(self.change, 1)
    
    def change(self, dt):
        self.current += 1
        self.text = "seconds passed: " + str(self.current)
        if self.current >= self.total:
            return False

class FirstScrean(Screen):
    def __init__(self, name):
        super().__init__(name = name)
        btn = Button(text = "START TIMER")
        self.label = Sec(5)
        btn.on_press = self.label.start
        self.layout = BoxLayout()
        self.layout.add_widget(btn)
        self.layout.add_widget(self.label)
        self.add_widget(self.layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScrean("1"))
        return sm

app = MyApp()
app.run()