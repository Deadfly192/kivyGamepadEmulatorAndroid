from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from joystick.joystick import Joystick


class Main_screen(Screen):
    conf_image = 'Assets/conf.png'
    settings_btn = Button(background_normal=conf_image, background_down=conf_image)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=11)
        settings_layout = BoxLayout()
        for i in range(5):
            layout.add_widget(Widget())
        layout.add_widget(settings_layout)
        self.settings_btn.on_press = self.go_to_config
        settings_layout.add_widget(self.settings_btn)
        for i in range(5):
            layout.add_widget(Widget())
        # row 1
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Button(text='UP'))
        for i in range(5):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='1'))
        layout.add_widget(Widget())
        # row 2
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Button(text='LEFT'))
        layout.add_widget(Widget())
        layout.add_widget(Button(text='RIGHT'))  
        for i in range(3):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='4'))
        layout.add_widget(Widget())
        layout.add_widget(Button(text='2'))
        # row 3
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Button(text='DOWN'))
        for i in range(5):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='3'))
        # row 4
        layout.add_widget(Widget())
        for i in range(15):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='stick_left'))
        for i in range(3):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='stick_right'))


        self.add_widget(layout)

    def update_coordinates1(self, joystick, pad):
        x = str(pad[0])[0:5]
        y = str(pad[1])[0:5]
        self.labelst.text = f"{x};    {y}"



    def update_coordinates2(self, joystick, pad):
        x = str(pad[0])[0:5]
        y = str(pad[1])[0:5]
        self.labelst2.text = f"{x};    {y}"

    def go_to_config(self):
        self.manager.transition = SlideTransition(direction="down")
        self.manager.current = 'config'

class Tutorial_screen(Screen):
    
    btn_back = Button(text='Back')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_back.on_press = self.go_to_config
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Tutorial Screen'))
        layout.add_widget(self.btn_back)
        self.add_widget(layout)

    def go_to_config(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'config'
class Config_screen(Screen):
    
    btn_tuto = Button(text='tuto')
    btn_back = Button(text='Back')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_back.on_press = self.go_to_gamepad
        self.btn_tuto.on_press = self.go_to_tutorial
        main_layout = BoxLayout(orientation='vertical')
        row_layout = BoxLayout(orientation='horizontal')
        main_layout.add_widget(Label(text='Config Screen'))
        row_layout.add_widget(self.btn_tuto)
        row_layout.add_widget(self.btn_back)
        main_layout.add_widget(row_layout)
        self.add_widget(main_layout)

    def go_to_gamepad(self):
        self.manager.transition = SlideTransition(direction="up")
        self.manager.current = 'main'
    def go_to_tutorial(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'tutorial'
class GamePad(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main_screen(name='main'))
        sm.add_widget(Tutorial_screen(name='tutorial'))
        sm.add_widget(Config_screen(name='config'))
        return sm
    
    
if __name__ == '__main__':
    app = GamePad()
    app.run()

