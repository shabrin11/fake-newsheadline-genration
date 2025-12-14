#import the random module
import random
#create subjects
subjects = [
    "sharukh khan ",
    "virat kohli ",
    "nirmala sitharam",
    "a mombai cat",
    "a group of monkeys",
    "prime minister modi",
    "auto rikshaw driver from delhi"
]

actions = [
    "launches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]
places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL match",
    "at India gate"
]

#start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input=input("\n do you want another headline(yes/no)").strip().lower()
    if user_input == "no":
       break
#print goodbye message
print("thanks you for using fake news headline generation")
