from kivy.app import App
from kivy.uix import button, boxlayout, screenmanager, label

class Screen1(screenmanager.Screen):
    def __init__(self, name):
        super().__init__(name = name)
        welcomeLable = label.Label(text = "Welcome to the Rufier test!!")
        subLable = label.Label(text = "Press the button below to start")
        startBtn = button.Button(text = "START")
        startBtn.on_press = self.start
        layout = boxlayout.BoxLayout()
        layout.add_widget(welcomeLable)
        layout.add_widget(subLable)
        layout.add_widget(startBtn)
        self.add_widget(layout)
    
    def start(self):
        self.manager.transition.direction = "left"
        self.manager.current = "2"