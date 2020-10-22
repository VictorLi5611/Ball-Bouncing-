""" VARIABLE MAP
VARIABLE            PURPOSE                   TYPE                       RANGE
x                   X location of ball        int                        20-980
y                   Y location of ball        int                        20-980    
bkx                 background Width          int                        1000
bky                 background Height         int                        1000
incrxBall          x incuments of ball        int                        3
incryBall          y incruments of ball       int                        3
upbound            upper boundary             int                        20
lowbound           lower boundary             int                        980
rbound             right boundary             int                        980
lbound             left boundary              int                        20
ballwidth          ball width                 int                        40
balllength         ball length                int                        40
dogx               x location of dog          int                        20-980
dogy               y location of dog          int                        20-980
dogWidth           dog width                  int                        40
dogHeight          dog height                 int                        40
incrxDog           x incruments of dog        int                        1- infinity
incryDong          y incruments of dog        int                        1- infinity
distance         distance between dog + ball  int                        20-1000
gameOver         game over screen             img                        N/A
back             background image             img                        N/A
dog              dog image                    img                        N/A
"""




import random
def setup():
    global x,y,bkx,bky,incrxBall,incryBall
    global upbound,lowbound,rbound,lbound, ballwidth, balllength
    global dogx, dogy, dogWidth, dogHeight, incrxDog, incryDog
    global distance, gameOver, back, dog
    #background 
    bkx = 1000
    bky = 1000
    #ball dimensions
    ballwidth = 40
    balllength = 40
    #ballBoundaries
    rbound = bkx - ballwidth/2
    lowbound = bky - balllength/2
    upbound = ballwidth/2
    lbound = balllength/2
    #increments 
    incrxBall = int(3)
    incryBall = int(3)
    incrxDog = int(1)
    incryDog = int(1)
    #ball location
    x = random.randint(lbound,rbound)
    y = random.randint(upbound,lowbound)
    #dog location
    dogx = 50
    dogy = 200
    #dog size
    dogWidth = 40
    dogHeight = 40
    
    distance = (dogWidth + ballwidth)/2
    
    gameOver = loadImage("gameover.png")
    back = loadImage("background.jpg")
    dog = loadImage ( "dog.jpg")
    size (1000,1000)


####################################################################################cheak numbers if positive or negitive
def negitive(num):
    if num > 0:
        num = int(-num)
    return num
def positive(num):
    if num < 0:
        num = int(-num)
    return num  
    
#####################################################################################dog movement
def dogMovement():
    global dogx, dogy, dogWidth, dogHeight, incrxDog, incryDog
    global upbound,lowbound,rbound,lbound
    
    image (dog, dogx,dogy,dogWidth, dogHeight)
    dogx = dogx + incrxDog
    dogy = dogy + incryDog

def dogBoundaries():
    global dogx,dogy,dogWidth,dogHeight, incrxDog,incryDog
    global upbound,lowbound,rbound,lbound
    
    if dogx > rbound:
        dogx = rbound 
        incrxDog = -incrxDog
    
        
    
    #set left DogBoundaries
    if dogx < lbound:
        dogx = lbound
        incrxDog = -incrxDog
    
   
    #set up DogBoundaries
    if dogy < upbound:
        dogy = upbound
        incryDog = -incryDog
    

    #set bottom DogBoundaries
    if dogy > lowbound:
        dogy = lowbound
        incryDog = -incryDog
#dog speed up
def speedUp():
    global incrxDog, incryDog
    if frameCount % 30 == 0:
        if incrxDog > 0:
            incrxDog = incrxDog + 0.5
        else:
            incrxDog = incrxDog - 0.5
        if incryDog > 0:
            incryDog = incryDog + 0.5
        else:
            incryDog = incryDog - 0.5
                         
#set tracking
def dogTracking():
    global dogx,dogy,x,y, incryDog,incrxDog    
    
    if dogx > x and dogy > y:
        incrxDog = negitive(incrxDog)   
        incryDog = negitive(incryDog)
    if dogx < x and dogy > y:
       incrxDog = positive(incrxDog)
       incryDog = negitive(incryDog)
    if dogx < x and dogy < y:
        incrxDog = positive(incrxDog)
        incryDog = positive(incryDog)
    if dogx > x and dogy < y:
        incrxDog = negitive(incrxDog)
        incryDog = positive(incryDog)
       
#####################################################################################ball movement
def ballMovement(): 
    global x,y,bkx,bky,incrxBall,incryBall
    global upbound,lowbound,rbound,lbound, ballwidth, balength
    ellipse (x, y , ballwidth,balllength)
    x = x + incrxBall
    y = y + incryBall
    
# randomize the direction of bounce
def randomizeBounces():
    keepGoing = True
    value = random.randint(-1,1)
    while keepGoing:
        if value == 0:
            value = random.randint(-1,1)
        else:
            keepGoing = False
    return value
        


    
    
# setballBoundaries
def ballBoundaries():
    global x,y,bkx,bky,incrxBall,incryBall,bouncelimit,bounceincr
    global upbound,lowbound,rbound,lbound, ballwidth, balllength
     #set right ballBoundaries
    if x > rbound:
        x = rbound 
        incrxBall = -incrxBall
        incryBall = incryBall * randomizeBounces()
        
    
    #set left ballBoundaries
    if x < lbound:
        x = lbound
        incrxBall = - incrxBall
        incryBall = incryBall * randomizeBounces()
   
    #set up ballBoundaries
    if y < upbound:
        y = upbound
        incryBall = -incryBall
        incrxBall = incrxBall * randomizeBounces()

    #set bottom ballBoundaries
    if y > lowbound:
        y = lowbound
        incryBall = -incryBall
        incrxBall = incrxBall * randomizeBounces()     
           
#calculate distance
def calcdistance(ax,ay,bx,by):
    distance = (( ax - bx )**2 + ( ay - by)**2)**0.5

    return distance

#end game
def endgame():
    global incrxBall,incryBall, incrxDog, incryDog ,bky,bkx, gameOver
    incrxBall = 0
    incryBall = 0
    incrxDog = 0
    incryDog = 0
    image(gameOver,0,0,bkx,bky)
    
def draw():
    global x,y,bkx,bky,incrxBall,incryBall
    global upbound,lowbound,rbound,lbound, ballwidth, balllength
    global dogx, dogy, dogWidth, dogHeight, incrxDog, incryDog
    global distance, back
    background (back)
    fill (204,102,0)
    ellipseMode(CENTER)
    rectMode(CENTER)
    #set ballBoundaries
    ballBoundaries() 
    #move ball
    ballMovement()
    #move dog
    dogMovement() 
    #dog tracking ball
    dogTracking()
    #dog speed up
    speedUp()
    #dog boundaries
    dogBoundaries()
    if calcdistance(x,y,dogx,dogy) < distance:
        endgame()

    
    
    

    

    
    
