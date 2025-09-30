from kivy.app import App
from joystick.joystick import Joystick
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class DemoApp(App):
  def build(self):
    self.root = BoxLayout()
    self.root.padding = 50
    joystick = Joystick()
    joystick.bind(pad=self.update_coordinates1)
    self.root.add_widget(joystick)
    self.labelst = Label()
    self.labelst2 = Label()
    self.root.add_widget(self.labelst)
    self.root.add_widget(self.labelst2)
    joystick2 = Joystick()
    joystick2.bind(pad=self.update_coordinates2)
    self.root.add_widget(joystick2)

  def update_coordinates1(self, joystick, pad):
    x = str(pad[0])[0:5]
    y = str(pad[1])[0:5]
    self.labelst.text = f"{x};    {y}"



  def update_coordinates2(self, joystick, pad):
    x = str(pad[0])[0:5]
    y = str(pad[1])[0:5]
    self.labelst2.text = f"{x};    {y}"


DemoApp().run()