import math
'''
def vol(rad):
    result = 4/3*math.pi*rad**3
    return result

print(vol(2))

def run_check(num,low,high):
    return num in range(low,high+1)

print(run_check(6,1,7))

def run_check(num,low,high):
    if num in range(low,high+1):
        print(f"{num} находится между {low} и {high}")
    else:
        print(f"{num} не входит в диапазон")

run_check(1,3,7)

def up_low(s):
    u, l = [], []
    for a in s:
        if a.isupper():
            u.append(a)
        else:
            l.append(a)
    print(len(u), len(l))

b=[]
def unique_list(lst):
    for i in lst:
            if i not in b:
              b.append(i)
    return b

print(unique_list([1,3,5,6,6,8]))

def multi_play(numbers):
    x=1
    for nums in numbers:
        x *= nums
    return x
print(multi_play([2,3,4]))

def palindrome(sss):
    sss=sss.replace(' ','')
    return sss[::1].lower() == sss[::-1].lower()

print(palindrome('ga ag'))

import string

def check_panagrama(str1,alphabet=string.ascii_lowercase):
    alha = set(alphabet)
    bla = set(str1.lower())
    print(alha)
    print(bla)
    return bla <= alha

check_panagrama('sdffdvfhg')
'''
class Circle():
    pi = math.pi

    def __init__(self, radius=1):
        self.radius = radius

    def get_S(self):
        return self.pi*self.radius**2

Circle1 = Circle(10)

print(Circle1.get_S())

class Animal():

    def __init__(self):
        print("Animal created")
    def who(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
class Dog(Animal):

    def __init__(self):

        Animal.__init__(self)
        print("Dog created")

mydog=Dog()

coor1=(3,2)
coor2=(8,10)
class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self):
        return math.sqrt((self.coor2[1]-self.coor1[0])**2+(self.coor2[1]-self.coor1[0])**2)



myline=Line(coor1,coor2)
print(myline.distance())
