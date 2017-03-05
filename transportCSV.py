from cartodb import CartoDBAPIKey, CartoDBException, FileImport # these are your essentials so you can transport your csv to Carto

#configurations 
API_KEY ='Here you write your API key'
cartodb_domain = 'HEREYOUWRITEYOUR DOMAIN' #when you create your carto account in your settings you can obtain this info
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
 
#import csv write the path 
fi = FileImport("C://Tweets.csv", cl) #note it is important to chekc that when you install carto you have your File import for some reason when i originally ran it did not have it.
 
fi.run()