
class vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __str__(self):
        return "x:{0},y:{1},z:{2}".format(self.x, self.y,self.z)
      
    def get_len(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    @staticmethod
    def dot(self,other):
         return vector3D(self.x*other.z-self.z*othe.y,
         self.z*other.x-self.x*other.z,
         self.x*other.y-self.y*other.x)
    def scale(self,factor):
        self.x=self.x*factor
        self.y=self.y*factor
        self.z=self.z*factor
    @staticmethod
    def summ(self,other):
         return vector3D(self.x+other.x,
         self.y+other.y,self.z+other.z)
         
    def __add__(self,other):
         return vector3D(self.x+other,self.y+other,self.z+other)         




v1= vector3D(10,10,0)
v2= vector3D(20,10,0)
v3=v1+v2
print(v3)
a=v3.x
b=v3.y
c=v3.z
print(v1.get_len())
print(v2.get_len())
print(vector3D.dot(v1,v2)
print(v1.scale(2))
vector3D.summ(v1,v2)