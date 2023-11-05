#1 Countdown functions
def Countdown(int):
    j=0
    x=[]

    for i in range(int,-1,-1):
        
        x.append(i)
    return x    
               
print(Countdown(5))

#2 Print and Return functions

def print_and_return(list):
    if len(list) != 2 : 
        print("Please enter a list with lenght 2")
    else:
        print(list[0])
        return list[1]

print(print_and_return([4,10]))

#3 First plus lenght functions
def first_plus_lenght(list):
    
    return list[0]+list[len(list)-1]

print(first_plus_lenght([1,2,3,4,5]))

#4 Values greater than second
def values_greater_than_second(list):
    list_greater=[]
    if len(list)<2 :
        return False
    else:
        for i in range(len(list)) :
            if list[i]>list[1] :
                list_greater.append(list[i])
        return list_greater

print(values_greater_than_second([5,2,3,2,4,1]))
print(values_greater_than_second([3]))

#5 This length that value
def lenght_and_value(size,val) :
    list=[]
    for i in range(size):
        list.append(val)
    return list

print(lenght_and_value(4,7))
print(lenght_and_value(6,2))