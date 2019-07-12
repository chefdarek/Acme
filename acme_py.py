
"""
Acme Product Class file
"""
import random

class Product:
    """Class of Product 
    args: 
    
    name(str), weight(int),price(int),
    flammability(float),identifier(random generated int)
    
    methods:
      - stealability
      - explodes
    """  
    def __init__(
            self,
            name="Name",
            weight = 20,
            price = 10,
            flammability = 0.5,
            identifier = random.randint(100000,9999999)
    ):
        self.name = name
        self.weight = weight
        self.price = price
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        """Calculates price div weight 
        param: Self
        returns: str level of stealability
        """
        ratio_pw = (self.price/self.weight)
        if ratio_pw < 0.5:
          return "Not so stealable"
        if ratio_pw >= 0.5 and ratio_pw <1.0:
          return "Kinda stealable"
        else:
          return "Very Stealable"
        
    def explode(self):
      """Calculates flammability times weight
      params: self
      returns: str level explodability
      """
      splodtio = (self.flammability * self.weight)
      
      if splodtio < 10:
        return "...fizzle."
      if splodtio >= 10 and splodtio < 50:
        return "...boom!"
      else:
        return "...BABOOM!!"

class Boxingglove(Product):
  """Subclass of Product"""
  def __init__(self, weight=10):
    self.weight = weight
    
  def explode(self):
    return "...its a glove."
  
  def punch(self):
    """ 
    Evaluates weight and returns strength of punch
    param: Self
    returns: str of punch 
    """
    if self.weight < 5:
      return "That tickles."
    
    if self.weight is >= 5 and self.weight < 15:
      return "Hey that hurt!"
    
    else:
      return "OUCH!"
