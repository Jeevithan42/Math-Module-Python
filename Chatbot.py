import math
import random
from random import randint
output = 0
mult1 = 0
mult2 = 0
intersect1 = 0
list_of_multiples1 = []
list_of_multiples2 = []
l2 = []
denooom = 0
answer = []
product = 1
abso = 0

Option = input("What would you like to do today?\nLCM - LCM\nrandom order - RO\nGCF - GCF\nFraction calculator - FC\nFactorial - FAC\nVolume and Surface area calculator - volsa\nForce, Mass, Acceleration - FMA\nVector - vector\nFloatability - cf\nPythagorean Theorem - pythag\nDensity - Den\n")

def LCM (x,y):
  global mult1
  global mult2
  global denooom 
  global intersect1
  n = 1
  list_of_multiples1.clear()
  list_of_multiples2.clear()
  temp = 0
  if x > y :
    temp = x
  else:
    temp = y
  for i in range (int(temp)):
    list_of_multiples1.append(int(x)*n)
    
    list_of_multiples2.append(int(y)*n)
    
    n = n+1
  # print(l1)
  # print(l2)
  set1 = set(list_of_multiples1)
  intersect = list(set1.intersection(list_of_multiples2))
  intersect1 = min(intersect)
  denooom = intersect1
  
  # print(denooom)
  # easy class
  # print(intersect)
  mult1 = denooom/int(x)
  #print(mult1)
  mult2 = denooom/int(y)

def RO(inn):
    input = inn.split(',')
    global l2 
    l2 = []
  
    for i in range (len(input)):
      n = random.randint(0,(len(input)-1))
      l2.append(input[n])
      input.remove(input[n])
    input = l2
    print(l2)

def GCF(num1, num2):
    global output
    num1list = []
    num2list = []
    if num1 > num2:
      for i in range(1, num1):
        temp1 = num1 / i
        if temp1 == int(temp1):
          num1list.append(i)
        temp2 = num2 / i
        if temp2 == int(temp2):
          num2list.append(i)
        i += 1
    else:
      for i in range(1, num2):
        temp1 = num1 / i
        if temp1 == int(temp1):
          num1list.append(i)
        temp2 = num2 / i 
        if temp2 == int(temp2):
          num2list.append(i)
        i += 1
    set1 = set(num1list)
    intersect = list(set1.intersection(num2list))
    gcf = intersect[len(intersect) - 1]
    output = gcf
    print(output)

def FC(input):
    n = 0
    global answer
    
    
    
   
    input1 = input.split(' ')
    

    for i in range (0, int((len(input1)-1)/2)):
        
        frac1 = input1[n].split('/')
        
        frac2 = input1[n+2].split('/')
        
        if input1[n+1] == 'x':
            numerator = int(frac1[0]) * int(frac2[0])
            denominator = int(frac1[1]) * int(frac2[1])
            
        
        if input1[n+1] == '/':
            numerator = int(frac1[0]) * int(frac2[1])
            denominator = int(frac1[1]) * int(frac2[0])
        
        if input1[n+1] == '+':
            LCM(frac1[1],frac2[1])
            numerator = (int(frac1[0]) * mult1) + (int(frac2[0]) * mult2)
            denominator = intersect1
            
        if input1[n+1] == '-':
            LCM(frac1[1],frac2[1])
            numerator = (int(frac1[0]) * mult1) - (int(frac2[0]) * mult2)
            denominator = intersect1
        
        input1.remove(input1[0])
        input1.remove(input1[0])
        input1.remove(input1[0])
        
        input1.insert(0, str(int(numerator)) + '/' + str(denominator))
        
    answer.append(input1)
    print(answer)
        
        
def FAC(x):
    n = 0
    global product
    product = 1
    for i in range (1 , int(x)):
        product =+ product * (x - n)

        
        n = n+1
    print(product)

#CP broken
def volsa():   
      
  temp2 = input(("\n\nThis is the Volume/S.A Calculator our options are:\nRectanglular Prism(RP)\nCylinder(CYL)\nCube(CUBE)\nTriangular Prism(TP)\nCustom Prism(CP requires side length and height)\nSphere(SPH)\nPlease Select One"))
  if temp2 == "RP":
    print("\nRectangular Prism, SA or Volume(V)")
    temp3 = input()
    if temp3 == "SA":
      print("Please input L W H")
      dimensions = input().split(" ")
      LA = (2 * int(dimensions[0]) + 2 * int(dimensions[1])) * int(dimensions[2])
      A = int(dimensions[0]) * int(dimensions[1])
      Answer =  LA + 2 * A
      print(str(Answer))
    if temp3 == "V":
      print("Please input L W H")
      dimensions = input().split(" ")
      A = int(dimensions[0]) * int(dimensions[1])
      Answer =  A * int(dimensions[2])
      print(Answer)
  if temp2 == "CYL":
    print("\nCylinder, SA or Volume(V)")
    temp3 = input()
    if temp3 == "SA":
      print("Please input R H")
      dimensions = input().split(" ")
      LA = int(dimensions[0]) * 2 * int(dimensions[1])
      A = int(dimensions[0]) * int(dimensions[0])
      Answer = (float(LA) + float(A) * float(2)) * 3.141592653589793238462643383279
      print(str(Answer))
    if temp3 == "V":
      print("Please input R H")
      dimensions = input().split(" ")
      A = int(dimensions[0])**2 * 3.14159265358979323846264338327
      Answer =  A * int(dimensions[1])
      print(Answer)
      #Callum could we make a google translate thats fax, how?
  if temp2 == "CUBE":
    print("\nCube, SA or Volume(V)")
    temp3 = input()
    if temp3 == "SA":
      print("Please input side length")
      dimensions = input().split(" ")
      LA = int(dimensions[0]) * 4 * int(dimensions[0])
      A = int(dimensions[0]) * int(dimensions[0])
      Answer =  LA + 2 * A
      print(str(Answer))
    if temp3 == "V":
      print("Please input side length")
      dimensions = input().split(" ")
      print(str(int(dimensions[0]) * int(dimensions[0]) * int(dimensions[0])))
  if temp2 == "TP":
    print("\nTriangular Prism, SA or Volume(V)")
    temp3 = input()
    if temp3 == "SA":
      print("Please input B H L")
      dimensions = input().split(" ")
      P1 = int(int(dimensions[0])/2)**2 
      P2 = int(int(dimensions[1])**2)
      P3 = math.sqrt(P1 + P2)
      PF = P3*2 + int(dimensions[0])
      
      LA = PF * int(dimensions[2])
      A = int(dimensions[0])*int(dimensions[1])/2
      Answer = A * 2 + LA
      print(str(Answer))
    if temp3 == "V":
      print("Please input Base_length Base_Height Prism_Length")
      
      dimensions = input().split(" ")
      A1 = int(dimensions[0])*int(dimensions[1])/2
      print(str(int(dimensions[2]) * A1) )
  if temp2 == "CP":
      
    print("\nCustom Prism, SA or Volume(V)")
    temp3 = input()
    if temp3 == "SA":
      print("Please input side length, number of sides and height")
      dimensions = input().split(" ")
      LA = int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2])
      sideC = int(dimensions[0])**2
      sideA = (int(dimensions[0])/2)**2
      apothem = math.sqrt(sideC - sideA)
      A = ((int(dimensions[0]) * apothem)/2) * int(dimensions[1])
      print(str(LA + (2 * A)))
    if temp3 == "V":
      print("Please input side length, number of sides and height")
      dimensions = input().split(" ")
      sideC = int(dimensions[0])**2
      sideA = (int(dimensions[0])/2)**2
      apothem = math.sqrt(sideC - sideA)
      A = ((int(dimensions[0]) * apothem)/2) * int(dimensions[1])
      print(str(A * int(dimensions[2])))
  if temp2 == "SPH":
      
    print("\nSphere, SA or Volume(V)")
    temp3 = input()
    if temp3 == "SA":
      print("Please input Radius")
      dimensions = input().split(" ")
      LA = dimensions[0]**2 * 4 * 3.14159265358979323846264338327
      
      print(LA)
    if temp3 == "V":
      print("Please input Radius")
      dimensions = input().split(" ")
      sideC = (int(dimensions[0])**3 * 3.14159265358979323846264338327 * 4 / 3)
      
      print(str(sideC))


    
def FMA():
    n = 0
    FMA = input('<Force(N)>, <Mass(kg)>, <Acceleration(m/s²)> (put dash < - > and that one will be solved for)')
    lis = FMA.split(',')
    print(lis)
    for i in range (0, int(len(lis))):
        if lis[n] == '-':
            if n == 0:
                print('Force is ' + str(int(lis[1])*int(lis[2])) + ' Newtons')
            if n == 1:
                print('Mass is ' + str(int(lis[0])/int(lis[2])) + ' kg')
            if n == 2:
                print('Acceleration is ' + str(int(lis[0])/int(lis[1])) + ' m/S²')
            
        n += 1
    
    


def vector():
    temp = input('Starting point and terminating point of vector: x,y x,y')
    lis = temp.split(' ')
    c1 = lis[0].split(',')
    c2 = lis[1].split(',')
    mag = math.sqrt(((abs(int(c1[0]) - int(c2[0])))**2) + ((abs((int(c1[1])) - int(c2[1])))**2))
    dir1 = int(c1[0]) - int(c2[0])
    dir2 = int(c1[1]) - int(c2[1])
    print("Magnitude: " + str(mag) + "\n Direction: " + str(dir1) + ', ' + str(dir2))


def cf():
    temp = input("<Mass of fluid>, <Volume of fluid> -  <Mass of object/second fluid>, Volume of object/second fluid>")
    l = temp.split('-')
    d1 = l[0].split(',')
    d2 = l[1].split(',')
    den1 = int(d1[0])/int(d1[1])
    print("Density of first: " + str(den1) )
    den2 = int(d2[0])/int(d2[1])
    print("Density of second: " + str(den2) )
    if den2 > den1:
        print("The second will float")
    else:
        print("the second will not float")
    
def pythag():
    n = 0
    temp = input("A,B,C  Write a dash in the place of the one you want solved for")
    templist = temp.split(',')
    for i in range (0 , 3):
        if templist[n] == '-':
            if n == 0:
                print("Side length A is: " + str(math.sqrt((int(templist[2])**2) - (int(templist[1])**2))))
                break
            if n == 1:
                print("Side length B is: " + str(math.sqrt((int(templist[2])**2) - (int(templist[0])**2))))
                
            if n == 2:
                print("Side length C is: " + str(math.sqrt((int(templist[0])**2) + (int(templist[1])**2))))
        n += 1
                
                
def Den():
    temp = input("Mass(g),Volume(ml)")
    l1 = temp.split(',')
    print("The density is " + str(int(l1[0])/int(l1[1])) + "g/ml")               
        
        
if Option == 'LCM':
  temp = input("x,y")
  l2 = temp.split(',')
  LCM(l2[0],l2[1])
  print(intersect1)
if Option == 'RO':
  RO(input("Items:"))
if Option == 'GCF':
  l = (input("x,y").split(','))
  GCF(int(l[0]),int(l[1]))
if Option == 'FC':
  FC(input("x/y <operation> a/b <operation> c/d ...."))
if Option == 'FAC':
  FAC(int(input("Number to factorial?")))
if Option == 'volsa':
  volsa()
if Option == 'FMA':
  FMA()
if Option == 'vector':
  vector()
if Option == 'cf':
  cf()
if Option == 'pythag':
  pythag()
if Option == 'Den':
  Den()
  

  
  





