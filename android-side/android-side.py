from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from joystick.joystick import Joystick
import requests

buttons = {
    'Y': 1,
    'B': 2,
    'A': 3,
    'X': 4,
    'UP': 5,
    'DOWN': 6,
    'LEFT': 7,
    'RIGHT': 8,
    'Rb': 9,
    'Lb': 10,
    'Rt': 11,
    'Lt': 12,
    'Guide': 13,
    'Back': 14,
    'Start': 15,
}


class Req:
    url = 'http://127.0.0.1:5000/api/controller'
    passw = 1234

class Main_screen(Screen):
    conf_image = 'Assets/conf.png'
    settings_btn = Button(background_normal=conf_image, background_down=conf_image)

    def createRequest(self, instance, is_stick=False, x=0, y=0):
        if not is_stick:
            btn_text = instance.text
            request = f'{Req.passw}B{buttons[btn_text]-1};1Z'
        else:
            request = f'{Req.passw}S{instance};{x},{y}Z'
        
        try:
            self.errorlabel.text = ''
            requests.get(f'{Req.url}/{request}')
        except Exception as e:
            self.errorlabel.text = 'Connection Error! Check API\'s url and try again.'
            # print(e)

    def createReleaseRequest(self, instance):
        
        btn_text = instance.text
        request = f'{Req.passw}B{buttons[btn_text]-1};0Z'
        try:
            requests.get(f'{Req.url}/{request}')
            self.errorlabel.text = ''
        except:
            self.errorlabel.text = 'Connection Error! Check API\'s url and try again.'



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=11)
        settings_layout = BoxLayout()

        # layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Button(text='Lt', on_press=self.createRequest, on_release=self.createReleaseRequest))
        for i in range(2):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='Back', on_press=self.createRequest, on_release=self.createReleaseRequest))
        self.errorlabel = Label()
        layout.add_widget(self.errorlabel)
        layout.add_widget(Button(text='Start', on_press=self.createRequest, on_release=self.createReleaseRequest))
        for i in range(2):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='Rt', on_press=self.createRequest, on_release=self.createReleaseRequest))
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Button(text='Lb', on_press=self.createRequest, on_release=self.createReleaseRequest))
        for i in range(3):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='Guide', on_press=self.createRequest, on_release=self.createReleaseRequest))
        for i in range(3):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='Rb', on_press=self.createRequest, on_release=self.createReleaseRequest))
        layout.add_widget(Widget())
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
        layout.add_widget(Button(text='UP', on_press=self.createRequest, on_release=self.createReleaseRequest))
        for i in range(5):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='Y', on_press=self.createRequest, on_release=self.createReleaseRequest))
        layout.add_widget(Widget())
        # row 2
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Button(text='LEFT', on_press=self.createRequest, on_release=self.createReleaseRequest))
        layout.add_widget(Widget())
        layout.add_widget(Button(text='RIGHT', on_press=self.createRequest, on_release=self.createReleaseRequest))
        for i in range(3):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='X', on_press=self.createRequest, on_release=self.createReleaseRequest))
        layout.add_widget(Widget())
        layout.add_widget(Button(text='B', on_press=self.createRequest, on_release=self.createReleaseRequest))
        # row 3
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(Button(text='DOWN', on_press=self.createRequest, on_release=self.createReleaseRequest))
        for i in range(5):
            layout.add_widget(Widget())
        layout.add_widget(Button(text='A', on_press=self.createRequest, on_release=self.createReleaseRequest))
        # row 4
        layout.add_widget(Widget())
        for i in range(15):
            layout.add_widget(Widget())
        joystick = Joystick(size=(200, 200))
        joystick.bind(pad=self.update_coordinates1)
        layout.add_widget(joystick)
        for i in range(3):
            layout.add_widget(Widget())
        joystick2 = Joystick()
        joystick2.bind(pad=self.update_coordinates2)
        layout.add_widget(joystick2)
        
        self.add_widget(layout)

    def update_coordinates1(self, joystick, pad):
        x = str(pad[0])[0:5]
        y = str(pad[1])[0:5]
        self.createRequest(0, is_stick=True, x=x, y=y)

    def update_coordinates2(self, joystick, pad):
        x = str(pad[0])[0:5]
        y = str(pad[1])[0:5]
        self.createRequest(1, is_stick=True, x=x, y=y)

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

    def change_url(self, instance):
        try:
            Req.url = self.input_url_field.text
            Req.passw = int(self.input_passw_field.text)
        except:
            pass
        print(Req.url)
        print(Req.passw)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_back.on_press = self.go_to_gamepad
        self.btn_tuto.on_press = self.go_to_tutorial
        main_layout = BoxLayout(orientation='vertical')
        row_layout = BoxLayout(orientation='horizontal')
        row_layout_input = BoxLayout(orientation='horizontal')
        main_layout.add_widget(Label(text='Config Screen'))
        row_layout.add_widget(self.btn_tuto)
        row_layout.add_widget(self.btn_back)
        self.input_url_field = TextInput(text=Req.url, multiline=False)
        self.input_passw_field = TextInput(text=str(Req.passw), multiline=False)
        row_layout_input.add_widget(self.input_url_field)
        row_layout_input.add_widget(self.input_passw_field)
        row_layout_input.add_widget(Button(text='Change connection settings', on_press=self.change_url))
        main_layout.add_widget(row_layout_input)
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

