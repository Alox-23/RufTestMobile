from kivy.app import App
from kivy.uix import button, boxlayout, screenmanager, label, textinput

class Screen3(screenmanager.Screen):
    def __init__(self, name):
        super().__init__(name = name)
        indexLabel = label.Label(text = "Your rufier index: 0")
        levelLabel = label.Label(text = "You are average")
        layout = boxlayout.BoxLayout(orientation = "vertical")
        layout.add_widget(indexLabel)
        layout.add_widget(levelLabel)
        self.add_widget(layout)