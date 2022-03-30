class Car(object):
    """
       blueprint for the car

    """

def _init_(self,model,color,company,speed_limit):
    self.color=color
    self.company=company
    self.speed_limit=speed_limit
    self.model=model
    
def start(self):
    print("started")

def stop(self):
    print("stop")    

def accelarate(self):
    print("accelarating") 
    "accelarate functionality here"
    
def change_gear(self,gear_type):
    print("gear_changed")      
    "gear related functionality here"
    
rolls_royce=Car("phantom convertible coupe","Golden","rolls_royce",155) 

print(rolls_royce.start())
     