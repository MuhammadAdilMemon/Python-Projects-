import random
import string


data=input("Enter your string : ")

characters=string.ascii_letters+string.digits

random1="".join(random.choices(characters,k=3))

random2="".join(random.choices(characters,k=3))


if len(data)>0 and len(data)<2:
    data=data[::-1]
    print(data)

else:
    data=data[1:]+data[0]
    data=random1+data
    data=data+random2
    print(data)

#to decode
print("decode")
data=data[3:-3]
data=data[-1]+data[0:-1]
print(data)