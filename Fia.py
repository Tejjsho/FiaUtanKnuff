from graphics import *


def main():

    W = GraphWin ("Fia Utan Knuff", 800,800)
    global W
    W.setBackground("Black")
   
    PathList = []
    global PathList
    
#    a = Circle(Point(100,100),10)
#    a.setFill("white")
#    a.draw(W)


    
    cr = Lcircle(150, 150, 60, "red")
    global cr
    print cr.mp.getX(), cr.mp.getY()

    c1 = Lcircle(150, 300, 25, "red")
    global c1
    c2 = Lcircle(200, 300, 25, "white")
    global c2  
    c3 = Lcircle(250, 300, 25, "white")
    global c3
    c4 = Lcircle(300, 300, 25, "white")
    global c4
    c5 = Lcircle(300, 250, 25, "white")
    global c5
    c6 = Lcircle(300, 200, 25, "white")
    global c6
    c7 = Lcircle(300, 150, 25, "white")
    global c7
    c8 = Lcircle(350, 150, 25, "white")
    global c8
    
    cg = Lcircle(550, 150, 60, "green")
    global cg

    c9 = Lcircle(400, 150, 25, "green")
    global c9
    c10 = Lcircle(400, 200, 25, "white")
    global c10
    c11 = Lcircle(400, 250, 25, "white")
    global c11
    c12 = Lcircle(400, 300, 25, "white")
    global c12
    c13 = Lcircle(450, 300, 25, "white")
    global c13
    c14 = Lcircle(500, 300, 25, "white")
    global c14
    c15 = Lcircle(550, 300, 25, "white")
    global c15
    c16 = Lcircle(550, 350, 25, "white")
    global c16

    cb = Lcircle(550, 550, 60, "blue")
    global cb

    c17 = Lcircle(550, 400, 25, "blue")
    global c17
    c18 = Lcircle(500, 400, 25, "white")
    global c18
    c19 = Lcircle(450, 400, 25, "white")
    global c19
    c20 = Lcircle(400, 400, 25, "white")
    global c20
    c21 = Lcircle(400, 450, 25, "white")
    global c21
    c22 = Lcircle(400, 500, 25, "white")
    global c22
    c23 = Lcircle(400, 550, 25, "white")
    global c23
    c24 = Lcircle(350, 550, 25, "white")
    global c24

    cy = Lcircle(150, 550, 60, "yellow")
    global cy

    c25 = Lcircle(300, 550, 25, "yellow")
    global c25
    c26 = Lcircle(300, 500, 25, "white")
    global c26
    c27 = Lcircle(300, 450, 25, "white")
    global c27
    c28 = Lcircle(300, 400, 25, "white")
    global c28
    c29 = Lcircle(250, 400, 25, "white")
    global c29
    c30 = Lcircle(200, 400, 25, "white")
    global c30
    c31 = Lcircle(150, 400, 25, "white")
    global c31
    c32 = Lcircle(150, 350, 25, "white")
    global c32
    

  
#    print PathList[0].mp.getX()
    #c1a.a.draw(W)
    red = player("red",0)

    while True:
        if W.getMouse():
            red.nextPosition()
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
    def __init__(self, color, index):
        #self.mp = Point(c13a.mp.getX(), c13a.mp.getY())
        self.index = index
        self.mp = PathList[self.index].mp
        a = Circle(self.mp,10)
        self.a = a
        a.setFill(color)
        #if color == "red":
            #self.mp = c1a.mp 
        a.draw(W)
        
    def nextPosition(self):
        print "Here is Pathlist object", PathList[self.index].a
        p1 = PathList[self.index].a.getCenter()
        x1 = p1.getX()
        y1 = p1.getY()
        self.index = self.index + 1
        p2 = PathList[self.index].a.getCenter()
        x2 = p2.getX()
        y2 = p2.getY()

        dx = (x2-x1)
        dy = (y2-y1)
        
        self.a.move(dx,dy)



    

main()


#http://www.cs.swarthmore.edu/~newhall/cs21/pythondocs/using-graphics.html
