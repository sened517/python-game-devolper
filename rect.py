import pgzrun

#assighn the sepective values to 
#the width and height of the screen
WIDTH = 700
HEIGHT = 700

#all the actions that must repeat forever
#are written within this fuction
def draw() :
  
   w = WIDTH
   h = 200
   r = 255
   g = 0
   b = 135

   for i in range(20):
     # creating rectnagle but not making it appear 
     r1 = Rect((0, 0 ),(w,h))
    #making thr rectnagle appear
     r1.center = 350, 200
     screen.draw.rect (r1,(r, g, b))
     w = w-10
     h = h+10
     r = r-10
     g = g+10



#this command is used to 
#call the function draw() automaticlly
pgzrun.go()