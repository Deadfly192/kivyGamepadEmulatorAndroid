from flask import Flask, request
from simulatingGamepad import Simulator
app = Flask(__name__)\

a = Simulator(gamepads_amount=1)
a.change_passwords(1, 1234)

@app.route('/api/controller/<keyCode>', methods=['POST', 'GET'])
def controller(keyCode):
    if request.method == "GET":
        a.scan(keyCode)
        print(keyCode)
        return 'ok'
    return 'Error 404'

if __name__ == "__main__":
    app.run(debug=True)

# ! http://127.0.0.1:5000/api/controller
















    #     if keyCode == 3:
    #         print('A')
    #     if keyCode == 2:
    #         print('B')
    #     if keyCode == 1:
    #         print('Y')
    #     if keyCode == 4:
    #         print('X')
    #     if keyCode == 5:
    #         print('DOWN')
    #     if keyCode == 6:
    #         print('UP')
    #     if keyCode == 7:
    #         print('LEFT')
    #     if keyCode == 8:
    #         print('RIGHT')
    #     if keyCode == 9:
    #         print('Rb')
    #     if keyCode == 10:
    #         print('Lb')
    #     if keyCode == 11:
    #         print('Rt')
    #     if keyCode == 12:
    #         print('Lt')
    #     if keyCode == 103:
    #         print('Ar')
    #     if keyCode == 102:
    #         print('Br')
    #     if keyCode == 101:
    #         print('Yr')
    #     if keyCode == 104:
    #         print('Xr')
    #     if keyCode == 105:
    #         print('DOWNr')
    #     if keyCode == 106:
    #         print('UPr')
    #     if keyCode == 107:
    #         print('LEFTr')
    #     if keyCode == 108:
    #         print('RIGHTr')
    #     if keyCode == 109:
    #         print('Rbr')
    #     if keyCode == 110:
    #         print('Lbr')
    #     if keyCode == 111:
    #         print('Rtr')
    #     if keyCode == 112:
    #         print('Ltr')