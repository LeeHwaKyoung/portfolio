import requests
import time
import schedule
from datetime import timedelta
from datetime import datetime

# addrPred= "http://192.168.27.32:5000"
#URL = "/landslide/api/risks?place_code=GRMS01"

addrPred = "http://127.0.0.1:5000"
URL = "/landresponse"

def sendRequest(addrPred, URL):
    response = requests.get(addrPred+URL)
    return response

def job():
    data = sendRequest(addrPred, URL).json()
    print(data)
    
    #가상 데이터
    # result_code = 0
    # base_date = '20220517'
    # base_time = '1700'
    # place_code = 'GRMS01'
    # place_coordinate = [273243.3, 3235323.3]
    # risk_level = [0, 0, 2, 1, 0, 1, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0]

    # fcstTime = dateReturn(base_date, base_time) 
    
    # insert문 for문 25번 돌리기 (예측 날짜, 예측 시간, 장소 코드, 좌표 위도, 좌표 경도, 위험도, 현재 시간) / db에 테이블 만들어지면 실제로 넣어보기
    #for i in range(25):
        #fcstTime[i][1], fcstTime[i][0], place_code, place_coordinate[0], place_coordinate[1], risk_level[i], getdate()
        # insertDB = "INSERT INTO dbo.tb_테이블명(예측 시간, 장소 코드, 좌표 위도, 좌표 경도, 위험도, 현재 시간) VALUES('%s', '%s', '%f', '%f', '%d', getdate())"%(data["forecast_time"], data["place_code"], data["place_coordinate"][0], data["place_coordinate"][1], risk_level[i], )
    
# def insertDB():
#     print()

def dateReturn(baseDate, baseTime):
    current = datetime.strptime(baseDate, "%Y%m%d")
    tomorrow = current + timedelta(days=1)

    baseTimeint = int(baseTime)

    fcstTime = []
    fcstTime.append([baseTimeint, baseDate])
    baseDateStr = ""

    for i in range(24):
        a = fcstTime[-1][0]+100
        baseDateStr = current.strftime("%Y%m%d")
        if a == 2400:
            a = 0
            current = current + timedelta(days=1)
            baseDateStr = current.strftime("%Y%m%d")
        fcstTime.append([a, baseDateStr])

    for i in range(len(fcstTime)):
        fcstTime[i][0] = str(fcstTime[i][0]).zfill(4)

    print(fcstTime)
    return fcstTime

if __name__ == "__main__":
    # schedule.every(10).seconds.do(job)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    job() #테스트용 코드(나중에 지울것)

    #지금 주석처리 한것은 지우면 안됨 다 유효한 코드 나중에 실행해야 함