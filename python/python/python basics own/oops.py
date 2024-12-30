import math
# class is a blueprint of an object
# object is an instance of a class
# class is a logical entity         
# object is a physical entity
# so everthing in python is an object there are 6  pillars of oops in python
# 1. class
# 2. object
# 3. method
# 4. inheritance
# 5. polymorphism
# 6. encapsulation

# class has four things one is attributes and anothers are methods constructor and destructor and magic words(__init__ , __del__, __str__, __repr__, __add__, __sub__, __mul__, __div__)
  # attributes are the properties of the class or in simple words the variables of the class they might be public or private 
  # methods are the functions of the class they might be public or private 
  #magic words are the special functions in python which are used to perform some special operations like addition, subtraction, multiplication, division, etc
  # constructor is a special method in python which is used to initialize the attributes of the class
     #when we make an object of the class the constructor is called automatically we no need to call is explicitly like another method
     #constructor is also called as __init__ method
     #constructor is also called as instance method
        #constructor is also called as initializer
# destructor is a special method in python which is used to destroy the object of the class
        #destructor is also called as __del__ method
        #destructor is also called as instance method
        #destructor is also called as finalizer
# encapsulation is the process of binding the data and the functions that manipulate the data  
 # encapsulation is also called as data hiding when we make the attributes of the class private
 # and then access them using the getter and setter methods
 # encapsulation is also called as data abstraction when we make the attributes of the class private     
# inheritance is the process of inheriting the properties of the parent class to the child class
# polymorphism is the process of performing the same operation in different ways
# abstraction is the process of hiding the implementation details and showing only the functionality to the user

#so there is a list of progrma to practice the oop in python

#1. create a class and object in python
#2. create a class with constructor in python
#3. create a class with destructor in python
#4. create a class with attributes and methods in python

#a simple clas of car not having the constructor 
class Car:
    pass

car1= Car()
car2= Car()

car1.windows=4
car1.tyres=4
car1.engine="diesel"

car2.windows=6
car2.tyres=6
car2.engine="petrol"

print(car1.engine)
print(car2.engine)

#print(dir(car1))
# having the constructor in the class
class Car:
    # constructor
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

    def self_driving(self,engine):
        print("The car type is {} it so cast effective  ".format(engine))


car1=Car(4,4,"petrol")
print("The no of tyres in object car1 is {}".format(car1.tyres))
print("The no of windows in object car1 is {}".format(car1.windows))
car1.self_driving("electric")


# __name__ is a special variable in python which is used to check whether the code is run as a script or as a module
if __name__=='__main__':
    car1.self_driving("electric")

# create a class of the fraction data typee

#description: a fraction number has two parts one is the numerator and the other is the denominator 
  # for the fraction number 1/2 the numerator is 1 and the denominator is 2
  #for the algerbra like add we to take the lcm ofthe denominator and then add the numerator in the follawing way 
    # 1/2 + 1/3 = 3/6 + 2/6 = 5/6
    # so the formula for the addicton is (a/b) + (c/d) = (ad+bc)/bd in terms of numinator and denominator numinator is ad+bc and denominator is bd
    # for the subtraction the formula is (a/b) - (c/d) = (ad-bc)/bd
    # for the multiplication the formula is (a/b) * (c/d) = (a*c)/(b*d)
    # for the division the formula is (a/b) / (c/d) = (a*d)/(b*c)

class Fraction:
    
    def __init__(self,x,y):
        self.numinator=x
        self.denominator=y

    def __str__(self):
        return "The fraction is {}/{}".format(self.numinator,self.denominator)

    def __add__(self,other):
        numinator=self.numinator*other.denominator + self.denominator*other.numinator
        denominator=self.denominator*other.denominator
        return Fraction(numinator,denominator)
    def __sub__(self,other):
        numinator=self.numinator*other.denominator - self.denominator*other.numinator
        denominator=self.denominator*other.denominator
        return Fraction(numinator,denominator)
    def __mul__(self,other):
        numinator=self.numinator*other.numinator
        denominator=self.denominator*other.denominator
        return Fraction(numinator,denominator)
    def __truediv__(self,other):
        numinator=self.numinator*other.denominator
        denominator=self.denominator*other.numinator
        return Fraction(numinator,denominator)

# add the simplyfy method to the class to simply fy the fratcion number JUS The maths module which has gcd method whic hgive as the greatest common divisor(in simpler terms the comman factor of the two numbers)
    def simplyfy(self):
        comman_divisor=math.gcd(self.numinator,self.denominator)
        self.numinator=self.numinator // comman_divisor
        self.denominator=self.denominator // comman_divisor

        return self


f1=Fraction(36,2)
f2=Fraction(3,4)

result=f1*f2
print(result)
n=result.simplyfy()
print(n)


# Further operations like multiplication are not possible:
# there are two ways to retunn the results one is in the string formate or in the object formate 
#when we return a string 
                  #f1 = Fraction(1, 2)
                  #f2 = Fraction(3, 4)
                  #result = f1 * f2
                  #print(result)  # Output: "3/8"
                  # Further operations like multiplication are not possible:
                  # f3 = Fraction(5, 6)
                  # new_result = result * f3  # This will raise an error!

# when we return the object
                #f1 = Fraction(1, 2)
                #f2 = Fraction(3, 4)

                #result = f1 * f2
                #print(result)  # Output: <__main__.Fraction object at 0x...> (or after adding __str__, "3/8")

                # You can still do:
                #f3 = Fraction(5, 6)
                #new_result = result * f3  # Multiplying another Fraction object.
#Returning a Fraction Object:

#You keep the result as a Fraction instance.
#You can still perform mathematical operations (like *, +) on the result because it’s a proper object.

#Returning a String:
#You lose the ability to use the result as a fraction in calculations.
# #It’s now only a textual representation, mainly useful for displaying output.

# if you wnat to display the result in the string formate then you have to use the __str__ method along with the object functioanlity


# if you leran the concept then try to make  class for the comlex nunmber and then try to add the substract the two complex numbers
# the complex number has two parts one is the real part and the other is the imaginary part
# the complex number is represented as a+bi where a is the real part and bi is the imaginary part
# the addition of the two complex number is done in the following way
# (a+bi) + (c+di) = (a+c) + (b+d)i
# the subtraction of the two complex number is done in the following way
# (a+bi) - (c+di) = (a-c) + (b-d)i
# the multiplication of the two complex number is done in the following way
# (a+bi) * (c+di) = (ac-bd) + (ad+bc)i
# the division of the two complex number is done in the following way
# (a+bi) / (c+di) = (ac+bd)/(c^2+d^2) + (bc-ad)i/(c^2+d^2)
  

  # ther are some hints for the complex number class