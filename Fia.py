from graphics import *
import math
import random

W = GraphWin ("Fia Utan Knuff", 800,800)
PathList = []

def checkBump(moved, c1, c2, c3):
    if inCircle(moved.getP2(), c1.getplayercircle()):
        c1.backtobase()
    elif inCircle(moved.getP2(), c2.getplayercircle()):
        c2.backtobase()
    elif inCircle(moved.getP2(), c3.getplayercircle()):
        c3.backtobase()
    else:
        return None
   
def main():
    W.setBackground("Black")
    smallCircle = Circle(Point(0, 0), 25)
     
    'red base'
    global cr
    cr = Lcircle(150, 150, 60, "red")
    'reds path (8 steps + 3 final steps)'
    c1 = Lcircle(150, 300, 25, "white")
    c2 = Lcircle(200, 300, 25, "white")
    c3 = Lcircle(250, 300, 25, "white")
    c4 = Lcircle(300, 300, 25, "white")
    c5 = Lcircle(300, 250, 25, "white")
    c6 = Lcircle(300, 200, 25, "white")
    c7 = Lcircle(300, 150, 25, "white")
    c8 = Lcircle(350, 150, 25, "white")

    r1 = Lcircle(200, 350, 25, "red")
    r2 = Lcircle(250, 350, 25, "red")
    r3 = Lcircle(300, 350, 25, "red")
    
    'green base'
    global cg
    cg = Lcircle(550, 150, 60, "green")
    'green path (8 steps + 3 final steps)'
    c9 = Lcircle(400, 150, 25, "white")
    c10 = Lcircle(400, 200, 25, "white")
    c11 = Lcircle(400, 250, 25, "white")
    c12 = Lcircle(400, 300, 25, "white")
    c13 = Lcircle(450, 300, 25, "white")
    c14 = Lcircle(500, 300, 25, "white")
    c15 = Lcircle(550, 300, 25, "white")
    c16 = Lcircle(550, 350, 25, "white")

    g1 = Lcircle(350, 200, 25, "green") 
    g2 = Lcircle(350, 250, 25, "green")
    g3 = Lcircle(350, 300, 25, "green")

    'blue base'
    global cb
    cb = Lcircle(550, 550, 60, "blue")
    'blue path (8 steps + 3 final steps)'
    c17 = Lcircle(550, 400, 25, "white")
    c18 = Lcircle(500, 400, 25, "white")
    c19 = Lcircle(450, 400, 25, "white")
    c20 = Lcircle(400, 400, 25, "white")
    c21 = Lcircle(400, 450, 25, "white")
    c22 = Lcircle(400, 500, 25, "white")
    c23 = Lcircle(400, 550, 25, "white")
    c24 = Lcircle(350, 550, 25, "white")

    b1 = Lcircle(500, 350, 25, "blue")
    b2 = Lcircle(450, 350, 25, "blue")
    b3 = Lcircle(400, 350, 25, "blue")

    'yellow base'
    global cy
    cy = Lcircle(150, 550, 60, "yellow")
    'yellow path (8 steps + 3 final steps)'
    c25 = Lcircle(300, 550, 25, "white")
    c26 = Lcircle(300, 500, 25, "white")
    c27 = Lcircle(300, 450, 25, "white")
    c28 = Lcircle(300, 400, 25, "white")
    c29 = Lcircle(250, 400, 25, "white")
    c30 = Lcircle(200, 400, 25, "white")
    c31 = Lcircle(150, 400, 25, "white")
    c32 = Lcircle(150, 350, 25, "white")
    
    y1 = Lcircle(350, 500, 25, "yellow")
    y2 = Lcircle(350, 450, 25, "yellow")
    y3 = Lcircle(350, 400, 25, "yellow")


    goal = Lcircle(350, 350, 25, "black")
    
    
    'full player paths'
    redpathlist = [cr,c1,c2,c3,c4,c5,c6,c7,c8,c9,
                   c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,
                   c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,
                   c30,c31,c32,r1,r2,r3,goal]
    greenpathlist = [cg,c9,c10,c11,c12,c13,c14,c15,c16,c17,
                     c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,
                     c28,c29,c30,c31,c32,c1,c2,c3,c4,c5,
                     c6,c7,c8,g1,g2,g3,goal]
    bluepathlist = [cb,c17,c18,c19,c20,c21,c22,c23,c24,c25,
                     c26,c27,c28,c29,c30,c31,c32,c1,c2,c3,
                     c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,
                     c14,c15,c16,b1,b2,b3,goal]
    yellowpathlist = [cy,c25,
                     c26,c27,c28,c29,c30,c31,c32,c1,c2,c3,
                     c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,
                     c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,
                     c24,y1,y2,y3,goal]
    
    global red
    red = player("red", 0, redpathlist)
    global green
    green = player("green", 0, greenpathlist)
    global blue
    blue = player("blue", 0, bluepathlist)
    global yellow
    yellow = player("yellow", 0, yellowpathlist)
  
    while True:
        p=W.getMouse()

        cr.checkBaseClick(p)
        
        red.checkClick(p)
        checkBump(red, green, blue, yellow)
        
        green.checkClick(p)
        checkBump(green, red, blue, yellow)
        
        blue.checkClick(p)
        checkBump(blue, green, red, yellow)
        
        yellow.checkClick(p)
        checkBump(yellow, green, blue, red)

class Lcircle(object):
    def __init__(self, x, y, radius, color):
        self.centerpoint = Point(x, y)
        self.radius = radius
        self.color = color
        circle = Circle(self.centerpoint,self.radius)
        self.circle = circle
        circle.setFill(color)
        circle.draw(W)
        PathList.append(self)

    def checkBaseClick(self, p):
        if inCircle(p, cr.circle):
            if not inCircle(red.circle.getCenter(),cr.circle):
                print "You have moved red player by clicking on red base."
                red.nextPosition()
                return True
            elif not inCircle(p, red.circle):
                print "You have moved red player by clicking on red base."
                red.nextPosition()
                return True

        elif inCircle(p, cg.circle):
            if not inCircle(green.circle.getCenter(), cg.circle):
                print "You have moved green player by clicking on green base."
                green.nextPosition()
                return True
            elif not inCircle(p, green.circle):
                print "You have moved green player by clicking on green base."
                green.nextPosition()
                return True
            
        elif inCircle(p, cb.circle):
            if not inCircle(green.circle.getCenter(), cb.circle):
                print "You have moved blue player by clicking on blue base."
                blue.nextPosition()
                return True
            elif not inCircle(p, blue.circle):
                print "You have moved blue player by clicking on blue base."
                blue.nextPosition()
                return True
            
        elif inCircle(p, cy.circle):
            if not inCircle(yellow.circle.getCenter(), cy.circle):
                print "You have moved yellow player by clicking on yellow base."
                yellow.nextPosition()
                return True
            elif not inCircle(p, yellow.circle):
                print "You have moved yellow player by clicking on yellow base."
                yellow.nextPosition()
                return True
        else:
            return False
  
class player(object):
    def __init__(self, color, index, pathlist):
        self.index = index
        self.pathlist = pathlist
        self.centerpoint = self.pathlist[self.index].centerpoint
        circle = Circle(self.centerpoint, 10)
        self.circle = circle
        circle.setFill(color) 
        circle.draw(W)
        self.color = color
             
    def getP2(self):
        return self.circle.getCenter()

    def getplayercircle(self):
        return self.circle
    
    def backtobase(self):
        self.index = 0
        p1 = self.circle.getCenter()
        x1 = p1.getX()
        y1 = p1.getY()

        p2 = self.pathlist[self.index].circle.getCenter()
        x2 = p2.getX()
        y2 = p2.getY()
        
        dx = (x2-x1)
        dy = (y2-y1)
        self.circle.move(dx, dy)
        
    def nextPosition(self):
        p1 = self.pathlist[self.index].circle.getCenter()
        x1 = p1.getX()
        y1 = p1.getY()
        self.index = self.index
        tempdicevalue = 0
        
        if self.pathlist[self.index] != self.pathlist[-1]:
            tempdicevalue = dice(1, 6)
            
            if self.pathlist[self.index] == self.pathlist[-2]:
                tempdicevalue = dice(1, 1)
            elif self.pathlist[self.index] == self.pathlist[-3]:
                tempdicevalue = dice(1, 2)
            elif self.pathlist[self.index] == self.pathlist[-4]:
                tempdicevalue = dice(1, 3)
            elif self.pathlist[self.index] == self.pathlist[-5]:
                tempdicevalue = dice(0, 4)
            elif self.pathlist[self.index] == self.pathlist[-6]:
                tempdicevalue = dice(0, 5)

            print self.color,"player rolled >>", tempdicevalue, "<< and was moved to"
            print "X:", str(x1), ",", "Y:", str(y1)
            self.index = self.index + tempdicevalue
            tempx2 = self.pathlist[self.index].circle.getCenter().getX()
            tempy2 = self.pathlist[self.index].circle.getCenter().getY()
            print "from"
            print "X:", str(tempx2), ", Y:", str(tempy2)
            print "------------------------------------"            
        else:
            print "------------------------------------"
            print "------------------------------------"
            print "A player has won!"
            print "Game has been reset."
            print "------------------------------------"
            print "------------------------------------"
            main()
            
        p2 = self.pathlist[self.index].circle.getCenter()
        x2 = p2.getX()
        y2 = p2.getY()
        dx = (x2-x1)
        dy = (y2-y1)
        self.circle.move(dx, dy)
        
    def checkClick(self, p):
        if inCircle(p, self.circle):
            self.nextPosition()
            return True
        else:
            return False

def bump():
    if yellow.pathlist[index + 1] == red.pathlist[index]:
        red.pathlist[index] = red.pathlist[0]

def inCircle(p, smallCircle):    
    radius=smallCircle.getRadius()
    centerpoint=smallCircle.getCenter()
    cx = centerpoint.getX()
    cy = centerpoint.getY()
    x = p.getX()
    y = p.getY()
    distance = math.sqrt((cx - x)**2 +(cy - y)**2)
    if distance > radius:
        return False
    else:
        return True

def dice(From, sides):
    r = random.randint(From, sides)
    return r

main()



#http://www.cs.swarthmore.edu/~newhall/cs21/pythondocs/using-graphics.html
