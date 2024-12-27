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

class Car:
    # constructor
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

    def self_driving(self,engine):
        print("The car type is {} engine ".format(engine))


car1=Car(4,4,"petrol")
print("The no of tyres in object car1 is {}".format(car1.tyres))
print("The no of windows in object car1 is {}".format(car1.windows))
car1.self_driving("electric")

if __name__=='__main__':
    car1.self_drivingd