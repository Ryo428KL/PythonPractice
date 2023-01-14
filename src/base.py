# pythonの基本文法類を整理する

# 出力
#print 'hello world' # python2
print ('hello world') # python3

# 定義
val1 = 11
val2 = 'val2'
val3 = val1 == 11 # bool True or False ※先頭大文字なので注意
print(val1)
print(val2)
print(val3)

# データ型を確認する
print(type(val1))
print(type(val2))
print(type(val3))

# 配列
val4 = ['test1','test2','test3']
print(val4)
print(len(val4)) # 配列の長さ
print(type(val4))

# 配列の挿入操作
val5 = ['1','2']
val5.insert(2,'3') # index:2に対して'3'を挿入
print(val5)
val5.insert(100,'4') # index:100に対して'4'を挿入
print(val5)
print(len(val5)) # 結論：末尾に追加する場合は配列の長さより大きい値をindexに指定する必要がある?
val5.insert(0,'0') # index:0に対して'0'を挿入
print(val5)
val5.insert(len(val5),None) # pythonではnullはNoneと言うらしい
print(val5)
val5.insert(len(val5),'6')
print(val5)
print(len(val5))

# if文
val6 = 'こけっこっこー'
if val6 == 'にゃんこ':
  print('猫ですね')
elif val6 == 'わんこ':
  print('犬ですね')
else:
  print('猫と犬以外ですね')

# 日付型
import datetime
print(datetime.date.today())
print(datetime.datetime.today())
print(datetime.date(2023,1,14))
print(datetime.datetime(2023,1,14,20,25,16))
today = datetime.date.today()
now = datetime.datetime.today()
print(today.year)
print(today.month)
print(today.day)
print(now.hour)
print(now.minute)
print(now.second)

# 曜日 ※0 : 月曜日, 1 : 火曜日, 2 : 水曜日, 3 : 木曜日, 4 : 金曜日, 5 : 土曜日, 6 : 日曜日
print(datetime.date.today().weekday())
print(datetime.date(2023,1,1).weekday())

# for文
forAry = [1,2,3,4,5]
for data in forAry:
  print(data)

sumVal = 0
for data in forAry:
  sumVal += data
print('sumVal is ' + str(sumVal))
print('sum of forAry is ' + str(sum(forAry))) # こっちでよい

# Map

# 関数定義、呼び出し

# json読込、json出力

# csv読込、csv出力

# 非同期処理


