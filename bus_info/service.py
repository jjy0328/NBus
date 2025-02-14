import requests
from bs4 import BeautifulSoup
import json

from bus_info.vo import Bus1, Bus2, station1


class Service:
    def __init__(self):
        self.key = 'AKfan37NDGnLV%2FFaafUPpYaYwl2YG91sOrLFQX1vco5iqRInax4RzmyoEDOLGXIUoXlKmz0mCnEToQn7wRjtOg%3D%3D'

    def getStationByName(self, strSrch): # 버스 이름으로 검색하는 메소드 생성
        url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByName?'
        url += 'serviceKey=' + self.key
        url += '&stSrch=' + strSrch
        html = requests.get(url).text # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
        root = BeautifulSoup(html, 'lxml-xml') # 파서 객체 생성
        headerCd = root.find('headerCd').text
        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        routeList = root.find_all('itemList') #태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        for route in routeList:
            arsId = route.find('arsId').text + '@' + route.find('stId').text
            stNm = route.find('stNm').text

            res.append(Bus1(arsId=arsId, stNm=stNm))

        return res

    def getRouteByStation(self, arsId):  # getBusInfoByStationId
        url = 'http://ws.bus.go.kr/api/rest/stationinfo/getRouteByStation?'
        url += 'ServiceKey=' + self.key
        url += '&arsId=' + arsId

        html = requests.get(url).text  # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
        root = BeautifulSoup(html, 'lxml-xml')  # 파서 객체 생성
        headerCd = root.find('headerCd').text
        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        routeList = root.find_all('itemList')  # 태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        for route in routeList:
            busRouteId = route.find('busRouteId').text
            # busRouteNm = route.find('busRouteNm').text
            res.append(busRouteId)

        return res

    def getStaionByRoute(self, busRouteId, stId):  # 버스 노선ID 넣으면 노선 가는 모든 정류장의 순번, 정류장ID
        url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?'
        url += 'ServiceKey=' + self.key
        url += '&busRouteId=' + busRouteId

        html = requests.get(url).text  # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
        root = BeautifulSoup(html, 'lxml-xml')  # 파서 객체 생성
        headerCd = root.find('headerCd').text
        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        stationList = root.find_all('itemList')  # 태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        for station in stationList:
            busRouteId = station.find('busRouteId').text
            seq = station.find('seq').text
            station = station.find('station').text

            if stId == station:
                res.extend([station, busRouteId, seq]) # getArrInfoByRoute에 들어갈 파람 stId,busRouteId, seq

        return res

    #seq=None, name=None, direction=None, x=None, y=None
    def getArrInfoByRoute(self, stId,busRouteId, seq):
        url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?'
        url += 'ServiceKey=' + self.key
        url += '&stId=' + stId
        url += '&busRouteId=' + busRouteId
        url += '&ord=' + seq

        html = requests.get(url).text  # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
        root = BeautifulSoup(html, 'lxml-xml')  # 파서 객체 생성
        headerCd = root.find('headerCd').text
        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        stationList = root.find_all('itemList')  # 태그 이름이 'itemList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        rerideNumDic = {'0': '정보없음','3':'여유', '4':'보통', '5':'혼잡'}
        busTypeDic = {'0': '일반', '1': '저상'}
        for station in stationList:
            stNm = station.find('stNm').text
            rtNm = station.find('rtNm').text
            firstTm = station.find('firstTm').text
            firstTm = firstTm[8:10]+'시'+ firstTm[10:12] +'분'
            lastTm = station.find('lastTm').text
            lastTm = lastTm[8:10] + '시' + lastTm[10:12] + '분'
            term = station.find('term').text + '분'

            vehId1 = station.find('vehId1').text
            plainNo1 = station.find('plainNo1').text
            busType1 = busTypeDic[station.find('busType1').text]
            arrmsg1 = station.find('arrmsg1').text
            reride_Num1 = rerideNumDic[station.find('reride_Num1').text]

            isLast1 = station.find('isLast1').text
            vehId2 = station.find('vehId2').text
            plainNo2 = station.find('plainNo2').text
            busType2 = busTypeDic[station.find('busType2').text]
            arrmsg2 = station.find('arrmsg2').text
            reride_Num2 = rerideNumDic[station.find('reride_Num1').text]
            isLast2 = station.find('isLast2').text
            res.append(Bus2(stNm=stNm,rtNm=rtNm, firstTm=firstTm,lastTm=lastTm, term=term,
                 vehId1=vehId1, plainNo1=plainNo1,busType1=busType1, arrmsg1=arrmsg1, reride_Num1=reride_Num1, isLast1=isLast1,
                 vehId2=vehId2, plainNo2=plainNo2, busType2=busType2, arrmsg2=arrmsg2, reride_Num2=reride_Num2, isLast2=isLast2))
        return res


    def getStationByPos(self, tmX,tmY,radius): # tmX 127 머시기로 시작함 # tmY 37 뭐시기로 시작함
        # &tmX=126.8973568&tmY=37.51936&radius=100
        url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos?'
        url += 'serviceKey=' + self.key
        url += '&tmX=' + str(tmX) + '&tmY=' + str(tmY) # 좌표
        url += '&radius=' + str(radius) # 반경

        html = requests.get(url).text # url로 요청을 보내고 받은 응답 페이지 텍스트를 html에 저장
        root = BeautifulSoup(html, 'lxml-xml') # 파서 객체 생성
        headerCd = root.find('headerCd').text
        if headerCd != '0':
            msg = root.find('headerMsg').text
            print(msg)
            return

        routeList = root.find_all('itemList') #태그 이름이 'StationList'인 모든 태그 요소를 리스트에 담아서 반환
        res = []
        for route in routeList:
            arsId = route.find('arsId').text
            gpsX = route.find('gpsX').text
            gpsY = route.find('gpsY').text
            dist = route.find('dist').text
            stationNm = route.find('stationNm').text
            stationId = route.find('stationId').text

            res.append(
                {
                    'arsId':arsId+ '@' + stationId,
                    'gpsX':gpsX,
                    'gpsY':gpsY,
                    'stationNm':stationNm,
                    'dist':dist
                }
            )

        return res