# a=50
# print(type(a))
# b=60.5
# print(type(b))
# c="jagathis"
# print(type(c))
# a=True
# print(type(a))

#complex datatypes

#list
# a=[10,40,60]
# a[2]=30
# print(a)
# print(a[1])

#tuple
# s=(40,67,80,56)
# print(s)
# print(s[0])

#set
#it removes duplicates
# a={10,10,20,20,30,30,40,40,50,50,50}
# b=list(a)
# print(a)
# print(b)
# print(b[4])
#dict
# person={
#     "name":"arisvaran", # name is key and arisvaran is value 
#     "dob":(2009,2010),
#     "address":"Kanchipuram"
    
# }

# person["dept"]="CSE" 
# print(person)
# print(person["dob"][1],person["name"])



# import math
# print(math.sqrt(9))
# print(math.factorial(6))
# print(math.ceil(5.7))
# print(math.floor(4.7))
# print(math.pi)
# print(math.pow(2,4))


# import random 
# print(random.randint(10,99))
# print(random.random())
# a=(3,5,7,8,9)
# print(random.choice(a))


import calendar
# year = 2026
# month=11
# print(calendar.month(year,month))  


from datetime import datetime
today = datetime.now()
print(calendar.month(today.year,today.month))

now=datetime.now()

print(now)
print(now.date())
print(now.month)
print(now.year)
print(now.time())
print(now.hour)









