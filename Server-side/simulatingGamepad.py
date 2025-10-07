import vgamepad as vg
import time

xb = vg.XUSB_BUTTON
btns = [xb.XUSB_GAMEPAD_Y, xb.XUSB_GAMEPAD_B, xb.XUSB_GAMEPAD_A, xb.XUSB_GAMEPAD_X, 
        xb.XUSB_GAMEPAD_DPAD_UP, xb.XUSB_GAMEPAD_DPAD_DOWN, xb.XUSB_GAMEPAD_DPAD_LEFT, xb.XUSB_GAMEPAD_DPAD_RIGHT,
        xb.XUSB_GAMEPAD_RIGHT_THUMB, xb.XUSB_GAMEPAD_LEFT_THUMB, xb.XUSB_GAMEPAD_RIGHT_SHOULDER, xb.XUSB_GAMEPAD_LEFT_SHOULDER,
        xb.XUSB_GAMEPAD_GUIDE, xb.XUSB_GAMEPAD_BACK, xb.XUSB_GAMEPAD_START]

class Gamepad:
    def __init__(self):
        self.gp = vg.VX360Gamepad()
        self.gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gp.update()
        time.sleep(0.1)
        self.gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        self.gp.update()


    def Stick(self, stick : int, x, y):
        if stick == 1:
            self.gp.right_joystick_float(x_value_float=float(x), y_value_float=float(y))
        else:
            self.gp.left_joystick_float(x_value_float=float(x), y_value_float=float(y))
        self.gp.update()

    def simbtn(self, btn_ID, press):
        if press == 1:
            if btn_ID:
                pass
            self.gp.press_button(button=btns[btn_ID])
        else:
            self.gp.release_button(button=btns[btn_ID])
        self.gp.update()
        

    def Parse(self, data : str):
        end = False
        for i in data:
            if data == 'Z':
                end = True
        if not end:
            pass
        if data[0] == 'S':
            _id = int(data[1])
            x = float(data[3:].split(',')[0])
            y = float(data[3:].split(',')[1].split('Z')[0])
            print(_id, x, y)
            self.Stick(_id, x, y)
        elif data[0] == 'B':
            _id = int(data[1])
            press = data[3:-1]
            self.simbtn(_id, press)   
        else:
            pass
    
    def __str__(self):
        print('there will be a help')

class Simulator:
    
    def __init__(self, pass1=1234, pass2=2234, pass3=3334, pass4=4444, gamepads_amount=4):
        self.passwords = {
            1: pass1,
            2: pass2,
            3: pass3,
            4: pass4
        }

        self.gamepads = {}
        for i in range(gamepads_amount):
            self.gamepads[i+1] = Gamepad()

    def change_passwords(self, number : int, password : int):
        if len(str(password)) == 4 and number in (1, 2, 3, 4):
            self.passwords[number] = password
        else:
            print('Bad input!')

    def scan(self, data : str):
        scan_pass = int(data[0:4])
        for i in self.passwords:
            if self.passwords[i] == scan_pass:
                self.gamepads[i].Parse(data[4:])

            













 





''' 
    структура
    0. Пароль
    4 цифры, например 1234


    1. стик или кнопка
    B - кнопка или S - стик
    
    2. айди
    в случае стика,
    0 - левый стик, 1 - правый стик
    в случае кнопки, элемент из списка btns
    
    3. значение
    в случае стика,
    x,y
    в случае кнопки,
    True или False
    true - нажали, false - отпустили

    4. Разделители и конец
    ; - Разделитель
    , - Разделитель x и y
    Z - конец строки

    Пример:

    B0;trueZ

    или

    S1;0.5,1.0Z
    '''
        # print(f"simbtn(btn_ID(int), press(bool)) - simulates buttons\nbtns list: \n{btns}\nStick(stick_ID(0-left, 1-right), x(float), y(float)) - emulates Stick\nParse(data(str)) - Parses a string with data\ndata string type:\n(there will be a string type)")