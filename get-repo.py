# Import Libraries
import requests
from num import test_num
from sys import exit
import time

# Function to fetch User data 
def repo_info(user):

    # Access Repos of that User [If exists]
    url = f"https://api.github.com/users/{user}/repos"

    # Get JSON
    user_data = requests.get(url).json()

    # Return list
    return user_data

# Function to fetch repo contents
def repo_contents(repo_user, repo_name):

    # Access repo contents of provided username
    url = f"https://api.github.com/repos/{repo_user}/{repo_name}/contents"

    # Get JSON 
    repo = requests.get(url).json()

    # Return list
    return repo

# Get Username
username = input("\nGitHub Username: ")

# Get All data from function
user_repos = repo_info(username)

# If no data found, Exit the program [unsuccessfully]
if user_repos == None:

    print("\nNo USER found!\n")
    exit(1)

# List to store repo names
repo_names = []

# Repo counter
i = 1

time.sleep(2)

print("\n===============================")
print("      LIST OF REPOSITORIES")
print("=================================\n")

# Iterate row by row inside list
for row in user_repos:

    # Store repo name in list
    repo_names.append(row['name'])

    # Print repo data
    print("\nRepo No. : ", i)
    print("Repo Name: ", row['name'])
    print("Last Updated: ", row['updated_at'])
    print("Repo URL: ", row['html_url'])
    print("Private: ", row['private'])
    print("Created at: ", row['pushed_at'])
    print("===================================\n")

    i += 1

    time.sleep(1)

print("\nWhich Repo you want to open ?")

# Keep prompting until user exits
while (True):

    # Ask for repo no
    repo_no = input("\nEnter Repo No: ")

    # Check for correct input
    check = test_num(repo_no)

    # If correct repo no is given
    if check == True and int(repo_no) <= i - 1 and int(repo_no) > 0:
        
        # Extract repo name from the list
        name = repo_names[int(repo_no) - 1]

        # Call function to get all repo contents
        user_repos_contents = repo_contents(username, name)
        
        time.sleep(2)

        # Print all repo contents
        print("\n================================")
        print("          REPO CONTENTS")
        print("==================================\n")

        no = 1

        # Iterate through list
        for row in user_repos_contents:

            print(no, row['name'])
            print("  URL: ", row['html_url'], "\n")
            no += 1
            time.sleep(1)

        print("\n")

        # Ask to continue
        while (True):

            ask = input("Exit [Y/N]: ")

            # If "YES", exit the program successfully
            if ask.lower() == "yes" or ask.lower() == "y":

                print(f"\nThankyou! {username}")
                exit(0)

            # Else break the loop
            if ask.lower() == "n" or ask.lower() == "no":
                break
            
            # If not correct option is given
            print("\nEnter Correct Option!\n")

    # If not correct repo no is given
    else:
        print(f"\nPlease Enter Correct Repo no. [1 - {i - 1}]\n")
