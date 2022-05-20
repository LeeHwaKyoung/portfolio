from flask import Flask, jsonify, render_template, request
import random
import datetime
import time
from datetime import date, timedelta
import tkinter
app = Flask (__name__)
 
@app.route('/')
def riskValue():
    return render_template('riskValueInput.html')

@app.route('/landresponseset', methods = ['POST', 'GET'])
def risk_set():

    global weights
    
    if request.method == 'POST':
        print('post')
        val = request.form
        val = val.to_dict()
        print(val['정상'], val['주의'], val['경보'], val['위험'])
        weights = [float(val['정상']), float(val['주의']), float(val['경보']), float(val['위험'])]
    
    code = [0, 1, 2, 3]

    now = time.localtime()
    year = "%d"%(now[0])
    month = "%d"%(now[1])
    day = "%d"%(now[2])
    hour = "%d"%(now[3])

    result_code = 0
    base_date = year+month+day
    if month in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        base_date = year+'0'+month+day
    
    base_time = hour+'00'
    if hour in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        base_time = '0'+hour+'00'

    place_code = 'GRMS01'

    place_coordinate = [273243.3, 3235323.3]    

    if not weights :
        weights = [7.5, 1, 1, 0.5]
        print(weights)

    risk_level = (random.choices(code, weights, k = 25))

    
    list = []
    list.append(result_code)
    list.append(base_date)
    list.append(base_time)
    list.append(place_code)
    list.append(place_coordinate)
    list.append(risk_level)

    landValue = 'result_code:%d, base_date:%s, base_time:%s, place_code:%s, place_coordinate:%s, risk_level:%s'%(result_code, base_date, base_time, place_code, place_coordinate, risk_level)

    print(landValue)

    return render_template('riskValueInput.html', landValue = landValue) 

@app.route('/landresponse', methods = ['POST', 'GET'])
def hello_land():

    # global weights
    
    # if request.method == 'POST':
    #     print('post')
    #     val = request.form
    #     val = val.to_dict()
    #     print(val['정상'], val['주의'], val['경보'], val['위험'])
    #     weights = [float(val['정상']), float(val['주의']), float(val['경보']), float(val['위험'])]
    
    global weights
    code = [0, 1, 2, 3] 
    
    
    now = time.localtime()
    year = "%d"%(now[0])
    month = "%d"%(now[1])
    day = "%d"%(now[2])
    hour = "%d"%(now[3])

    result_code = 0
    base_date = year+month+day
    if month in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        base_date = year+'0'+month+day
    
    base_time = hour+'00'
    if hour in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        base_time = '0'+hour+'00'

    place_code = 'GRMS01'

    place_coordinate = [273243.3, 3235323.3]    

    if not weights :
        weights = [7.5, 1, 1, 0.5]
        print(weights)

    risk_level = (random.choices(code, weights, k = 25))

    
    list = []
    list.append(result_code)
    list.append(base_date)
    list.append(base_time)
    list.append(place_code)
    list.append(place_coordinate)
    list.append(risk_level)


    # landValue = str(jsonify('result_code:%d, base_date:%s, base_time:%s, place_code:%s, place_coordinate:%s, risk_level:%s'%(result_code, base_date, base_time, place_code, place_coordinate, risk_level)))

    # print(landValue)


    return jsonify('result_code:%d, base_date:%s, base_time:%s, place_code:%s, place_coordinate:%s, risk_level:%s'%(result_code, base_date, base_time, place_code, place_coordinate, risk_level))
    # return render_template('riskValueInput.html', landValue = landValue)
    #result_code, base_date, base_time, place_code, place_coordinate, risk_level    

 
if __name__ == "__main__":
    

    # window = tkinter.Tk()
    

    # window.title("산사태 조기 예측 시스템 Simulator")
    # window.geometry("500x400+100+100")
    # # # window.resizable(False, False)

    # # label = tkinter.Label(window, "text")
    # # label.pack()

    # window.mainloop()
    app.run(host='0.0.0.0')