print("Hello world")
print("How was your day")

number1 = 10.5 #float
age=30 #int
firstName= ("Jane")



#show output 
print(number1)
print(age)
print(firstName)


lastName= str("Owens")
print(lastName)

#Show variables type 
print(type(number1))
print(type(age))
print(type(firstName))
print(type(lastName))

gender = True #True is male, false is female
is_connected = False

print(gender)
print(is_connected)
print(type(gender))
print(type(is_connected))

#declaring seveal values at once
number1,number2,colour=20,30,"red"
print(number1)
print(colour)

x=y=z=0
print(x)
print(y)
print(z)

print("x is :"+str(x)  )

# print (firstName+lastName+age)
print(firstName+" "+ lastName +" " + "is"+" " + str(age) +" "+ "years old")
print(f"{firstName} {lastName} is {age} years old") #f_string

# Casting a number a number
length="25"
print(length)
print(f"type of length is : {type(length)}")
lengthNumber=int(length)
print(f"type of lengthNumber is : {type(lengthNumber)}")

#...............slice string (substring)............
message = "hello everybody!!!"
cool=message[0:12] 
print(cool)

age="hey"
ageNumber = int(age)
print (f" type of ageNumber is {type(ageNumber)}")


