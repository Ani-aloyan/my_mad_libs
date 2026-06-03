import random

# Define the three templates as strings with placeholders
template1 = "It was about {} {} ago when I arrived at the hospital in a {}. The hospital is a/an {} place, there are a lot of {} {} here. There are nurses here who have {} {}. If someone wants to come into my room I told them that they have to {} first. I’ve decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. I heard that all doctors {} {} every day for breakfast. The most {} thing about being in the hospital is the {} {}!"

template2 = "This weekend I am going camping with {}. I packed my lantern, sleeping bag, and {}. I am so {} to {} in a tent. I am {} we might see a(n) {}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {}. I have heard that the {} lake is great for {}. Then we will {} hike through the forest for {} {}. If I see a {} {} while hiking, I am going to bring it home as a pet! At night we will tell {} {} stories and roast {} around the campfire!!"

template3 = "Dear {}, I am writing to you from a {} castle in an enchanted forest. I found myself here one day after going for a ride on a {} {} in {}. There are {} {} and {} {} here! In the {} there is a pool full of {}. I fall asleep each night on a {} of {} and dream of {} {}. It feels as though I have lived here for {} {}. I hope one day you can visit, although the only way to get here now is {} on a {} {}!!"

print("--- Welcome to the Mad Libs Generator ---")

# Error Handling: Loop until the user provides a valid choice (1-4)
while True:
    print("\nChoose a template:")
    print("1. The Hospital Visit")
    print("2. Camping Trip")
    print("3. Enchanted Castle")
    print("4. Random Choice")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice in ("1", "2", "3", "4"):
        break # Valid input received, exit the menu loop
    else:
        print("❌ Invalid selection. Please enter a number between 1 and 4.")

# Handle the random choice logic
if choice == "4":
    choice = str(random.randint(1, 3))
    print(f"🎲 Randomly selected Template {choice} for you!")

# Helper function to ensure inputs aren't left entirely blank
def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("⚠️ Input cannot be empty. Please type something!")

# Logic for Template 1
if choice == "1":
    num = get_input("Type a number: ")
    time = get_input("Type a measure of time: ")
    transport = get_input("Type a mode of transportation: ")
    adj1 = get_input("Type an adjective: ")
    adj2 = get_input("Type another adjective: ")
    noun1 = get_input("Type a noun: ")
    color = get_input("Type a color: ")
    body = get_input("Type a part of the body: ")
    verb1 = get_input("Type a verb: ")
    num2 = get_input("Type a second number: ")
    noun2 = get_input("Type a second noun: ")
    noun3 = get_input("Type a third noun: ")
    body2 = get_input("Type another part of the body: ")
    verb2 = get_input("Type a second verb: ")
    noun4 = get_input("Type a fourth noun: ")
    adj3 = get_input("Type a third adjective: ")
    silly = get_input("Type a silly word: ")
    noun5 = get_input("Type a fifth noun: ")
    
    print("\n--- YOUR STORY ---")
    print(template1.format(num, time, transport, adj1, adj2, noun1, color, body, verb1, num2, noun2, noun3, body2, verb2, noun4, adj3, silly, noun5))

# Logic for Template 2
elif choice == "2":
    p_noun = get_input("Type a Person's Name: ")
    noun1 = get_input("Type a noun: ")
    feel1 = get_input("Type an adjective (feeling): ")
    verb1 = get_input("Type a verb: ")
    feel2 = get_input("Type another adjective (feeling): ")
    animal1 = get_input("Type an animal: ")
    verb2 = get_input("Type a second verb: ")
    color1 = get_input("Type a color: ")
    verb_ing = get_input("Type a verb ending in 'ing': ")
    adverb = get_input("Type an adverb (ending in 'ly'): ")
    num = get_input("Type a number: ")
    time = get_input("Type a measure of time: ")
    color2 = get_input("Type another color: ")
    animal2 = get_input("Type another animal: ")
    num2 = get_input("Type a second number: ")
    silly = get_input("Type a silly word: ")
    noun2 = get_input("Type a second noun: ")
    
    print("\n--- YOUR STORY ---")
    print(template2.format(p_noun, noun1, feel1, verb1, feel2, animal1, verb2, color1, verb_ing, adverb, num, time, color2, animal2, num2, silly, noun2))

# Logic for Template 3
elif choice == "3":
    p_noun = get_input("Type a Person's Name: ")
    adj1 = get_input("Type an adjective: ")
    color1 = get_input("Type a color: ")
    animal1 = get_input("Type an animal: ")
    place = get_input("Type a place: ")
    adj2 = get_input("Type a second adjective: ")
    magic1 = get_input("Type a magical creature (plural): ")
    adj3 = get_input("Type a third adjective: ")
    magic2 = get_input("Type another magical creature (plural): ")
    room = get_input("Type a room in a house: ")
    noun1 = get_input("Type a noun: ")
    noun2 = get_input("Type a second noun: ")
    noun_p1 = get_input("Type a noun (plural): ")
    adj4 = get_input("Type a fourth adjective: ")
    noun_p2 = get_input("Type another noun (plural): ")
    num = get_input("Type a number: ")
    time = get_input("Type a measure of time: ")
    verb_ing = get_input("Type a verb ending in 'ing': ")
    adj5 = get_input("Type a fifth adjective: ")
    noun3 = get_input("Type a third noun: ")
    
    print("\n--- YOUR STORY ---")
    print(template3.format(p_noun, adj1, color1, animal1, place, adj2, magic1, adj3, magic2, room, noun1, noun2, noun_p1, adj4, noun_p2, num, time, verb_ing, adj5, noun3))
