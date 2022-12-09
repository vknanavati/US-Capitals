def welcome_message():
    print("\nWelcome to Capitals of the United States!")
    print("Enter a US state below to learn it's capital.")


welcome_message()


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
    while True:
        user = input("\nState: ").title()
        if user not in DataSet:
            print("\nOops! Not a valid state, please try again.\n")
            continue
        else:
            print("\n" + user + "'s capital is: " + DataSet[user] + ".")

        choice = input(
            "\nWould you like to learn another capital? Type Y for 'yes' and N for 'no': "
        ).capitalize()
        if choice == "Y":
            continue
        else:
            break
    print("\nThank you for visiting US State Capitals. Come back soon!")


learn()


# Formatted spacing between lines with \n
# Changed wording of prompts

# Questions for Sebby-is that too much to put in one definition? serparate def for closing message?

# Need to do:
# create def main() best practices
# create def goodbye message


# while True:
#         user = input("Please enter US State: ").title()
#         if user not in DataSet:
#             print("\nNot a valid state try again.\n")
#             continue
#         else:
#             break
#     print(user + "'s capital is: " + DataSet[user] + ".")
