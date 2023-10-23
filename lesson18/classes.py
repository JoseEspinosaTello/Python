#classes are kinda like blueprints when we want to create somthing
# we are going to create objects using classes
# classes are blueprints for objects
#method is a function that is a member of a class

class Vehicle: #always capitalize a class
    # we will define a method which will be an action the object could take 
    #we will take properties and look at those as details about the class

    
         #class can have properties
        # properties are set using the inizializer funtion
    def __init__(self, make, model):
            
            self.make = make
            self.model  = model
    
    #add moves method
    def moves(self):
         
         print('moves along..')

    #can put more methods or properties on your class and retrieve those using a getter
    def get_make_model(self):
          print(f"I'm a {self.make} {self.model}")


#create an object of the class
my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model() # get method will be available
my_car.moves()


# now create my car
your_car = Vehicle("Honda", "Civic")
your_car.get_make_model()
your_car.moves()


### INHERITANCE

#new Airplane class will inherit Vehicle class
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model) # super means we will inherit those values from the parent class
        self.faa_id = faa_id
        print(faa_id)

    def moves(self):
            print('Flies along..')
    
            
            
        

class Truck(Vehicle):
      def moves(slef):
            print('Rumbles alon..')


class GolfCart(Vehicle):
      pass


#since all the new classes are vehicles we need to pass a make and a model

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')


cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n\n')


#Polymorphism####################################################
#the ability to behave differently in resoponse to the same input messages

#in this case it means we are goint to get different responses when we call get_make_model and moves, even though we are giving these objects the same input messages
#go ahead and provide the response to get_make_model and provide response to moves method for each of these objects

for v in (my_car, your_car, cessna, mack, golfwagon): #will loop through all of these objects and will get the response for each one.
      v.get_make_model()
      v.moves()