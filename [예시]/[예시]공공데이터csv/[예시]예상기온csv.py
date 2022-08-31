# -*- coding: utf-8 -*-
"""[예시]예상기온csv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vITi2-6gtcPMfF8mx8riahcXkiisztHY

#**기상청**
**1. 오늘의 예상 기온 구하기**
*   만약 날짜가 같다면 (올해-전년해)의 기온 차를 더해 평균 구함
   → 지구온난화에 따른 기온 상승률 반영하기 위함
*   평균을 토대로 입력한 전해 + 차이 (수열)

**2. 오늘의 옷차림 추천** (출처: 네이버 기온별 옷차림)

**3. 과거 같았던 기온의 날짜 소개**



#**오차범위**
1. 습도, 강수량 등의 데이터 미포함으로 재미로 해보기!^^
"""

## 기초작업
import csv
data1 = csv.reader(open('data2.csv'))
next(data1)

year=[]
day=[] 
temp=[]
result=[]

for row in data1 :
  if row[1] != '' and row[2] != '' :
    year.append(row[0])
    # 연도 제외하고 월, 일 day에 넣어주기
    day.append(str(row[0].split('-')[1])+str(row[0].split('-')[2]))
    #온도도 차례대로 넣어주기
    temp.append(float(row[1]))

i=0
d_temp = 0
s_temp = 0
day2 = []
d1 = []


## 수열 구하기
data2 = csv.reader(open('data2.csv'))
next(data2)

for row in data2 :
  for k in range(365) :
    #월일이 같다면
    if str(row[0].split('-')[1])+str(row[0].split('-')[2]) == str(day[k]) :
      #기온의 차이 넣어주기
      if s_temp == 0:
        s_temp = float(temp[k])
      else:
        d_temp += float(temp[k])-s_temp
        s_temp = float(temp[k])
      i += 1
  #날짜별로 기온의 상승률, 하락률 반영
  day2.append(row[0].split('-')[1]+row[0].split('-')[2])
  d1.append(round(float(d_temp/i),2))



## 입력한 날짜의 해의 기온 예상

# 날짜 입력하기 : 주의 - 2022.07.26. 이후로 입력해야 함.
while True:
  in_put = input('미래에 알고자하는 날짜를 입력해 주세요. (형식: 2026-06-14) : ')
  in_year = in_put.split('-')[0]
  in_day = in_put.split('-')[1]+in_put.split('-')[2]
  if int(in_year+in_day) <= 20220726 :
    print('다시 입력해 주세요.')
    continue
  else:
    break

# 과거 해당 날짜의 기온 찾기
re_temp = 0
rd_temp = 0

data3 = csv.reader(open('data2.csv'))
next(data3)

for row in data3 :
  #해당 날짜의 수열차 구하기
  for j in range(365):
    if in_day == str(day2[j]) :
      rd_temp = d1[j]
      #print(rd_temp)
  #해당 날짜의 기온과 배수 구하기
  if int(in_day) <= int('0726') :
    ye = 2022
    if int(row[0].split('-')[0]+row[0].split('-')[1]+row[0].split('-')[2]) == int('2022'+in_day) :
      #print(row[1])
      re_temp = float(row[1])
  else :
    ye = 2021
    if int(row[0].split('-')[0]+row[0].split('-')[1]+row[0].split('-')[2]) == int('2021'+in_day) :
      re_temp = float(row[1])

# 예상 기온 구하기
pre_temp = round(float(re_temp)+float(rd_temp)*(int(in_year)-ye),1)
print('\n'+str(in_put)+'의 평균 기온은 '+str(pre_temp)+'도로 예상됩니다.')


# 기온별 옷차림
if pre_temp <= 4:
  print('이 날의 옷차림은 패딩, 두꺼운 코트, 누빔옷, 기모, 목도리를 추천드립니다.')
elif pre_temp <= 8:
  print('이 날의 옷차림은 울 코트, 히트텍, 가죽옷, 기모를 추천드립니다.')
elif pre_temp <= 11:
  print('이 날의 옷차림은 트렌치코트, 야상, 점퍼를 추천드립니다.')
elif pre_temp <= 16:
  print('이 날의 옷차림은 자켓, 가디건, 맨투맨, 청바지를 추천드립니다.')
elif pre_temp <= 22:
  print('이 날의 옷차림은 얇은 가디건, 블라우스, 긴팔티, 면바지를 추천드립니다.')
elif pre_temp <= 27:
  print('이 날의 옷차림은 반팔, 얇은 셔츠, 반바지를 추천드립니다.')
else:
  print('이 날의 옷차림은 민소매, 반팔, 반바지, 린넨 옷을 추천드립니다.')

# 환경 안내(과거 기온)
eco_day = []

for i in range(len(temp)):
  if temp[i] == pre_temp:
  # 과거 같은 기온 프린터
    if int(year[i].split('-')[0]+year[i].split('-')[1]+year[i].split('-')[2]) < int(in_year+in_day) :
      eco_day.append(year[i])
  
# 같은 온도가 없음
if eco_day == []:
  print('이 날짜는 데이터상 과거와 같은 평균기온은 없습니다.')
else:
  print('과거 이 날짜와 평균 기온이 같았던 날은 '+str(eco_day)+'이었습니다. ')

print('\n오늘도 환경을 생각하는 알찬 하루가 되시길 바라며, 좋은 하루 보내세요. ^^*')