class Rectangle:
     def __init__(self, width, height):
         self._width = width
         self._height = height

    #  def get_width(self):
    #      return self._width
     
    #  def set_width(self, width):
    #      if width < 0:
    #          raise ValueError('width cannot be negative')
        #  else:
        #      self._width = width
         # until and unless you do not have to use restrictions on setting value of a property
     @property
     def height(self):
         return self._height

     def __str__(self):
         return 'rectangle : height = {0}, width = {1}'.format(self._height,self._width)
    
     def __repr__(self):
         return 'Rectangle({0},{1})'.format(self._width,self._height)
    
     def __eq__(self, other):
         if isinstance(other, Rectangle):
            return self._height == other._height and self._width == other._width
         else:
             return False
    #  def __lt__(self, other):
    #      if isinstance(other, Rectangle):
    #          return self.area() < other.area()
    #      else:
    #          return NotImplemented
     # getter and setter

r1 = Rectangle(1,2)
r2 = Rectangle(10,2)
r1.set_width(5)
print (r1.get_width()) 
    
    
#     ####to over ride a function, let's say f we have to define it like this -  def __f__():
    

# print(r1.area(),' ', r1.perimeter())
# print(str(r1),r1)
# #print(r1.str())
# print(r1)
# print(r1 == r2, 21 == 100)

# print(r1<r2, ' ', r1<387)
# #####__repr__ stands for representation,
# #####__eq__ used to define comparision between two objects of same class

 
# #### "is not' doesn't use __eq__ for comparision so even if '==' generates true is not generate false, coz two objects created at different 
# #### are stored in different locations.
 # __lt__  -> less than, likewise
#  __gt__() , __le__(), __ge__() 

