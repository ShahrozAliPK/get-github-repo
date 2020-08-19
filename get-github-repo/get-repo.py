# PYTHON PROGRAM TO GET REPO DATA/INFO OF GITHUB USER (Developed By Syed Shehroz Ali) #

# Import Libraries
import requests
from pprint import pprint
from sys import exit

# Function to fetch User data 
def get_repo(user):

    # Access Repos of that User [If exists]
    url = f"https://api.github.com/users/{user}/repos"

    # Store all data in nested list
    user_data = requests.get(url).json()

    # Return All data
    return user_data


# Get Username
username = input("Enter Username: ")

# Get All data from function
data = get_repo(username)

# If no data found, Exit the program [unsuccessfully]
if data == None:

    print("\nNo USER found!\n")
    exit(1)

# Iterate row by row inside list
for row in data:

    # Get repo data
    print("\nRepo Name: ", row['full_name'])
    print("Last Updated: ", row['updated_at'])
    print("Repo URL: ", row['html_url'])
    print("Private: ", row['private'])
    print("Created at: ", row['pushed_at'])
    print("===================================\n")

# Exit Program successfully
exit(0)