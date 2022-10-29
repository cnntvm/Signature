import urllib.request
import xml.dom.minidom
import bs4
import pandas as pd

encodingKey = "u%2FT6cFqR8gwBZ69RoAfitw%2FOEW1Dy6cjuCVy5i1lyhhQ3cYV5eDMwXF9tL%2B%2BelYC6%2FvsjFlrq7e4kEp4OPTk%2BA%3D%3D"
decodingKey = "u/T6cFqR8gwBZ69RoAfitw/OEW1Dy6cjuCVy5i1lyhhQ3cYV5eDMwXF9tL++elYC6/vsjFlrq7e4kEp4OPTk+A=="

key = input("행정구역코드 : ")
numOfRows = input("페이지당 건수(최대 1,000) :")

# request url정의
#8) 핼정동 단위 상가업소 조회 오퍼레이션 명세
url = "http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInDong?divId=adongCd&key="+str(key)+"&indsLclsCd=Q&numOfRows="+str(numOfRows)+"&pageNo=1&serviceKey="+encodingKey
request = urllib.request.Request(url)

# request보내기
response = urllib.request.urlopen(request)

# 결과 코드 정의
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    dom = xml.dom.minidom.parseString(response_body.decode('utf-8'))
    pretty_xml_as_string = dom.toprettyxml()
    #print(pretty_xml_as_string)
else:
    print("Error Code:" + rescode)

xml_obj = bs4.BeautifulSoup(response_body,'lxml-xml')
rows = xml_obj.findAll('item')

# 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
row_list = [] # 행값
name_list = [] # 열이름값
value_list = [] #데이터값

# xml 안의 데이터 수집
for i in range(0, len(rows)):
    columns = rows[i].find_all()
    #첫째 행 데이터 수집
    for j in range(0,len(columns)):
        if i ==0:
            # 컬럼 이름 값 저장
            name_list.append(columns[j].name)
        # 컬럼의 각 데이터 값 저장
        value_list.append(columns[j].text)
    # 각 행의 value값 전체 저장
    row_list.append(value_list)
    # 데이터 리스트 값 초기화
    value_list=[]
    
restaurant_df = pd.DataFrame(row_list, columns=name_list)

#restaurant_df.to_csv('restaurant.csv', encoding='utf-8-sig')
restaurant_df.to_excel('restaurant.xlsx')