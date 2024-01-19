#資料:程式的基本單位
#數字
13456
3.5
#字串
"中文、123456"
#布林值
True
False
#有順序、可動的列表 List 中括號
[1,2,3]
["hello","world"]
#有順序、不可動的列表 Tuple 小括號
(1,2,3)
("hello","world")
#集合 Set 無順序 大括號
{1,2,3}
{"hello","world"}
#字典 Dictionary
{"apple":"蘋果","data":"資料"}
#變數:用來儲存資料的自訂名稱
#變數名稱=資料
x=3
print(x)
x=True #取代舊的資料
print(x)
x={1,2,3}
print(x)

#數字運算
#加法
x=1+1
print(x)
#減法
x=2-1
print(x)
#乘法
x=2*2
print(x)
#除法含小數點
x=6/5
print(x)
#除法不含小數點
x=6//5
print(x)
#餘數
x=7%3
print(x)
#次方
x=5**3  #5的3次方
print(x)
x=2**0.5  #0.5次方=根號
print(x)
#變數
x=2+3
print(x)
x+=1  #x=x+1 #x再+1
print(x)
x-=1  #x=x-1 #x再-1
print(x)
x*=1  #x=x*1 #x再*1
print(x)
x/=1  #x=x/1 #x再/1
print(x)
#絕對值
x=-4
print(abs(x))
#四捨五入
x=3.14
print(round(x))
x=3.1415926
print(round(x,2))
#無條件進位
import math
x=9.5
print(math.ceil(x))
#無條件捨去
import math
x=9.5
print(math.floor(x))
#圓周率
import math
print(math.pi)

#字串運算
#跳脫 在"前面加一個\ 使得"符號在字串中被顯示
print("hello \"world")
#字串串聯
x="hello"+"world"  #也能用空白代替+
print(x)
#換行
print("hello\nworld")
print("""hello
world""")
#重複
print("hello"*3+"world")
#字串會對內部字元開始編號(索引)，從0開始算起
x="hello"
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
#指定開頭至指定結尾前一字
x="hello"
print(x[1:4])
#指定開頭至結尾
x="hello"
print(x[1:])
#取至指定結尾前一字
x="hello"
print(x[:4])
#email字串分析
email="s27688473@gmail.com"
index=email.index("@")
print(index)
print(email[:index])
print(email[(index+1):])

#整數
x=(int(455454.3))
print(x)
#浮點數
x=30
print(float(x))
#幾個字元
name="Joseph Joestar"
print(len(name))
#找到第一個空格
name="Joseph Joestar"
x=name.find(" ")
print("第一個空格在第",x,"個字元")
#首字大寫
name="joseph joestar"
x=name.capitalize()
print(x)
#全部大寫
name="joseph joestar"
x=name.upper()
print(x)
#全部小寫
name="JOSEPH JOESTAR"
x=name.lower()
print(x)
#尋找字元或符號出現次數
name="Joseph Joestar"
x=name.count("Jo")
print(x)
#替代
name="Joseph Joestar"
x=name.replace(" ","-")
print(x)

#F-string格式化字串
x=3.321
y=-77
z=15.11
print(f"{x:.2f}\n"  #取到小數點後兩位
      f"{y:.2f}\n"  #沒有小數點自動補上.00
      f"{z:.2f}\n")
#加上正負號
print(f"{x:+.2f}\n"  
      f"{y:+.2f}\n"
      f"{z:+.2f}\n")
#置左、置中、置右
print(f"{x:<10.2f}\n"  #置左10單位
      f"{y:^5.2f}\n"  #置中5單位
      f"{z:>3.2f}\n")  #置右3單位
#混合不同符號
print(f"{x:<+10.2f}\n"  
      f"{y:^+10.2f}\n"
      f"{z:>+10.2f}\n")

#有順序、可動的列表 List 中括號
x=[90,55,87,80,75]
print(x)
#列表中的索引(從0開始算起)
print(x[3])
#更改列表中某個位子的值
x=[90,55,87,80,75]
x[0]=60
print(x)
#指定開頭至指定結尾前一值
x=[90,55,87,80,75]
print(x[1:4])
#刪除指定開頭至指定結尾前一值
x=[90,55,87,80,75]
x[1:4]=[]
print(x)
#列表的串聯
x=[90,55,87,80,75]
x=x+[10,20,30]
print(x)
#求列表長度
x=[90,55,87,80,75]
print(len(x))
#列表中的列表
x=[[3,4,5],[6,7,8]]
print(x[0][0])  #取列表中的第一個列表中的第一個值
#更改列表中的列表
x=[[3,4,5],[6,7,8]]
x[0][0:2]=[1,2,3]
print(x)
#有順序、不可動的列表 Tuple 小括號
x=(90,55,87,80,75) 
#列表的新增或刪除
x=["蘋果","水梨","草莓"]
x=x+["芭樂"]  #新增
print(x)
x=["蘋果","水梨","草莓"]
x.append("芭樂")  #新增的另一種方式
print(x)
x=["蘋果","水梨","草莓","芭樂"]
x.remove("芭樂")  #刪除
print(x)

#集合的運算
#利用in和not in檢驗資料是否在集合中
x={1,2,3,4,5}
print(3 in x)
print(5 not in x)
#交集:取兩個集合中相同的資料
x1={3,4,5}
x2={4,5,6,7}
x3=x1&x2
print(x3)
#聯集:取兩個集合相同的資料，但不重複選取
x1={3,4,5}
x2={4,5,6,7}
x3=x1|x2
print(x3)
#差級:從一個集合減去和另一集合重複的資料
x1={3,4,5}
x2={4,5,6,7}
x3=x1-x2
print(x3)
#反交集:從兩個集合中，取不重複的部分
x1={3,4,5}
x2={4,5,6,7}
x3=x1^x2
print(x3)
#將字串拆解成集合
x=set("Hello")
print("H" in x)
print("A" in x)
#集合的新增及刪減
x={"蘋果","水梨","草莓"}
x.add("芭樂")  #新增
print(x)
x={"蘋果","水梨","草莓","芭樂"}
x.remove("芭樂")  #刪除的第一種(若集合中沒有該元素會出現錯誤)
print(x)
x={"蘋果","水梨","草莓","芭樂"}
x.discard("芭樂")  #刪除的第二種(若集合中沒有該元素也不會出現錯誤)
print(x)
#字典的運算:Key-value 配對
dic={"apple":"蘋果","bug":"蟲"}
print(dic)
print(dic["apple"])
#更改字典內容
dic={"apple":"蘋果","bug":"蟲"}
dic={"apple":"小蘋果"}
print(dic["apple"])
#字典的布林值運算
dic={"apple":"蘋果","bug":"蟲"}
print("apple" in dic)
print("pig" in dic)
#刪除字典中的鍵值對
dic={"apple":"蘋果","bug":"蟲"}
del dic["apple"]
print(dic)
#字典的集合運算
dic={x:x*2 for x in [3,4,5]}
print(dic)

#判斷式:取得字串形式的使用者輸入
x=input("請輸入整數數字:")
x=int(x)  #將字串型態轉換為數字型態(可和input組合成int(input()))
if x>200:
    print(">200")
elif x>100:
    print("101~200")
else:
    print("<100")
#四則運算:==是比較運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
x=input("請輸入運算:+ - * /:")
if x=="+":
    print(n1+n2)
elif x=="-":
    print(n1-n2)
elif x=="*":
    print(n1*n2)
elif x=="/":
    print(n1/n2)
else:
    print("不支援的運算")

#for迴圈 for變數in列表或字串
for x in [3,4,5]:
    print("逐一取得列表中的資料",x)
for x in "Hello":
    print("逐一取得字串中的字元",x)
#range:產生連續字數的寫法
for x in range(5):#相當於for x in [0,1,2,3,4]
    print(x)
for x in range(3,6):#相當於for x in [3,4,5]
    print(x)
#for迴圈連加
sum=0
for x in range(11):
    sum=sum+x
print(sum)  #有縮排的話會紀錄連加結果 沒縮排只顯示結果
#for迴圈鍵值
x={"a":"apple","b":"book","c":"cool"}
for key,value in x.items():
    print("key",key)
    print("value",value)
#while迴圈
x=1
while x<=5:
    print(x)
    x+=1
#while迴圈連加
x=1
sum=0
while x<=5:
    sum=sum+x
    x+=1
    print(sum)  #紀錄累加的結果
#強制結束迴圈
x=1
while x<5:
    if x==3:
        break
    print(x)
    x+=1
print(x)
#強制進行下一次迴圈
n=0
for x in [0,1,2,3]:
    if x%2==0:
        continue
    print(x)
    n+=1
print(n)
#while迴圈的else應用
x=1
while x<5:
    print("變數n的資料:",x)
    x+=1
else:
    print(x)
#for迴圈的else應用
for x in "Hello":
    print("逐一取得字串鍾的字元",x)
else:
    print(x)
#綜合範例:找出整數平方根
x=int(input("請輸入數字: "))
for y in range(x):
     if y**2==x:
         print("整數平方根",y)
         break  #用break強制結束迴圈時，不會執行else
else:
    print("沒有整數平方根")

#自己解
x=int(input("請輸入數字: "))
y=0
while y<x:
    if y**2<x:
        print(y)
        y+=1
    elif y**2==x:
        print("整數平方根",y)
        break
else:
    print("沒有整數平方根")
#練習
#不超過12字元
#不包含空白
#不包含數字
#都OK顯示歡迎+使用者名稱
x=input()
if len(x)>12:
    print("不超過12字元")
elif " " in x:
    print("不包含空白")
elif "1" in x:
    print("不包含數字")
elif "2" in x:
    print("不包含數字")
elif "3" in x:
    print("不包含數字")
elif "4" in x:
    print("不包含數字")
elif "5" in x:
    print("不包含數字")
elif "6" in x:
    print("不包含數字")
elif "7" in x:
    print("不包含數字")
elif "8" in x:
    print("不包含數字")
elif "9" in x:
    print("不包含數字")
elif "0" in x:
    print("不包含數字")
else:
    print("歡迎",x)

#邏輯運算
#and
x=int(input())
if x>0 and x<10:
    print("0<x<10")
else:
    print("error")
#or
x=int(input("0~10:error"))
if x>10 or x<0:
    print("讚")
else:
    print("error")
#not
x=int(input())
if not x>10:
    print("x<=10")
else:
    print("x>10")

#函式:def 函式名稱(參數名稱):
#定義函式:
def sayHello():
    print("Hello")
#呼叫上方定義的函式:
sayHello()
#定義函式:
def say(x):
    print(x)
#呼叫上方定義的函式:
say("Hello Fuction")
say("Hello python")
#定義一個作加法的函式
def add(n1,n2):
    x=n1+n2
    print(x)
#呼叫上方定義的函式:
add(3,4)
add(7,8)
#回傳值:結束函式 回傳none
def say(x):
    print(x)
    return
#呼叫函式取得回傳值:
value=say("Hello Fuction")
print(value)
#函式回傳字串Hello
def add(n1,n2):
    x=n1+n2
    return x
#呼叫函式，取得回傳值
value=add(3,4)
print(value) 
#定義一個作乘法的函式
def multiply(n1,n2):
    print(n1*n2)
#呼叫上方定義的函式:
vaule=multiply(n1,n2)
print(value)
#利用return的好處:
def multiply(n1,n2):
    return n1*n2
#呼叫上方定義的函式:
vaule=multiply(3,4)+multiply(5,6)   #(3*4)+(5*6)
print(value)
#程式的包裝
def calculate(n):
    sum=0
    for x in range(n+1):
        sum=sum+x
    print(sum) 
calculate(10)
calculate(20)
#函式參數的預設資料
def say(x="Hello"):
    print(x)
say()  #印出預設資料Hello
say("Hello Fuction")  #印出Hello Fuction
#函式的無限參數:def 函式名稱(*無限參數):  
def say(*x):   #參數以Tuple形式呈現
    for y in x:
        print(y)
say("Hello","Hi","Hey")
def n(*x):
    sum=0
    for y in x:
        sum=sum+y
    print(sum/len(x))
n(3,4)
n(3,5,10)
n(-1,-5,8,4)
#參數的預設資料設定
def power(x,y=0):
    print(x**y)
power(3,2)  #3**2=9
power(4)  #4**0=1(未設定參數的情況下使用預設資料)
#參數的名稱對應
def n(n1,n2):
    print(n1/n2)
n(2,4)  #2/4=0.5
n(n2=2,n1=4)  #4/2=2(可透過註明=來交換前後位子)

#模組基本語法:import 模組名稱、import 模組名稱 模組別名
#sys模組:取得系統相關資訊
import sys  #載入sys模組
print(sys.platform)  #印出作業系統
print(sys.maxsize)  #印出整數型態最大數
print(sys.path)  #系出搜尋模組的路徑
#利用別名
import sys as s  
print(s.platform)  
#自訂模組:幾何運算
import geometry
x=geometry.distance(1,1,5,5)
print(x)

#檢測檔案是否存在
import os
str=r"C:\Users\s2768\Desktop\大蛇.jpg"
print(str)
if os.path.exists(str):
    print("路徑存在")
else:
    print("路徑不存在")
if os.path.isfile(str):
    print("該路徑為檔案")
elif os.path.isdir(str):
    print("該路徑為目錄")
else:
    print("其他")
#讀取檔案
str=r"C:\Users\s2768\Desktop\臨時密碼.txt"
with open(str,encoding="utf-8") as file:
    print(file.read())

#封包:整理、分類模組
# - 專案資料夾
#    - 主程式.py
#    - 封包資料夾
#      - __init__.py
#      - 模組一.py
#      - 模組二.py

#儲存檔案
file=open("data.txt",mode="w")  #開啟
file.write("Hello World\nHello Python")  #操作(\n:換行)
file.close()  #關閉
#開啟中文編碼
file=open("data.txt",mode="w",encoding="utf-8")  
file.write("中文")  
file.close()  
#最佳實務寫法(自動安全關閉)
with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("中文\n好棒棒")
#檔案讀取
with open("data.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
print(data)
#把檔案中的數字資料，一行一行的讀取出來，並計算總合
with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3")
sum=0
with open("data.txt",mode="r",encoding="utf-8") as file:
    for line in file:  #一行一行的讀取
        sum+=int(line)
print(sum)
#使用JSON格式讀取、複寫檔案
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data)
print("name", data["name"])
print("version", data["version"])
data["name"]="New name" #修改變數中的資料
#把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)

#亂數模組
#從列表隨機選取一個資料
import random
x=random.choice([0,1,2,5,8,9])
print(x)
#從列表隨機選取兩個資料
import random
x=random.sample([0,1,2,5,8,9],2)
print(x)
#將列表的資料隨機「就地」調換
x=[0,1,9,8,5]
random.shuffle(x)
print(x)
#隨機亂數 
import random
x=random.randint(1,100) #取任意兩數之間的隨機整數 
print(x)
import random
x=random.random()  #取得0.0~1.0之間的隨機亂數
print(x)
import random
x=random.uniform(60,100) #取任意兩數之間的隨機亂數 
print(x)
#常態分配亂數
import random
x=random.normalvariate(100,10)  #取平均值100,標準差10的常態分配亂數
print(x)
#系統隨機生成1~100的隨機整數，若猜錯會顯示數字太大或太小，猜對會顯示猜幾次
import random
x=random.randint(1,100)
y=0

while True:
    z=int(input("請猜一個介於1~100的數:"))
    y+=1
    if z<x:
        print("猜的數字太小了")
    elif z>x:
        print("猜的數字太大了")
    else:
        print("恭喜你猜對了，總共猜了:",y,"次")
        break
#猜拳遊戲
import random
x=random.choice(["剪刀","石頭","布"])
z=["剪刀","石頭","布"]
y=input("請輸入剪刀、石頭、布:")
if y in z:
    if x == "剪刀" and y == "剪刀":
        print("平手，電腦出的是",x)
    elif x == "石頭" and y == "石頭":
        print("平手，電腦出的是",x)
    elif x == "布" and y == "布":
        print("平手，電腦出的是",x)
    elif x == "剪刀" and y == "石頭":
        print("勝利，電腦出的是",x)
    elif x == "布" and y == "剪刀":
        print("勝利，電腦出的是",x)
    elif x == "石頭" and y == "布":
        print("勝利，電腦出的是",x)
    elif x == "剪刀" and y == "布":
        print("敗北，電腦出的是",x)
    elif x == "石頭" and y == "剪刀":
        print("敗北，電腦出的是",x)
    elif x == "布" and y == "石頭":
        print("敗北，電腦出的是",x)
    else:
        print("蝦?你突破系統限制")
else:
    print("輸入錯誤")

#統計模組
#計算列表中數字的平均數
import statistics
x=statistics.mean([1,4,9,6])
print(x)
#計算列表中數字的中位數
import statistics
x=statistics.median([1,4,9,6])
print(x)
#計算列表中數字的標準差
import statistics
x=statistics.stdev([1,4,9,6])
print(x)

#下載特定網址資料
import urllib.request as request  #載入網路模組
with request.urlopen("https://www.google.com.tw/?hl=zh_TW") as response:
    data=response.read().decode("utf-8")
print(data)
#串接、擷取公開資料
import urllib.request as request
import json  #載入json模組
with request.urlopen("https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire") as response:
    data=json.load(response) #利用json模組處理json資料格式
print(data)
#將資料列表出來
x=data["result"]["results"]  #從資料得知result、results組成列表
for company in x:
    print(company["公司名稱"])  #利用字典的功能，將公司名稱對應的公司透過迴圈列出
#將資料寫入檔案
x=data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in x:
        file.write(company["公司名稱"]+"\n")

#封裝變數或函數
class Test:  #名稱首字大寫
    x=3  #定義變數
    def say():  #定義函式
        print("Hello")
#使用Test類別
print(Test.x+3)  #取得屬性x的資料3
Test.say()  #呼叫屬性say函式
#定義類別與類別屬性(封裝在類別中的變數和函式)
class Io:  #定義一個類別Io，有兩個屬性x、read
    x=["data","file"]  
    def read(y):
        if y not in Io.x:
            print("Not Supported")
        else:
            print("Read from",y)
print(Io.x) #使用類別
Io.read("data")
Io.read("file")
#自我練習
class Io:
    x=["data","file"]
    dic={"apple":"蘋果","data":"資料"}
    def read(y):
        if y not in Io.x:
            print("Not Supported")
        elif y in Io.dic:
            print("Read from",Io.dic[y])
        else:
            print("Read from", y)
print(Io.x)
Io.read("data")
Io.read("file")
Io.read("Internet")

 #定義實體物件
class Point:
    def __init__(self):  #建立初始化的函式
        self.x=3
        self.y=4
#建立實體物件
p1=Point()  #此物件包含x、y兩個實體屬性
print(p1.x,p1.y)
p2=Point()  #可建立第二個實體物件
print(p2.x,p2.y)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=Point(3,4)  #建立實體物件時可以直接傳入參數資料
print(p1.x,p1.y)
p2=Point(5,6)  
print(p2.x,p2.y)
#FullName 實體物件的設計:分開紀錄姓、名資料的全名
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=FullName("C.W","Peng")
print(name1.first,name1.last)
name2=FullName("T.Y","Ling")
print(name2.first,name2.last)
#實體方法:封裝在實體物件的函式
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def distance(self,targetX,targetY):
        return(((self.targetX)**2)+((self.y-targetY)**2))**0.5
p=Point(3,4)
p.show()
z=p.distance(0,0)
print(z)
#File實體物件的設計:包裝檔案讀取的程式
class File:
    #初始化函式
    def __init__(x,name):
        x.name=name
        x.file=None  #尚未開啟檔案:初期是None
    #實體方法
    def open(x):
        x.file=open(x.name,mode="r",encoding="utf-8")
    def read(x):
        return x.file.read()
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)

#抓取網站原始碼
import urllib.request  as req
url="https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url,headers={  #建立一個Request物件，附加Headers的資訊
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
#解析程式碼
import bs4
root=bs4.BeautifulSoup(data, "html.parser")  #讓BeautifulSoup解析html格式文件
titles=root.find_all("div",class_="title")  #尋找所有class="title"的div標籤
for title in titles:
    if title.a != None:  #如果標題包含a標籤，印出來
        print(title.a.string)
#抓取多頁ptt八卦版的原始碼
import urllib.request  as req
def getdata(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Cookie":"over18=1"  #抓cookie資料
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div",class_="title")  
    for title in titles:
        if title.a != None:  
            print(title.a.string)
    nextLink=root.find("a",string="‹ 上頁")  #抓取上一頁連結，找到內文是"‹ 上頁"的a標籤
    return nextLink["href"]
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"  #抓取一個頁面的標題
count=0
while count<3:
    pageurl="https://www.ptt.cc"+getdata(pageurl)
    count+=1
print(pageurl)

#爬ptt內文
import requests
import bs4
import os
def download(url,save_path):  #定義下載圖片函式
    print("正在下載圖片:",url)
    resqonse=requests.get(url)  #發起網絡請求，獲取圖片的二進制內容
    with open(save_path,"wb") as file:  #寫入圖片的二進制內容到文件
        file.write(resqonse.content)
    print("-"*30)  #分隔線
def main():  #主程式
    url="https://www.ptt.cc/bbs/Beauty/M.1698322162.A.AEA.html"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "cookie":"over18=1"
    }
    response=requests.get(url,headers=headers)  #發起請求，獲取網頁內容
    with open("data.html","w",encoding="utf-8") as f:  #寫入網頁內容到 data.html 文件
        f.write(response.text)  
    soup=bs4.BeautifulSoup(response.text,"html.parser")  #使用 Beautiful Soup 解析網頁內容
    #尋找標題
    spans=soup.find_all("span",class_="article-meta-value")
    print(spans[2].text)
    print("-"*30)
    #創建資料夾
    title=spans[2].text   #輸出第三個span標籤的文字內容
    dir_name=f"image/{title}"  #資料夾名稱是文章標題
    if not os.path.exists(dir_name):  #如果資料夾不存在，建立資料夾；如果存在則跳過
        os.makedirs(dir_name)
    
    #爬網頁中的圖片
    links=soup.find_all("a")  #找出所有的超連結標籤
    allow=["jpg","jpeg","png","gif"]  #允許的副檔名
    x=[]
    for img in links:  
        if img.find_parent(class_="push"):  #將父級元素帶有"push"的連結找出，這代表該連結來自於留言
            x.append(img.text)
    for link in links:
        href=link.get("href")  #取得連結
        if not href:  #如果不是連結就跳過
            continue
        if href in x:  #如果網址來自於留言，則跳過
            continue
        file_name=href.split("/")[-1]  #將網址中/後面的字串定義為名稱
        exception=href.split(".")[-1].lower()  #利用網址中.後面的字串分析出要的副檔名
        if exception in allow:
            print("url:",href)
            print("副檔名:",exception)
            download(href,f"{dir_name}/{file_name}")  #下載圖片並保存到指定目錄
if __name__=="__main__":  #如果主程式執行
    main()  #執行主程式
print("下載完畢")

#抓取AJAX格式網站的資料
import urllib.request  as req
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=8992d7961e95a58a99d55aec457593b2"
#建立一個Request物件，附加Headers的資訊
request=req.Request(url,headers={  
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Cookie":"KKUD=85d53795d6812e621f02db205091c1b3; _fw_crm_v=35740ae1-bd2d-4316-a90b-5e3a33432e4d; csrf_cookie_name=8992d7961e95a58a99d55aec457593b2; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22332535daec6b41a0e949a18886ac3bba%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1695823722%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D46e2b53f2b2e1b68d232b6348c642bb4; country_lang=zh-tw; currency=TWD",
    "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,ja;q=0.5",
    "Accept":"application/json, text/javascript, */*; q=0.0",
    "Sec-Fetch-Dest":"empty",
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")  #根據觀察，取得的資料是Json格式
#解析Json格式的資料
import json
data=json.loads(data)  #把原始的Json資料解析成字典表示形式
#取得Json資料中的文章標題
posts=data["data"]["homepage_product_group"]  
for key in posts:
    print(key["title"])
#抓取Medium.com的文章資料，加入Request Data的概念
import urllib.request as req
import json
#建立連線網址
url="https://medium.com/_/graphql"
#建立一個Request物件，附上Request Headers和Request Data的資訊
requestData={"operationName":"CuratedHomeFeedModuleQuery","variables":{"paging":{"from":"10","limit":10}},"query":"query CuratedHomeFeedModuleQuery($paging: PagingOptions!) {\n  staffPicksFeed(input: {paging: $paging}) {\n    items {\n      ...CuratedHomeFeedItems_homeFeedItems\n      __typename\n    }\n    pagingInfo {\n      next {\n        page\n        limit\n        from\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CuratedHomeFeedItems_homeFeedItems on HomeFeedItem {\n  __typename\n  post {\n    id\n    title\n    ...HomeFeedItem_post\n    __typename\n  }\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...OverflowMenuButtonWithNegativeSignal_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n  ...Star_post\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n  normalizedTagSlug\n}\n\nfragment BookmarkButton_post on Post {\n  visibility\n  ...SusiClickable_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  isPublished\n  __typename\n}\n\nfragment OverflowMenuButtonWithNegativeSignal_post on Post {\n  id\n  visibility\n  ...OverflowMenuWithNegativeSignal_post\n  __typename\n}\n\nfragment OverflowMenuWithNegativeSignal_post on Post {\n  id\n  creator {\n    id\n    __typename\n  }\n  collection {\n    id\n    __typename\n  }\n  ...OverflowMenuItemUndoClaps_post\n  ...AddToCatalogBase_post\n  __typename\n}\n\nfragment OverflowMenuItemUndoClaps_post on Post {\n  id\n  clapCount\n  ...ClapMutation_post\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  __typename\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    ...useIsVerifiedBookAuthor_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  membership {\n    tier\n    __typename\n    id\n  }\n  name\n  username\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n\nfragment useIsVerifiedBookAuthor_user on User {\n  verifications {\n    isBookAuthor\n    __typename\n  }\n  __typename\n  id\n}\n\nfragment Star_post on Post {\n  id\n  creator {\n    id\n    __typename\n  }\n  __typename\n}\n"}
request=req.Request(url,headers={
    "Content-Type":"application/json; charset=utf-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
},data=json.dumps(requestData).encode("utf-8"))
#發出請求
with req.urlopen(request) as response:
    result=response.read().decode("utf-8")
result=json.loads(result)
titles=(result["data"]["staffPicksFeed"]["items"])
for title in titles:
    print(title["post"]["title"])

#架設Flask網站
from flask import Flask
app=Flask(__name__)  #__name_代表目前執行的模組

@app.route("/")  #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def home():
    return "Hello Flask"

@app.route("/test")
def test():
    return "Hello Flask test"

if __name__=="__main__":  #如果主程式執行
    app.run()  #立刻啟動伺服器

#Pandas資料分析
import pandas as pd  #建立Series
#以列表資料為底建立，Series
pd.Series  #Series為列表
#使用Series
import pandas as pd
data=pd.Series([20,10,15])
print(data)
print(data[1])  #根據順序取值，以0為開頭
data=data*2  #放大兩倍
print(data)
data=data==20  #將資料和20做比較得出是否相等，並顯示true or false
print(data)
print(data.size)  #顯示資料數量
print(data.dtype)  #顯示資料型態
#建立DataFrame
import pandas as pd  #建立Pandas模組
#以字典資料為底，建立DataFrame
pd.DataFrame  #DataFrame為字典
#取得特定欄(直向))
import pandas as pd
data=pd.DataFrame({
    "name":["Amy","john","Bob"],
    "money":[30000,35000,40000]
})
print(data)
print(data["money"])
print(data["name"])
#取得特定列(恆謝))
import pandas as pd
data=pd.DataFrame({
    "name":["Amy","john","Bob"],
    "money":[30000,35000,40000]
})
print(data.iloc[0])  #列編號按順序由0開始
#自訂索引
import pandas as pd
data=pd.Series([20,10,15],index=[1,2,3])  #index是索引列表
print(data)
print(data[2])
data=pd.Series([1,5,20,10,15],index=["a","b","c","d","e"])
print(data) 
print(data.index)  #印出索引
print(data["c"])
#數字運算
import pandas as pd
data=pd.Series([3,10,20,5,-12])
print(data.sum(),data.max(),data.prod())  #1.加法總和 2.找最大值 3.乘法總和
print(data.mean(),data.median(),data.std())  #1.平均數 2.中位數 3.標準差
print(data.nlargest(3))  #前(3)大
print(data.nsmallest(2))   #前(2)小
#字串操作
import pandas as pd
data=pd.Series(["請","謝謝","對不起","您好","Python"])
print(data.str.lower(),data.str.upper(),data.str.len())  #1.所有字串變小寫 2.所有字串變大寫  3.算出所有字串的長度
print(data.str.cat(sep=","),data.str.contains("P"))  #1.所有字串用","串在一起 2.判斷字串是否有"大寫P"
print(data.str.replace("您好","Hello"))  #將每個字串的您好取代成Hello
#觀察資料
import pandas as pd
data=pd.DataFrame  ({
    "name":["Amy","john","Bob"],
    "money":[30000,35000,40000]
    },index=["a","b","c"])
print(data)
print("資料數量",data.size)
print("資料形狀(欄,列)",data.shape)
print("資料索引",data.index)
#取得列(橫向)的Series資料
print("取得第二列",data.iloc[1],sep="\n")  #照順序
print("取得第C列",data.loc["c"],sep="\n")  #照索引
#建立新欄位
data["revenue"]=[500000,400000,300000]
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])
data["cp值"]=data["revenue"]/data["money"]
print(data)
#Pandas資料篩選
import pandas as pd
data=pd.Series([30,15,20])
condition=[True,False,True]
newdata=data[condition]
print(newdata)

condition=data>20
newdata=data[condition]
print(newdata)

import pandas as pd
data=pd.Series(["您好","Python","Pandas"])
condition=[True,False,True]
newdata=data[condition]
print(newdata)

condition=data.str.contains("P")
print(condition)

newdata=data[condition]
print(newdata)
#DataFrame資料篩選
import pandas as pd
data=pd.DataFrame  ({
    "name":["Amy","john","Bob"],
    "money":[30000,35000,40000]
})
print(data)
condition=[False,True,True]
newdata=data[condition]
print(newdata)

condition=data["money"]>30000
newdata=data[condition]
print(newdata)

condition=data["name"]=="Amy"
newdata=data[condition]
print(newdata)
#讀取資料
import pandas as pd
data=pd.read_csv("googleplaystore.csv")  #把scv格式讀取成DataFrame
#觀察資料
print("資料數量",data.shape)
print("資料欄位",data.columns)
#分析資料
print("平均數",data["Rating"].mean())
print("中位數",data["Rating"].median())
print("前100個應用程式的平均數",data["Rating"].nlargest(100).mean())
condition=data["Rating"]>5
newdata=data[condition]
print(newdata)
#分析資料並排除異常:評分大於5
condition=data["Rating"]<=5  #將評分大於5的成績不列於統計內
newdata=data[condition]
print(newdata)
print("平均數",newdata["Rating"].mean())
print("中位數",newdata["Rating"].median())
print("前100個應用程式的平均數",newdata["Rating"].nlargest(100).mean())
#分析資料並排除異常:下載數量顯示為字串，無法進行計算
import pandas as pd
data=pd.read_csv("googleplaystore.csv")
data["Installs"]=data["Installs"].str.replace("[,+Free]","",regex=True)  #將字串中的,、+、Free用無取代掉
data["Installs"]=pd.to_numeric(data["Installs"])  #將字串轉為數字
newdata=data["Installs"]
print(newdata)
print("平均數",newdata.mean())
condition=data["Installs"]>100000
print("安裝數量大於100000的應用程式有",data[condition].shape[0],"個")
#利用關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword,case=False)  #忽略大小寫
print("遊戲區內搜尋結果如下:",data[condition]["App"])

#發送電子郵件
import email.message  #載入寄件模組
msg=email.message.EmailMessage()
msg["From"]='寄件人信箱'
msg["To"]='收件人信箱'
msg["Subject"]='測試測試'
#寄送純文字內容
msg.set_content("你好")
#利用HTML格式寄送多樣式內容
msg.add_alternative("<h3>測試</h3>測試測試",subtype="html")
#連線至SMTP伺服器
import smtplib  #載入smtp模組
sever=smtplib.SMTP_SSL("smtp.gmail.com",465)  #連線到Gmail的SMTP伺服器
sever.login("寄件人帳號","密碼")
sever.send_message(msg)
sever.close()

#Iterable可疊代的資料型態
#字串、列表、集合、字典
#for迴圈:for 變數名稱 in 可疊代資料:
for x in "abc":  #字串
    print(x)
for x in [1,2,3]:  #列表list
    print(x)
for x in (4,5,6):  #列表Taple
    print(x)
for x in {7,8,9}:  #集合
    print(x)
dic={"3":"three",5:"five",2:"two"}  #字典
for x in dic:
    print(dic[x])
#內建函式:max(可疊代資料)
x=max([10,50,8,9,44])  #取最大的數字
print(x)
x=max("a,g,z")  #取最大的英文字(最後一位)
print(x)
#內建函式:sorted(可疊代資料)
x=sorted([10,50,8,9,44])  #改成由小到大排序
print(x)
x=sorted(("zgbxa"))  #照字母順序排序
print(x)

#生成器
def x():
    number=0
    while number<=10000:
        yield number
        number+=2
y=x()
for z in y:
    print(z)

#回呼函式
def x(y):
    y()
def z():
    print(100)
x(z)
def x(y):
    y("Hello")
def z(a):
    print(a)
x(z)
def add(n1,n2,x):
    x(n1+n2)
def y(z):
    print("結果是:",z)
def y2(z):
    print("答案:",z)
add(3,4,y)
add(5,6,y2)

#裝飾器
def x(y):  #定義裝飾器
    def z():
        print("裝飾器")
        y(3)  #回呼函式
    return z
@x  #帶有裝飾器的函式
def a(data):
    print("普通函式",data)
a()  #先執行裝飾器內部程式碼，在透過回呼函式，執行普通函式

def x(y):
    def z():
        num=0
        for n in range(51):
            num=num+n
        y(num)
    return z
@x
def a(num):
    print("計算結果:",num)
a()
@x
def english(num):
    print("result:",num)
english()
#裝飾器工廠
def xyz(qwe):
    def x(y):
        def z():
            print("裝飾器內的值:",qwe)
            num=qwe*5
            y(num)
        return z
    return x
@xyz(10)
def a(num):
    print("函式的值:",num)
a()

def xyz(qwe):
    def x(y):
        def z():
            num=0
            for n in range(qwe+1):
                num=num+n
            y(num)
        return z
    return x
input=int(input("請輸入數字: "))
@xyz(qwe=input)
def a(num):
    print("1 加到",(input),"的計算結果:",num)
a()
#錯誤和例外處理
#語法錯誤:syntax Error
#例外:Exception
data=input("請輸入數字:" )
try:  #當出現以下情況以外的例外
    num=int(data)
except Exception:  #則以以下情況繼續
    num=0
num=num*2
print(num)

while True:
    data=input("請輸入數字:" )
    try:  #當出現以下情況以外的例外
        num=int(data)
        break
    except Exception:  #則以以下情況輸出
        print("錯誤")
num=num*2
print(num)

#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定Chrome Driver的執行檔路徑
options=Options()
options.Chrome_executable_path="G:\Microsoft VS Code\Python traning\chromedriver.exe"
#建立Driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
driver.get("https://www.gamer.com.tw/index2.php?ad=N")
driver.save_screenshot()
driver.close()
#Selenium網路爬蟲
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.Chrome_executable_path="G:\Microsoft VS Code\Python traning\chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://www.ptt.cc/bbs/Stock/index6618.html")  #連線到PTT股票版
print(driver.page_source)  #取得網頁原始碼
tags=driver.find_elements(By.CLASS_NAME,"title")  #搜尋class屬性是title的所有標籤
for tag in tags:  #取得標題，並利用迴圈逐一印出
    print(tag.text)
link=driver.find_element(By.LINK_TEXT,"‹ 上頁")#取得上一頁的文章標題
link.click()  #模擬使用者的點擊
tags=driver.find_elements(By.CLASS_NAME,"title")  #搜尋class屬性是title的所有標籤
for tag in tags:  #取得標題，並利用迴圈逐一印出
    print(tag.text)
driver.close()

#Selenium捲動視窗
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.Chrome_executable_path="G:\Microsoft VS Code\Python traning\chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search?keywords=&location=%E5%8F%B0%E7%81%A3%20%E8%87%BA%E5%8C%97%E5%B8%82%20%E5%8F%B0%E5%8C%97&geoId=106907071&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
n=0
while n<3:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #捲動視窗至底部
    time.sleep(3)  #等待5秒鐘(等待載入更多內容)
    n+=1
titleTags=driver.find_elements(By.CLASS_NAME,"base-search-card__title")
for titleTag in titleTags:
    print(titleTag.text)
driver.close()

#Selenium登入帳戶
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
options=Options()
options.Chrome_executable_path="G:\Microsoft VS Code\Python traning\chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://leetcode.com/accounts/login/")  #登入某刷題網站
username=driver.find_element(By.ID,"id_login")  #輸入帳號
username.send_keys("***")
password=driver.find_element(By.ID,"id_password")  #輸入密碼
password.send_keys("***")
signin=driver.find_element(By.ID,"signin_btn")  #點擊登入
signin.send_keys(Keys.ENTER)
time.sleep(5)  #等待讀取
driver.get("https://leetcode.com/problemset/all/")  #進入另一個網頁
time.sleep(5)
data=driver.find_element(By.CSS_SELECTOR,"[data-difficulty=TOTAL]")  #爬取資料
print(data.text)
x=data.text.split("\n")  #利用換行符號，只顯示自己要的資料
print("已刷題數量",x[1])
driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
options=Options()
options.Chrome_executable_path="G:\Microsoft VS Code\Python traning\chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://user.gamer.com.tw/login.php")  #以巴哈為例
username=driver.find_element(By.CSS_SELECTOR,"[placeholder=帳號或手機]")
username.send_keys("***")
password=driver.find_element(By.CSS_SELECTOR,"[placeholder=密碼]")
password.send_keys("***")
time.sleep(3)
recaptcha=driver.find_element(By.CSS_SELECTOR,"[data-callback=recaptchaPass]")
recaptcha.click()  #點擊"我不是機器人"(如果要圖片驗證就沒辦法)
time.sleep(10)
signin=driver.find_element(By.ID,"btn-login")
signin.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()

#寫入CSV格式的檔案
import csv
with open("data.csv",mode="w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow([1,2,3])
    writer.writerow([4,5,6])
    writer.writerow([7,8,9])
#讀取CSV格式的檔案
import csv
with open("data.csv",mode="r",newline="") as file:
    reader=csv.reader(file)
    for row in reader:  #逐列讀取檔案
        print(row)

#Matplotlib資料視覺化
import matplotlib.pyplot as plt
plt.plot([2,3,4],[4,6,8])  #(2,4)、(3,6)、(4,8)的線
plt.plot([2,3,4],[2,3,4])  #(2,2)、(3,3)、(4,4)的線
plt.show()

plt.plot([2,3,4],[[4,2],[6,3],[8,4]])  #效果同第一種
plt.show()
#讀取CSV格式的資料並畫出圖表
import csv
file=open("data.csv",encoding="utf-8")
reader=csv.reader(file)
header=next(reader)  #跳過標題行
print("標頭",header)
x=[]  #預期[2012,2013,2014]
y=[]  #預期[[50000,65000],[48000,49000],[58000,59000]]
import matplotlib.pyplot as plt
plt.rc("font",family="DFKai-SB")  #微軟正黑體：Microsoft JhengHei、標楷體：DFKai-SB...等
for row in reader:
    print("每列的資料",row)
    x.append(int(row[0])),
    y.append([int(row[1]),int(row[2])])
plt.plot(x,y, label=header[1:3])  #取標頭的第二筆~第三筆
plt.legend()  #額外顯示圖例
plt.xlabel(header[0])  #X座標的標題  #取標頭的第一筆  
plt.ylabel("薪資")  #Y座標的標題
plt.show()

#利用Matplotlib畫出圓餅圖
import matplotlib.pyplot as plt
plt.rc("font",family="DFKai-SB")
x=[20,30,50]
total=sum(x)
labels=[str(100*data/total)+"%" for data in x]  #利用迴圈算出各資料的占比
plt.pie(
    x,
    labels=labels,
    labeldistance=0.5  #標籤的位子，0代表圓心，1代表圓周，大於1代表圓之外
)
plt.legend()
plt.show()
#讀取CSV格式的資料並畫出圓餅圖
import matplotlib.pyplot as plt
plt.rc("font",family="DFKai-SB") 
import csv
file=open("data2.csv",encoding="utf-8")
reader=csv.reader(file)
next(reader)
x=[]  
labels=[]
for row in reader:
    labels.append(row[0])
    x.append(int(row[1]))
total=sum(x)
percent=[str(100*data/total)+"%" for data in x]
y=[f"{a} {b}" for a,b in zip(labels, percent)]
plt.pie(x,labels=y,labeldistance=0.5)
plt.legend(loc="upper left")  #更改圖例位子，有 upper left, upper right, lower left, lower right這四種
plt.show()

#利用Matplotlib畫出點座標
import matplotlib.pyplot as plt
plt.rc("font",family="DFKai-SB") 
plt.scatter([2,4,3],[4,3,6],c="blue",s=1000,label="標籤一")  #c=顏色(也可以用色碼)，S=大小
plt.scatter([1,3,4],[2,5,6],c="red",s=100,label="標籤二") 
plt.legend()
plt.show()
#讀取CSV格式的資料並畫出點座標
import matplotlib.pyplot as plt
plt.rc("font",family="DFKai-SB") 
import csv
file=open("data3.csv",encoding="utf-8")
reader=csv.reader(file)
next(reader)
data={
    "男":{"x":[],"y":[]},
    "女":{"x":[],"y":[]}
}
for row in reader:
    gender=row[0]
    data[gender]["x"].append(int(row[1]))
    data[gender]["y"].append(int(row[2]))
#也可以這樣寫:
#for row in reader:  
    #if row[0] == "男":
        #data["男"]["x"].append(int(row[1]))
        #data["男"]["y"].append(int(row[2]))
    #else:
        #data["女"]["x"].append(int(row[1]))
        #data["女"]["y"].append(int(row[2]))
plt.scatter(data["男"]["x"],data["男"]["y"],c="blue",label="男生")
plt.scatter(data["女"]["x"],data["女"]["y"],c="red",label="女生")
plt.legend()
plt.show()

