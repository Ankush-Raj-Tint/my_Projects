import csv
from bs4 import BeautifulSoup
import html5lib
import requests
from datetime import datetime
import pytz




def current_date_time(country_time_zone):

    country_time_zone = pytz.timezone(country_time_zone)
    country_time = datetime.now(country_time_zone)
    print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))





def Advices():

    url = "https://www.forbes.com/sites/laurabegleybloom/2019/08/27/17-things-you-should-never-do-in-europe/?sh=6772a43d5884"
    responseObj = requests.get(url)

    # print(responseObj.content)
    soup = BeautifulSoup(responseObj.content, 'html.parser')
    # print(soup.prettify())

    advicesList = []  # list

    table = soup.find_all('p')
    # print(table)

    for row in table:

        temp = []

        temp.append(row.text)
        advicesList.append(temp)


    i = 8
    while(i < len(advicesList)):
        print(advicesList[i])
        print('\n')
        i += 1
        if i == len(advicesList)-5:
            break




def travelAdvisiory():

    url = "https://www.euronews.com/travel/2022/03/18/what-s-the-latest-on-european-travel-restrictions"
    responseObj = requests.get(url)

    soup = BeautifulSoup(responseObj.content, 'html5lib')

    #print(soup.prettify())

    table = soup.find_all('p')
    info = []

    for item in table:
    
        temp = []
        temp.append(item.text)
        info.append(temp)

    for item in range(2, len(info)-203):
        print(info[item])
        print('\n')






# DRIVER CODE STARTS

print("Shall we find the Date and Time ?")
val = input("Enter 'y' for yes and 'n' for no \n")
keep_going = True

while keep_going == True:

    if val == "y":
        zone_format = input(
        "Enter in the format (camel case) -> Continent/City \n")

        found = False

        for item in pytz.all_timezones:
            if item == zone_format:
                # we are good to go.
                found = True
                current_date_time(zone_format)

        if found == False:
            print("Wrong format or Zone not available")
            print("Please enter again.")

        if found == True:
            val = input(
            "Do you want to know the date and time of any other place ? Enter yes or no! \n")

        if val == "y":
            keep_going = True
        else:
            keep_going = False

    elif val!="y" and val!="n":
        print("wrong input recieved!!")
        print("please try again")
        val = input("Enter 'y' for yes and 'n' for no\n")
        if val=="y":
            keep_going = True
        else:
            keep_going=False
    
    else:
        keep_going=False







print('\n')
print("Want to know about some Do's and Dont's in Europe?")

val = input("Enter 'y' for yes and 'n' for no \n")
print('\n')

keep_going = True

while(keep_going==True):
    if val == "y":
        Advices()
        keep_going = False

    elif val == "n":
        keep_going = False

    else:
        print("Invalid Input! Please try again.")
        val = input("Enter 'y' for yes and 'n' for no \n")
        keep_going = True







print('\n')
print("Would You like to see the 'Latest European Travel Restrictions ?")

val = input("Enter 'y' for yes and 'n' for no \n")
print('\n')

keep_going = True

while(keep_going==True):
    if val == "y":
        travelAdvisiory()
        keep_going = False

    elif val == "n":
        keep_going = False

    else:
        print("Invalid Input! Please try again.")
        val = input("Enter 'y' for yes and 'n' for no \n")
        keep_going = True