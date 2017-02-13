#Write a script that determines whether the following extensions are available:
#ArcGIS 3D Analyst, ArcGIS Network Analyst, and ArcGIS Spatial
#Analyst. The script should print an informative message with the results,
#such as "The following extensions are available: ...".

#Gina Fonseca 

#Chapter 5 Challenge Problem 4


import arcpy
#Extension codes "3D" "Spatial" " Network"
#Gina Fonseca
#Chapter 5 Challenge 04

from arcpy import env


env.worskapce = "C:/EsriPress/PythonData/Exercise05"

S = "" 
D = ""
N = ""

if arcpy.CheckExtension("Spatial") == "Available": #this one checks for spatial
		S = "Spatial Analyst"
		

if arcpy.CheckExtension("3D") == "Available": #this statement checks for 3D
		D = "3D Analyst"

		
if arcpy.CheckExtension("Network") == "Available": #this statemnent checks for network
		N = " Network Analyst"

print "The following license have been checked and are available: "  +  S  +  N  +  D
