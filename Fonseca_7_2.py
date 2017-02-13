#Write a script that adds a text field to the roads.shp feature class called
#FERRY and populates this field with YES and NO values, depending on
#the value of the FEATURE field.

#Gina Fonseca 
#Lab3

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
fc = "roads.shp" #the shp I want to modify
newfield = "FERRY" #name of the new field I wanna add on the atributte table
fieldtype = "TEXT" #type of information that it will have
fieldname = arcpy.ValidateFieldName(newfield) 
arcpy.management.AddField(fc, fieldname, fieldtype, "","",12)


cursor = arcpy.da.UpdateCursor(fc,["FERRY", "FEATURE"]) #we use Update CUrsos because  we need to add/delete the new field
# This populates the fields with Yes or No
for row in cursor:
	if row[1] == "Ferry Crossing":
		row[0] = "Yes"
		cursor.updateRow(row)
		print "Yes it has Ferry Crossing" # I put the print here and in else just for my own personal feedback while waiting 
	else:
		row[0] = "No"
		cursor.updateRow(row)
		print "Does not have Ferry Crossing"

del row #Removes locks without it it could block other applications from accessing the dataset.
del cursor
