class shape():
    def __init__(self):
        pass
    def getArea(self):
        pass 

class rectangle (shape):
    def __init__(self,l,w):
        super().__init__()
        self.l=l
        self.w=w
    def getArea(self):
        return self.l*self.w
    
class circle(shape):
    def __init__(self,radius):
        super().__init__()
        self.radius= radius
    def getArea(self):
        return 3.1415*self.radius*self.radius
    
class triangle(shape):
    def __init__(self,b,h):
        super().__init__()
        self.b=b
        self.h=h
    def getArea(self):
        return 0.5*self.b*self.h

#read txt file

file=open(r'shape.txt')
lines=file.readlines()
file.close()

totalShapes=[]

for line in lines:
    components=line.split(',')
    shape=components [0]

    if shape == 'rectangle':
        x=float(components[1])
        y=float(components[2])
        totalShapes.append(rectangle(x,y))
    elif shape == 'circle':
        x=float(components[1])
        totalShapes.append(circle(x))
    elif shape =='triangle':
        x=float(components[1])
        y=float(components[2])
        totalShapes.append(triangle(x,y))
    else:
        pass
for shape in totalShapes:
    print(shape.getArea())