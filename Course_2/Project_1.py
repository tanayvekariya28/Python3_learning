### Project 1
import math
import numbers


#### Goal 1


class Polygon:
    def __init__(self, n, r) -> None:
        if isinstance(r, numbers.Real) and isinstance(r, numbers.Real):
            self._r = r
            self._n = n
    
    @property
    def n(self):
        return self._n
    
    @property
    def r(self):
        return self._r
    
    @property
    def iangle(self):
        return (self.n-2)*(180/self.n)
    
    @property
    def edge(self):
        return 2*self.r* math.sin(math.pi/self.n)
    
    @property
    def apothem(self):
        return self.r*math.cos(math.pi/self.n)
    
    @property
    def area(self):
        return 0.5 * self.n*self.edge()*self.apothem()
    
    @property
    def perimeter(self):
        return self.n*self.apothem()
    
    def __repr__(self):
        return f'Polygon({self.n}, {self.r})'
    
    def __eq__(self, other) -> bool:
        return self.n == other.n and self.r == other.r
    
    def __gt__(self, other):
        return self.n> other.n
    

    #### Goal 2
    # class Polygons:
    #     def __init__(self) -> None:
            