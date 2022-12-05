def learn():
    DataSet = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne",
    }
    user = input("Please enter a US state: ")

    if user in DataSet:
        print(DataSet[user])
    else:
        print("No such state in the USA. Please enter a valid state.")


learn()

"""

renamed function to learn(),
renamed variable containing input(),
removed .keys() method and switched to syntax that iterates dirrectly through dictionary,
verified that function works.

Need to do:
welcome message,
format answer into a full sentence instead of one word,
how to restart app if user inputs invalid state i.e., how to prompt input line to run again.
create def main() best practices
"""


# def welcome_message():
#     print("Welcome to U.S.A State Capitals!")
#     print("Enter the name of a U.S. state to learn its capital.")


# def main():
#     welcome_message()
