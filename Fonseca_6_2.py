# Gina Fonseca 



#Chapter 6 Challenge 2



#Write a script that reads all the feature classes in a personal or file
#geodatabase and copies only the polygon feature classes to a new file
#geodatabase. You can assume there are no feature datasets in the existing
#data, and the feature classes can keep the same name.
#
#
#
import arcpy
from arcpy import env
env.overwriteOutput = True #this is in case you get an error the first time it overwrites the previous attempt
env.workspace = "C:\EsriPress\Python\Data\Exercise06\Results\NM.gdb" # Here is the enviroment I used NM. GDB bbecause it is a GDB created during Chapter 6 training

outputGDBpath = "C:\EsriPress\Python\Data\Exercise06\Results" # Here I created a variable for the path where I want my new GDB
outputname = "GFC2.gdb"                                     #HEre is the name of the new GDB I will create and put the polygon feature classes in
arcpy.CreateFileGDB_management(outputGDBpath, outputname) # this create the new GDB by only using the variable i created

fclist = arcpy.ListFeatureClasses("*", "polygon") #this looks for only the polygons feature classes
for fc in fclist:
	fcdesc = arcpy.Describe(fc)
	arcpy.CopyFeatures_management (fc, "C:\EsriPress\Python\Data\Exercise06\Results\GFC2.gdb" + fcdesc.basename)



print "It has been executed successfully!" 