from graphics import *

W = GraphWin ("Fia Utan Knuff", 800,800)
PathList = []

def main():
    W.setBackground("Black")
    
    cr = Lcircle(150, 150, 60, "red")

    c1 = Lcircle(150, 300, 25, "red")
    c2 = Lcircle(200, 300, 25, "white")
    c3 = Lcircle(250, 300, 25, "white")
    c4 = Lcircle(300, 300, 25, "white")
    c5 = Lcircle(300, 250, 25, "white")
    c6 = Lcircle(300, 200, 25, "white")
    c7 = Lcircle(300, 150, 25, "white")
    c8 = Lcircle(350, 150, 25, "white")

    cg = Lcircle(550, 150, 60, "green")

    c9 = Lcircle(400, 150, 25, "green")
    c10 = Lcircle(400, 200, 25, "white")
    c11 = Lcircle(400, 250, 25, "white")
    c12 = Lcircle(400, 300, 25, "white")
    c13 = Lcircle(450, 300, 25, "white")
    c14 = Lcircle(500, 300, 25, "white")
    c15 = Lcircle(550, 300, 25, "white")
    c16 = Lcircle(550, 350, 25, "white")

    cb = Lcircle(550, 550, 60, "blue")

    c17 = Lcircle(550, 400, 25, "blue")
    c18 = Lcircle(500, 400, 25, "white")
    c19 = Lcircle(450, 400, 25, "white")
    c20 = Lcircle(400, 400, 25, "white")
    c21 = Lcircle(400, 450, 25, "white")
    c22 = Lcircle(400, 500, 25, "white")
    c23 = Lcircle(400, 550, 25, "white")
    c24 = Lcircle(350, 550, 25, "white")

    cy = Lcircle(150, 550, 60, "yellow")

    c25 = Lcircle(300, 550, 25, "yellow")
    c26 = Lcircle(300, 500, 25, "white")
    c27 = Lcircle(300, 450, 25, "white")
    c28 = Lcircle(300, 400, 25, "white")
    c29 = Lcircle(250, 400, 25, "white")
    c30 = Lcircle(200, 400, 25, "white")
    c31 = Lcircle(150, 400, 25, "white")
    c32 = Lcircle(150, 350, 25, "white")
  
    

    redpathlist = [cr,c1,c2,c3,c4,c5,c6,c7,c8,c9,
                   c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,
                   c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,
                   c30,c31,c32]
    greenpathlist = [cg,c9,c10,c11,c12,c13,c14,c15,c16,c17,
                     c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,
                     c28,c29,c30,c31,c32,c1,c2,c3,c4,c5,
                     c6,c7,c8]
    bluepathlist = [cb,c17,c18,c19,c20,c21,c22,c23,c24,c25,
                     c26,c27,c28,c29,c30,c31,c32,c1,c2,c3,
                     c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,
                     c14,c15,c16]
    yellowpathlist = [cy,c25,
                     c26,c27,c28,c29,c30,c31,c32,c1,c2,c3,
                     c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,
                     c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24]
    
    
    red = player("red",0,redpathlist)
    green = player("green",0,greenpathlist)
    blue = player("blue",0,bluepathlist)
    yellow = player("yellow",0,yellowpathlist)
    while True:
        if W.getMouse():
            red.nextPosition()
            green.nextPosition()
            blue.nextPosition()
            yellow.nextPosition()
        else:
            print None
    

class Lcircle(object):
    def __init__(self, x, y, rad, color):
        self.mp = Point(x,y)
        self.rad = rad
        self.color = color
        a = Circle(self.mp,self.rad)
        self.a = a
        a.setFill(color)
        a.draw(W)
        PathList.append(self)
        

class ccirkel(object):
    def __init__(self, x, y):
        Circle(Point(400,400),10)
    

class player(object):
    def __init__(self, color, index, pathlist):
        self.index = index
        self.pathlist = pathlist
        self.mp = self.pathlist[self.index].mp
        a = Circle(self.mp,10)
        self.a = a
        a.setFill(color) 
        a.draw(W)
        
    def nextPosition(self):
        print "Here is Pathlist object", self.pathlist[self.index].a
        p1 = self.pathlist[self.index].a.getCenter()
        x1 = p1.getX()
        y1 = p1.getY()
        self.index = self.index + 1
        p2 = self.pathlist[self.index].a.getCenter()
        x2 = p2.getX()
        y2 = p2.getY()

        dx = (x2-x1)
        dy = (y2-y1)
        
        self.a.move(dx,dy)



    

main()


#http://www.cs.swarthmore.edu/~newhall/cs21/pythondocs/using-graphics.html
