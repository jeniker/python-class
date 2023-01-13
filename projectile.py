from math import sin, cos, radians
class Projectile():
    # Projectile simulates the flight of a simple projectile
    # near the earth's surface, ignoring wind resistance
    # Tracking is done in two dimensions, height (y)
    # and distance (x)
    def __init__(self, angle, velocity, height,time):
        # creates a projectile with a given launch angle
        # initial velocity and height
        self.xpos = 0.0 # initial x position 
        self.ypos = height  # the height given by the user
        theta = radians(angle)  # the angle (how steep the rise of the projectile)
        self.xvel = velocity * cos(theta) # calculates the x positions given the speed
        self.yvel = velocity * sin(theta) # calculates the y positions given the speed
        self.biggestY = 0.0
       
    def update(self, t): # gives the progress of the projectile
        self.xpos = self.xpos + t * self.xvel # calculates the x position
        yvel1 = self.yvel - 9.8 * t  # accounts for the y position being
                                     # effected by gravity, calculates the y position
        self.ypos1 = self.ypos + t * (self.yvel + yvel1)/2.0  # calculates the y position
        self.ypos = self.ypos1
        self.yvel = yvel1  # changes the y position for the new calculation as it moves
        
        
        
    def getY(self):
        return self.ypos # returns the position of y

    def getX(self):
        return self.xpos  # returns the position of x


    def __str__(self):
        # returns the maximum height of the projectile 
        return "The maximum value of y is {0:0.1f}".format(self.biggestY)

if __name__ == '__main__':  # runs the program
        # obtain the initial values from the user
        a = eval(input("Enter the launch angle (in degrees):")) # angle
        v = eval(input("Enter the initial velocity (in meters/sec): "))  # velocity
        h = eval(input("Enter the initial height (in meters): "))  # height
        t = eval(input("Enter the time interval between position calculations: "))
                    # time interval that the program will use to calculate positions
        ylist = [0]
        cball = Projectile(a,v,h,t) # sends the data to the program to be calculated
        while cball.getY() >= 0.0:  # works until the height reaches the ground- "0"
            cball.update(t)
            ylist.append(cball.getY()) # makes an iterable list for the max function
        cball.biggestY = max(ylist)  # calculates the max value of y position
        print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))  # print results
        print(cball) # prints the max value of y position
        
        
        
