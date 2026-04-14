import random

# Define the three templates as strings with placeholders
template1 = "It was about {} {} ago when I arrived at the hospital in a {}. The hospital is a/an {} place, there are a lot of {} {} here. There are nurses here who have {} {}. If someone wants to come into my room I told them that they have to {} first. I’ve decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. I heard that all doctors {} {} every day for breakfast. The most {} thing about being in the hospital is the {} {}!"

template2 = "This weekend I am going camping with {}. I packed my lantern, sleeping bag, and {}. I am so {} to {} in a tent. I am {} we might see a(n) {}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {}. I have heard that the {} lake is great for {}. Then we will {} hike through the forest for {} {}. If I see a {} {} while hiking, I am going to bring it home as a pet! At night we will tell {} {} stories and roast {} around the campfire!!"

template3 = "Dear {}, I am writing to you from a {} castle in an enchanted forest. I found myself here one day after going for a ride on a {} {} in {}. There are {} {} and {} {} here! In the {} there is a pool full of {}. I fall asleep each night on a {} of {} and dream of {} {}. It feels as though I have lived here for {} {}. I hope one day you can visit, although the only way to get here now is {} on a {} {}!!"

print("--- Welcome to the Mad Libs Generator ---")
print("Choose a template:")
print("1. The Hospital Visit")
print("2. Camping Trip")
print("3. Enchanted Castle")
print("4. Random Choice")

choice = input("Enter choice (1-4): ")

# Handle the random choice logic
if choice == "4":
    choice = str(random.randint(1, 3))

# Logic for Template 1
if choice == "1":
    num = input("Type a number: ")
    time = input("Type a measure of time: ")
    transport = input("Type a mode of transportation: ")
    adj1 = input("Type an adjective: ")
    adj2 = input("Type another adjective: ")
    noun1 = input("Type a noun: ")
    color = input("Type a color: ")
    body = input("Type a part of the body: ")
    verb1 = input("Type a verb: ")
    num2 = input("Type a second number: ")
    noun2 = input("Type a second noun: ")
    noun3 = input("Type a third noun: ")
    body2 = input("Type another part of the body: ")
    verb2 = input("Type a second verb: ")
    noun4 = input("Type a fourth noun: ")
    adj3 = input("Type a third adjective: ")
    silly = input("Type a silly word: ")
    noun5 = input("Type a fifth noun: ")
    
    print("\n--- YOUR STORY ---")
    print(template1.format(num, time, transport, adj1, adj2, noun1, color, body, verb1, num2, noun2, noun3, body2, verb2, noun4, adj3, silly, noun5))

# Logic for Template 2
elif choice == "2":
    p_noun = input("Type a Person's Name: ")
    noun1 = input("Type a noun: ")
    feel1 = input("Type an adjective (feeling): ")
    verb1 = input("Type a verb: ")
    feel2 = input("Type another adjective (feeling): ")
    animal1 = input("Type an animal: ")
    verb2 = input("Type a second verb: ")
    color1 = input("Type a color: ")
    verb_ing = input("Type a verb ending in 'ing': ")
    adverb = input("Type an adverb (ending in 'ly'): ")
    num = input("Type a number: ")
    time = input("Type a measure of time: ")
    color2 = input("Type another color: ")
    animal2 = input("Type another animal: ")
    num2 = input("Type a second number: ")
    silly = input("Type a silly word: ")
    noun2 = input("Type a second noun: ")
    
    print("\n--- YOUR STORY ---")
    print(template2.format(p_noun, noun1, feel1, verb1, feel2, animal1, verb2, color1, verb_ing, adverb, num, time, color2, animal2, num2, silly, noun2))

# Logic for Template 3
elif choice == "3":
    p_noun = input("Type a Person's Name: ")
    adj1 = input("Type an adjective: ")
    color1 = input("Type a color: ")
    animal1 = input("Type an animal: ")
    place = input("Type a place: ")
    adj2 = input("Type a second adjective: ")
    magic1 = input("Type a magical creature (plural): ")
    adj3 = input("Type a third adjective: ")
    magic2 = input("Type another magical creature (plural): ")
    room = input("Type a room in a house: ")
    noun1 = input("Type a noun: ")
    noun2 = input("Type a second noun: ")
    noun_p1 = input("Type a noun (plural): ")
    adj4 = input("Type a fourth adjective: ")
    noun_p2 = input("Type another noun (plural): ")
    num = input("Type a number: ")
    time = input("Type a measure of time: ")
    verb_ing = input("Type a verb ending in 'ing': ")
    adj5 = input("Type a fifth adjective: ")
    noun3 = input("Type a third noun: ")
    
    print("\n--- YOUR STORY ---")
    print(template3.format(p_noun, adj1, color1, animal1, place, adj2, magic1, adj3, magic2, room, noun1, noun2, noun_p1, adj4, noun_p2, num, time, verb_ing, adj5, noun3))

else:
    print("Invalid selection. Please run the program again.")
