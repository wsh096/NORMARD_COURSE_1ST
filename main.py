#1-2course_dictionary

#dictionary{}<-변수들을 하나의 묶음으로 만드는 역할<-{}안에서는 '=' 대신 ':' 사용, 그리고 변수간 구분할때는 ',' 사용
#list[]<-수정가능한 변수들의 sequency들
#tuple()<-수정불가능한 변수들의 sequency

seokhyeon = {
  "name" : "seokhyeon", "age" : 26, "korea" : True, "fav_food" : ["steak","Truple"]
}
print(seokhyeon)
seokhyeon["handsome"] = True
#dictionary는 수정가능한 list와 결합가능
print(seokhyeon)

#1-3_Built in Functions
print(len("asdasdsadasdasflsadfk;zl"))

age = "18"
print(age)
print(type(age))

n_age = int(age)
print(n_age)
print(type(n_age))

#1-4Crrating self Function

#{}괄호로 function을 구분하는 게 아니라 들여쓰기로 구분함 Tab이나 Space통해 구분 가능, True같은 것도 앞을 대문자로 구분하듯이 편리하게 이용 구분되게 잘 표현함
def say_hello():
  print("hello")
  print("bye")
say_hello() #()는 버튼의 역할 :는 이하의 들여쓰는 구간의 함수를 정의해달라는 표시역할

#1-5 Function arguments
#함수가 인자(argument)를 가질 때
def say_hello(who):
  print("hello", who)

say_hello("seokhyeon") #데이터 값에 맞춰야 하며, 빈칸으로는 아무것도 출력 안 해줌

#빈칸을 줄 때는 default 값을 설정해줘라0

def plus(a=0, b=0):
  print(a+b)
def minus(a=0,b=0):
  print(a-b)

plus(2,5)
minus(2,5)

plus(3)
minus(2)#, 2로 b에만 값을 주고 싶었는데 어떻게
minus(int(),2)

#1-7 keyworded arguments

#이제껏 위치에 한정적인 positional argument를 사용해 왔다. 하지만 위치에 제한이 없는  keyworded arguments도 있다. 그걸 배울 거다.

def plus(a,b):
  return a+b
result = plus(b = 30,a = 4)
print(result)

def say_hello(name, age):
  return f"Hello {name} you are {age} years old"
  #f는 format의 f이고 이와 다른 방식으로는 "Hello" + name + "you are" + age + "years old"라고 포맷없이 변수 각각을 각 문장의 구성에 더하는 방식이 존재.

hello= say_hello("seokhyeon","26")
print(hello)

hello_2 = say_hello(age=20,name="seokhyeon")
print(hello_2)

# keyworded argument를 쓰는 이유는 변수가 많아지기 때문이다.

#1-8 code challenge

def calculator(a=1 ,b=1):
  return f"a+b = {a+b} a-b = {a-b} a*b = {a*b} a/b = {a/b} a//b = {a//b} -a = {-a} a%b = {a%b}  a**b = {a**b}"
 
result = calculator(a= int(2), b=int("3"))
print(result)


#1-9Conditionals part One 

#if의 조건문은 if condition:으로 구성, else도 마찬가지로  else:로 구성 :중요
              
def plus (a,b):
  if type(a) and type(b) is int or type(a) and type(b) is float:
    return a + b
  else:
    return 'Wrong'

print(plus(12,"10"))

#1-10 if else and or

def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age == 18 or age ==19:
    print("you are mew to this")
  elif age>20 and age <25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")
  
age_check(19)

#1-11 for in

days = ("Mon","Tue","Wed","Thu","Fri")

for day in days:
  if day == "Wed":
    break
  else:
    print(day)

for name in "seokhyeon":
  print(name)#들여쓰기가 너무 중요한 파이썬

#1-12 Modules
from math import ceil, fsum as seokhyon_sum
  
print(ceil(1.2))
print(seokhyon_sum([1,2,3,4,5,6,7]))
