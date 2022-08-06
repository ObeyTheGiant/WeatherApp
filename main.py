#http://openweathermap.org/
#Key- 4cb1057e0ebe754b303b3ddc2c3c6bc5

#import stuff
import time
import json, requests
global zipcode

#welcome message
print("Welcome to the Weather Checker Program!")

time.sleep(1)

print(
    "In this program, you can enter a US zip code to find out what the weather in that location!"
)


def main():
    #get zip and confirm its valid or tell the user if not

    zipcode = int(input("Enter the zip code: "))
    if zipcode < 1:
        print("Error! Only valid 5 digit zip codes are allowed.")
    if zipcode > 99999:
        print("Error! Only valid 5 digit zip codes are allowed.")
        badZip = input(
            "The zip you entered is invalid, would you like to try again? (y or n)"
        )
        if badZip == "y":
            main()
        if badZip == "n":
            exit

#get weather details by zip
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    apikey = "4cb1057e0ebe754b303b3ddc2c3c6bc5"
    countrycode = "us"
    units = "imperial"
    url = f"{base_url}zip={zipcode},{countrycode}&appid={apikey}&units={units}"
    response = requests.get(url)
    unformated_data = response.json()
    responseCode = response.status_code
    print("API Response code:", responseCode)
    #tell user if API response is bad
    if responseCode == 400:
        error400 = input("You entered a wrong zip, try again? (y or n): ")
        if error400 == "y":
            main()
        if error400 == "n":
            print("Adios!")
            exit()
    elif responseCode == 500:
        print(
            "The API to check the weather is currently down.  Try again later."
        )
        error500 = input("You entered a wrong zip, try again? (y or n): ")
        if error500 == "y":
            main()
        if error500 == "n":
            print("Adios!")
            exit()


#display weather details from json
    else:
        currentTemp = unformated_data['main']["temp"]
        tempmin = unformated_data['main']["temp_min"]
        tempmax = unformated_data['main']["temp_max"]
        city = unformated_data['name']
        print("The current temp in", (city), "is:", (currentTemp), "F")
        print("The min temp today will be:", (tempmin), "F")
        print("The max temp today will be:", (tempmax), "F")

main()

while True:
    restartApp = input('Do you want to check another zip? (y or n):')
    if restartApp.lower().startswith("y"):
        main()
    if restartApp.lower().startswith("n"):
        print("Thanks for using the app!")
        exit()
