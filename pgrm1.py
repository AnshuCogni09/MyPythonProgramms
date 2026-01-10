num_participants = int(input("Enter the number of participants: "))

if num_participants <= 0:
    print("Invalid Input")
    exit()

participant_prefs = {}
event_participants = {}

for i in range(num_participants):
    name = input("Enter participant name: ")
    email = input("Enter participant email: ")
    reg_date = input("Enter registration date (YYYY-MM-DD): ")
    preferences = input("Enter participant preferences separated by spaces (Workshop/Presentation/Hackathon/Quiz): ").split()

    participant_prefs[name] = preferences

    for event in preferences:

        if event not in event_participants:
            event_participants[event] = []

        event_participants[event].append(name)
    print()  

print("Registered Successfully!")
print("Participant Preferences:", participant_prefs)
print("Event Participants:", event_participants)


# My code starts here

# participant = int(input("Enter participant number: "))

# if(participant <= 0):
#     print("Invalid Input")
#     exit()

# for i in range(1, participant + 1):   
#     name = input("Enter participant name: ")
#     email = input("Enter participant email: ")
#     regd_dt = input("Enter registration date (YYYY-MM-DD): ")
#     preference = input("Enter participant preference separarted by spaces(Workshop/Presentation/hackathon/Quiz): ").split()

# dict_one = {name: [preference]}

# event_part = {preference: [name]}

# print("Participant Preference: ", dict_one)
# print("Event Participants: ", event_part)