from kivy.app import App
from kivy.uix import button, boxlayout, screenmanager, label, textinput

class Screen2(screenmanager.Screen):
    def __init__(self, name):
        super().__init__(name = name)
        nameLabel = label.Label(text= "Enter your name:", size_hint = (0.2,0.2))
        nameEnt = textinput.TextInput(size_hint = (0.2,0.2))
        ageLabel = label.Label(text = "Enter your age", size_hint = (0.2,0.2))
        ageEnt = textinput.TextInput(size_hint = (0.2,0.2))
        test1Label = label.Label(text = "Lie on your back and take pusle for 15 sec. Clockt the 'Start first test' button to start the timer. Write down the result in the aproprite field.", size_hint = (0.2,0.2))
        test1Btn = button.Button(text = "Start first test", size_hint = (0.2,0.2))
        test1Ent = textinput.TextInput(size_hint = (0.2,0.2))
        nextBtn = button.Button(text = "Send the results.", size_hint = (0.2,0.2))
        layout = boxlayout.BoxLayout(orientation = "vertical")
        nextBtn.on_press = self.send_results
        layout.add_widget(nameLabel)
        layout.add_widget(nameEnt)
        layout.add_widget(ageLabel)
        layout.add_widget(ageEnt)
        layout.add_widget(test1Label)
        layout.add_widget(test1Btn)
        layout.add_widget(test1Ent)
        layout.add_widget(nextBtn)
        self.add_widget(layout)
    
    def send_results(self):
        self.manager.transition.direction = "left"
        self.manager.current = "3"
