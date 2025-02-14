class Bus1:
    def __init__(self, arsId=None, stNm=None):
        self.arsId = arsId # 정류소 id
        self.stNm = stNm

    def __str__(self):
        s = ''
        s += '정류소고유번호' + self.arsId + '\n'  # 확인 필요
        s += '정류소명' + self.stNm + '\n'

        return s

class Bus2:
    def __init__(self,  stNm=None,rtNm=None, firstTm=None,lastTm=None, term=None,
                 vehId1=None,plainNo1=None, busType1=None, arrmsg1=None, reride_Num1=None, isLast1=None,
                 vehId2=None,plainNo2=None, busType2=None, arrmsg2=None, reride_Num2=None, isLast2=None):


        self.stNm = stNm # 정류소명
        self.rtNm = rtNm  # 노선명
        self.firstTm = firstTm # 첫차시간
        self.lastTm = lastTm # 막차시간
        self.term = term # 배차간격 (분)


        self.vehId1 = vehId1  # 도착예정버스ID
        self.plainNo1 = plainNo1  # 도착예정버스의 차량유형
        self.busType1 = busType1  # 첫번째 도착예정 버스의 도착정보메시지
        self.arrmsg1 = arrmsg1  # 첫번째 도착예정 버스의 도착정보메시지
        self.reride_Num1 = reride_Num1  # 첫번째 도착예정 버스의 버스내부 제공용 현재 재차 인원
        self.isLast1 = isLast1  # 도착예정버스의 막차여부

        self.vehId2 = vehId2  # 도착예정버스ID
        self.plainNo2 = plainNo2  # 도착예정버스의 차량유형
        self.busType2 = busType2  # 첫번째 도착예정 버스의 도착정보메시지
        self.arrmsg2 = arrmsg2  # 첫번째 도착예정 버스의 도착정보메시지
        self.reride_Num2 = reride_Num2  # 첫번째 도착예정 버스의 버스내부 제공용 현재 재차 인원
        self.isLast2 = isLast2  # 도착예정버스의 막차여부


    def __str__(self):
        s = ''
        s += '정류소명' + self.stNm + '\n'
        s += '노선명' + self.rtNm + '\n'
        s += '첫차시간: ' + self.firstTm + '\n'
        s += '막차시간: ' + self.lastTm + '\n'
        s += '배차간격: ' + self.term + '\n'

        s += '첫번째 도착예정버스ID: ' + self.vehId1 + '\n'
        s += '첫번째 도착예정버스의 차량번호: ' + self.plainNo1 + '\n'
        s += '첫번째 도착예정버스의 차량유형: ' + self.busType1 + '\n'
        s += '첫번째 도착예정 버스의 도착정보메시지: ' + self.arrmsg1 + '\n'
        s += '첫번째 도착예정 버스의 버스내부 제공용 현재 재차 인원: ' + self.reride_Num1 + '\n'
        s += '첫번째 도착예정버스의 막차여부: ' + self.isLast1 + '\n'

        s += '두번째 도착예정버스ID: ' + self.vehId2 + '\n'
        s += '두번째 도착예정버스의 차량번호: ' + self.plainNo2 + '\n'
        s += '두번째 도착예정버스의 차량유형: ' + self.busType1 + '\n'
        s += '두번째 도착예정 버스의 도착정보메시지: ' + self.arrmsg2 + '\n'
        s += '두번째 도착예정 버스의 버스내부 제공용 현재 재차 인원: ' + self.reride_Num2 + '\n'
        s += '두번째 도착예정버스의 막차여부: ' + self.isLast2 + '\n'
        return s

class station1:
    def __init__(self, arsId=None, gpsX=None, gpsY=None, stationNm=None,stationId=None, dist=None):
        self.arsId = arsId  # 정류소 번호
        self.gpsX = gpsX # 정류소 좌표X (GRS80)
        self.gpsY = gpsY	 # 정류소 좌표Y (GRS80)
        self.stationNm = stationNm  # 정류소명
        self.stationId = stationId  # 정류소 고유 ID
        self.dist = dist	  # 거리
    def __str__(self):
        s = ''
        s += '정류소 번호' + self.arsId + '\n'  # 확인 필요
        s += '정류소 좌표X' + self.gpsX + '\n'  # 확인 필요
        s += '정류소 좌표Y' + self.gpsY + '\n'
        s += '정류소명' + self.stationNm + '\n'
        s += '정류소 고유 ID' + self.stationId + '\n'
        s += '거리' + self.dist + '\n'


        return s