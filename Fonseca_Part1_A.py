#Gina Fonseca
#Lab4

#Write a script that copies all the rasters in a workspace to a new file geodatabase.
#You can use the rasters in the Exercise09 folder as an example.



import arcpy
from arcpy import env

#Overwrite in case it fails
arcpy.env.overwriteOutput = True

#Work Area 
env.workspace = "C:\EsriPress\Python\Data\Exercise09"


#Path for my new GDB
Out_Raster = ("C:\EsriPress\Python\Data\Exercise09\MyRadRasters.gdb")


#Creates GDB
arcpy.CreateFileGDB_management("C:\EsriPress\Python\Data\Exercise09", "MyRadRasters.gdb")
		
#variable that looks for all rasters and lists them 
listras = arcpy.ListRasters() # the parenthesis is empyt because I want to copy all files no matter the type.


#Loop that takes the list of rasters and copys them to new GDB 
for raster in listras :
	arcpy.CopyRaster_management(raster,Out_Raster + '/' + arcpy.Describe(raster).basename,"Defaults") #here is exactly where the copying happens


print " Task complete! "
# 
    	

