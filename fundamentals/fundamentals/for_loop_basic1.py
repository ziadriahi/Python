# Basic
i=0
for i in range(151):
    print(i)

#Multiples of Five
j=1
while i < 1000 :
    i=j*5
    j+=1
    print(i)

# Counting the Dojo Way

for i in range(1,101):
    if (i%10 == 0) and (i%5 == 0) :
        print("Coding Dojo")
    elif i%5 == 0 :
        print("Coding")
    else :
            print(i)

# Whoa. That Sucker's Huge
j=0
for i in range(500001):
     j+=i

print(j)

# Countdown by Fours
for i in range(2018,0,-4):
     print(i)

# Flexible counter

def Flexible_counter(lowNum,highNum,mult):
     for i in range(lowNum,highNum+1):
          if i%mult == 0 :
               print(i)
Flexible_counter(2,9,3)