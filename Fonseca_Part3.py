import turtle
import arcpy, arcinfo
from arcpy import env

env.workspace = "C:Users\Gina\Documents\PIes"
env.overwriteOutput = True 

#Turtle Customization
wn = turtle.Screen() # this opens the screen adn defines the color of it
wn.bgcolor("blue")
ash = turtle.Turtle() #these define turtle chracteristis such as color & shape
ash.color("hotpink")
ash.shape("turtle")

#turtle variables
ask = input("Enter a number let's put Ash to work! ") #this variable is an input for users. HEre users put anumber and it will create a shape according to that number
if ask < 2: # the answer the user gets if the inteer is less than 2
	print "Oh no Ash went crazy!!! Please write a number"

turn = 180 - ((ask - 2) * 180.0 / ask) #this variable calculates and creates the shape according to the "ask " variable
    
#ARCGIS Variables
turtlepoints = arcpy.Array()
shplocation = "C:\Users\Gina\Documents\PIes"

nameshape = "turtlemap.shp"



for x in range (ask):
	initialposition = arcpy.Point(ash.xcor(),ash.ycor())
	turtlepoints.add(initialposition)
	x = 0
	while x < ask:  # what happens to the turtle when you don't put an integer
		ash.forward(100)
		ash.left(turn)
		x = x + 1



arcpy.management.CreateFeatureclass(shplocation, nameshape, "Polygon", spatial_reference= arcpy.SpatialReference(4326))
 
cursor = arcpy.da.InsertCursor(nameshape, ["SHAPE@"])
cursor.insertRow([arcpy.Polygon(turtlepoints)])

del cursor

wn.exitonclick() #this closes the window when you click it

#create points arcpy.array()




#import the polygons created to arcgis 
#workspace
#overwrite
#save variable
#shapefilevariable

#set a spatial reference using the arcpy.management. createfeaturetofeatureclass

#make those polygons into feature classes using cursors remember to unlock them 