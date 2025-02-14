import pymysql
from datetime import datetime, timedelta
from reserve.vo import Reserve

class ReserveDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='nbus', charset='utf8')

    def disconn(self):
        self.conn.close()

    # 추가 메서드
    def insert(self, a:Reserve):
        #1. db 커넥션 수립
        self.connect()

        # 2. 사용할 cursor객체 생성. db 작업 메서드가 이 클래스에 정의되어 있으므로 꼭 필요.
        cursor = self.conn.cursor()

        # 3. 실행할 sql문 정의
        sql = 'insert into reserve(reservenum, resdate, id, arrmsg, rtNm, plainNo, stNm, stNmD, reserve, etc) ' \
              'values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        # 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
        d = (a.reservenum, a.resdate, a.id, a.arrmsg, a.rtNm, a.plainNo, a.stNm, a.stNmD, a.reserve, a.etc)

        # 5. sql 실행(실행할 sql, %s매칭한 튜플)
        cursor.execute(sql, d)

        # 6. 쓰기동작(insert, update, delete) 에서 쓰기 완료
        self.conn.commit()

        # db 커넥션 끊음
        self.disconn()

        # 검색 메서드
    def select(self, id:str):
        try:
            self.connect()#db연결
            cursor=self.conn.cursor() # 사용할 커서 객체 생성
            sql = 'select*from reserve where id=%s'
            d=(id,) #(O,) 튜플로 만들기 ',' 없으면 그냥 문자열로 된다.
            cursor.execute(sql, d) #sql 실행
            row = cursor.fetchone() # fetchone() : 현재 커서 위치의 한 줄 추출
            if row:
                return Reserve(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def selectById(self, id:str): #name 기준 검색, 여러개 검색
        res=[]
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            # sql = 'select*from reserve where name like %s'  # like 활용
            sql = 'select*from reserve where id=%s' # like 활용
            d = (id,)
            cursor.execute(sql, d)  # sql 실행
            for row in cursor:
                res.append(Reserve(reservenum=row[0],resdate=row[1],id=row[2], arrmsg=row[3],
                               rtNm=row[4], plainNo=row[5], stNm=row[6], stNmD=row[7],
                               reserve=row[8], etc=row[9]))
            #res =[Reserve(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            #      for row in cursor]
            return res

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def selectbyDate(self, id: str):  # resdate 기준 검색
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select * from reserve where id=%s and (resdate > %s)'
            tmp_now = str(datetime.now().date()) + ' 00:00:00'
            d = (id, tmp_now)  # (O,) 튜플로 만들기 ',' 없으면 그냥 문자열로 된다.
            cursor.execute(sql, d)  # sql 실행
            row = cursor.fetchall()  # fetchone() : 현재 커서 위치의 한 줄 추출
            todayres = []
            for i in range(len(row)):
                todayres.append((row[i][0], row[i][1], row[i][2], row[i][3], row[i][4], row[i][5], row[i][6], row[i][7],
                                 row[i][8], row[i][9]))
            return todayres
            # if row:
            #    return Reserve(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def selectbyDatepast(self, id:str): # resdate 기준 검색
        try:
            self.connect()#db연결
            cursor=self.conn.cursor() # 사용할 커서 객체 생성
            sql = 'select * from reserve where id=%s and (resdate <%s)'
            tmp_now = str(datetime.now().date()) + ' 00:00:00'
            d=(id, tmp_now) #(O,) 튜플로 만들기 ',' 없으면 그냥 문자열로 된다.
            cursor.execute(sql, d)  # sql 실행
            row = cursor.fetchall()
            res = []
            for i in range(len(row)):
                res.append((row[i][0], row[i][1], row[i][2], row[i][3], row[i][4], row[i][5], row[i][6], row[i][7], row[i][8], row[i][9]))
            return res
        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 삭제(reservenum으로 삭제하기)
    def delete(self, reservenum:int):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'delete from reserve where reservenum ' \
                  '= %s'
            d = (reservenum,)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()
            return print('삭제가 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()

# 지금은 안씀
    def update(self, a:Reserve):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'update reserve set reservenum=%s, arrmsg=%s, rtNm=%s, plainNo=%s, stNm=%s,' \
                  'stNmD=%s, reserve=%s, etc=%s' \
                  'where id = %s'

            d = (a.reservenum, a.arrmsg, a.rtNm, a.plainNo, a.stNm, a.stNmD, a.reserve, a.etc, a.id)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()
            return print('수정이 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()


