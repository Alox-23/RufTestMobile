from kivy.app import App
from timerScreen import TimerScreen
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
        start_timer = button.Button(text = "bru")
        start_timer.on_press = self.start_timer
        nextBtn.on_press = self.send_results
        layout.add_widget(nameLabel)
        layout.add_widget(nameEnt)
        layout.add_widget(ageLabel)
        layout.add_widget(start_timer)
        layout.add_widget(ageEnt)
        layout.add_widget(test1Label)
        layout.add_widget(test1Btn)
        layout.add_widget(test1Ent)
        layout.add_widget(nextBtn)
        self.add_widget(layout)
        self.sec = 5
    
    def start_timer(self):
        self.manager.add_widget(TimerScreen("t", self.sec))
        self.manager.current = "t"

    def send_results(self):
        self.manager.transition.direction = "left"
        self.manager.current = "3"
