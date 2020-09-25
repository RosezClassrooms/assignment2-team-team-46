from abc import ABC, abstractmethod #as usual

#First of all, let's create an array of each item divided into traversal, parts, and detection systems.

traversal=["Bipedal","Quadripedal","Wheeled","Flying"]
parts=["Bipedal legs","Quadripedal legs","Wings","Blades","Two wheels","Four wheels","Arms"]
detection_sys=["Camera Detection System","Infrared Detection System"]


#my aim is to not create different classes for each part of the robot.
class Robot:
  def __init__(self, name):
    self.name = name 
    self.traversal = []
    self.parts=[]
    self.detection = []
    
  def __str__(self):
    returnvalue = f'******Building an {self.name}******'
    returnvalue += f'\n{self.name} traverses with the system of: '
    for i in self.traversal:
      returnvalue+="\n"+i
    returnvalue += f'\n{self.name} has these parts: '
    for i in self.parts:
      returnvalue+="\n"+i
    returnvalue += f'\nAnd {self.name} uses the detection system of: '
    for i in self.detection:
      returnvalue+="\n"+i
    returnvalue+="\n"
    return returnvalue

    


class RobotBuilder(ABC):  #directly copy pasted from original file
    
  @abstractmethod
  def reset(self):
    pass

  @abstractmethod
  def build_traversal(self):
    pass

  @abstractmethod
  def build_detection_system(self):
    pass
  
  def get_product(self):
    return self.product


#builder classes for andriod and autonomous car
class AndroidBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot('Android')
  def reset(self):
    self.product = Robot("Android")

  def build_traversal(self):
    self.product.traversal.append(traversal[0])
    self.product.parts.append(parts[0])
    self.product.parts.append(parts[6])

  def build_detection_system(self):
    self.product.detection.append(detection_sys[0])


class AutonomousCarBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot('Autonomous Car')

  def reset(self):
    self.product = Robot('Autonomous Car')
    
  def build_traversal(self):
    self.product.traversal.append(traversal[2])
    self.product.parts.append(parts[5])

  def build_detection_system(self):
    self.product.detection.append(detection_sys[1])


#Director... need to combine the 2 make methods into 1
class Director:
    def make_robot(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()



def main():     #copy pasted from original file again.
  director = Director()

  builder = AndroidBuilder()
  print(director.make_robot(builder))

  builder = AutonomousCarBuilder()
  print(director.make_robot(builder))

if __name__=="__main__":
  main()