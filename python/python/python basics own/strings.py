#strings working with  the textual data
message="hellp  booby"
print(message)
name='ayush"ayu"'
print(name)
print(len(message))
print(len(name))
#slicing
print(name[0:3])
print(name[-10:-1])
print(message.casefold())
print(message.find('ayu'))
print(name.find('ayu'))

greeting="namaste"
name="gagandeep"
#concatinaiton
mess=greeting + ' ' + name
print(mess)
age=25
#mess2=f" {}.my name is .{}."
#f strings formattting
mess2=f" hello my name is {name.upper()}and i am {age} years old"
print(mess2)
#formatting using format methods
mess3='{} ,{} . your age is {}'.format(name,greeting,age)
print(mess3)
#print(dir(name))
print("\n")
#print(help(str))


name="ayush"
print(name.upper())
print(name.capitalize())
print(message.casefold())