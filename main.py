from kivy.app import App
from kivy.uix import button, boxlayout, screenmanager, label
import screen1
import screen2
import screen3

class Main(App):
    def __init__(self):
        super().__init__()
    
    def build(self):
        sm = screenmanager.ScreenManager()
        sm.add_widget(screen1.Screen1("1"))
        sm.add_widget(screen2.Screen2("2"))
        sm.add_widget(screen3.Screen3("3"))
        return sm

if __name__ == "__main__":
    app = Main()
    app.run()