
#http://openweathermap.org/
#Key- 4cb1057e0ebe754b303b3ddc2c3c6bc5

#import stuff
import time
import json, requests
global zipcode

#welcome message
print("Welcome to the Weather Checker Program!")

time.sleep(1)

print("In this program, you can enter a US zip code to find out what the weather in that location!")

#get zip and confirm its valid or tell the user if not
while True:
  try:
    zipcode = int(input("Enter the zip code: "))
  except ValueError:
    print ("Error! Only numbers are allowed.")
  if zipcode < 1:
    print ("Error! Only valid 5 digit zip codes are allowed.")
  elif zipcode > 99999:
    print ("Error! Only valid 5 digit zip codes are allowed.")
  #ADD SOMETHING TO CHECK FOR API FAILURE RESPONSES
  #ADD SOMETHING TO CONFIRM ZIP IS VALID FROM API
  else:
    break    



#get weather details by zip
base_url = "https://api.openweathermap.org/data/2.5/weather?"
apikey = "4cb1057e0ebe754b303b3ddc2c3c6bc5"
countrycode = "us"
units = "imperial"
url = f"{base_url}zip={zipcode},{countrycode}&appid={apikey}&units={units}"

#define jsons data
response = requests.get(url)
unformated_data = response.json()

#define and display temp and city info
currentTemp = unformated_data['main']["temp"]
tempmin = unformated_data['main']["temp_min"]
tempmax = unformated_data['main']["temp_max"]
city = unformated_data['name']
print("The current temp in",(city), "is:", (currentTemp),"F")
print("The min temp today will be:",(tempmin),"F")
print("The max temp today will be:",(tempmax),"F")