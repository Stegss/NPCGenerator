import random

# Define the "names" list
names = []

# Defines 3 lists full of atributes
potential_race = ["American Indian/Alaska Native", "Asian, Black", "African American", "Native Hawaiian", "Pacific Islander", "White, African", "Caribbean",
"Indian", "Melanesian", "Australasian/Aboriginal", "Chinese", "Guamanian", "Japanese", "Korean", "Polynesian", "European/Anglo Saxon", "Other Pacific Islander", "Latin American",
"Arabic", "Vietnamese", "Micronesian"]
potential_personality = ["Adaptable", "Adventurous", "Affectionate", "Agreeable", "Ambitious", "Analytical", "Artistic", "Assertive", "Attentive", "Authentic",
"Balanced", "Bold", "Brave", "Calm", "Caring", "Charming", "Cheerful", "Compassionate", "Confident", "Considerate",
"Cooperative", "Courageous", "Creative", "Curious", "Dependable", "Determined", "Diligent", "Discreet", "Empathetic", "Enthusiastic",
"Friendly", "Generous", "Gentle", "Genuine", "Gracious", "Happy", "Hardworking", "Honest", "Humorous", "Imaginative",
"Impartial", "Independent", "Innovative", "Inquisitive", "Insightful", "Inspiring", "Intuitive", "Joyful", "Kind", "Loyal",
"Meticulous", "Motivated", "Nurturing", "Optimistic", "Open-minded", "Organized", "Passionate", "Patient", "Perceptive", "Persuasive",
"Playful", "Polite", "Practical", "Proactive", "Punctual", "Realistic", "Reliable", "Resilient", "Respectful", "Responsible",
"Romantic", "Self-aware", "Sincere", "Sociable", "Spontaneous", "Supportive", "Sympathetic", "Tactful", "Tenacious", "Thoughtful",
"Trustworthy", "Understanding", "Unconventional", "Valiant", "Vibrant", "Warm", "Witty", "Wise", "Zany", "Zealous"]
potential_occupation = ["Doctor", "Engineer", "Teacher", "Artist", "Nurse", "Chef", "Plumber", "Electrician", "Pilot", "Writer",
"Architect", "Scientist", "Mechanic", "Lawyer", "Graphic Designer", "Software Developer", "Pharmacist",
"Journalist", "Musician", "Data Analyst", "Veterinarian", "Accountant", "Web Developer", "Salesperson",
"Psychologist", "Carpenter", "Fashion Designer", "Social Worker", "Firefighter", "Construction Worker",
"Marketing Specialist", "Researcher", "Optometrist", "Real Estate Agent", "Historian", "Statistician",
"Barista", "Florist", "Photographer", "Translator", "Security Guard", "Web Designer", "Dental Hygienist",
"Waiter", "Baker", "Custodian", "Occupational Therapist", "Insurance Agent", "Pilot", "Fitness Trainer",
"Electrician", "Chemist", "Film Director", "Public Relations Specialist", "Event Planner", "Software Engineer",
"Entrepreneur", "Logistician", "Quality Control Inspector", "Speech Therapist", "Urban Planner", "Biologist"]
potential_sport = ["Basketball", "Soccer", "Tennis", "Baseball", "Football", "Hockey", "Volleyball", "Golf", "Rugby", "Cricket",
"Swimming", "Athletics", "Cycling", "Table Tennis", "Badminton", "Gymnastics", "Wrestling", "Boxing", "Martial Arts", "Surfing",
"Skateboarding", "Snowboarding", "Rock Climbing", "Rowing", "Skiing", "Lacrosse", "Field Hockey", "Fencing", "Handball", "Softball",
"Rugby Sevens", "Ultimate Frisbee", "Diving", "Sailing", "Canoeing", "Triathlon", "Motor Racing", "Horse Racing", "Snooker", "Darts",
"Water Polo", "Billiards", "Archery", "Powerlifting", "Weightlifting", "CrossFit", "Pilates", "Yoga", "Cheerleading", "Cricket",
"Speed Skating", "Ice Climbing", "Aerial Skiing", "Biathlon", "Skeleton", "Luge", "Bobsleigh", "Parkour", "Slacklining", "Kitesurfing",
"Freestyle Wrestling", "Judo", "Taekwondo", "Karate", "Capoeira", "Surf Lifesaving", "Dragon Boat Racing", "Curling", "Australian Rules Football", "Sepak Takraw", "Underwater Basket Weaving"]

# Asks the user how many NPCs they want to make
count = int(input("How many NPCs do you wish to make? "))

# Repeats asking the user for a name depending on how many NPCs they wanted to make
while len(names) < count:
    names.append(input("Enter an NPC name: "))

# Randomly generates or checks for certain atributes
for i in names:
    name = random.choice(names)
    
    age = random.randint(1, 100)
    
    feet = random.randint(2, 6)
    inches = random.randint(0, 11)
    
    weight = random.randint(80,  300)
    
    strength = random.randint(1, 500)
    
    specificno = random.random()
    
    iq = random.randint(80, 160)
    
    # following four take from the previous lists
    race = random.choice(potential_race)
    
    personality = random.choice(potential_personality)
    
    occupation = random.choice(potential_occupation)
    
    sport = random.choice(potential_sport)
    
    # Following geraldrelation, inthethickofit, and eamon all check for if the name variable has a certain word inside
    geraldrelation = name.find("Gerald")
    if geraldrelation == -1:
        geraldrelation == False
    else:
        geraldrelation == True
        
    robloxplayer = random.randint(1, 10)
    if robloxplayer == 1:
        robloxplayer == True
    else:
        robloxplayer == False
        
    inthethickofit = name.find("KSI")
    if inthethickofit == -1:
        inthethickofit == False
    else:
        inthethickofit == True
        
    eamon = name.find("Eamon")
    if eamon == -1:
        eamon == False
    else:
        eamon == True
    
    cheese = random.randint(1, 17)
    if cheese < 6:
        cheese = 1
    elif cheese < 11:
        cheese = 2
    elif cheese > 11:
        cheese = 3
    
    # Prints the NPC atributes
    print("Name:", name, "\n",
    "Age:", age, "\n",
    "Height:", feet, "Feet", inches, "Inches", "\n",
    "Weight:", weight, "LBS", "\n",
    "Strength:", strength, "\n",
    "IQ:", iq, "\n",
    "Race:", race, "\n",
    "Personality:", personality, "\n",
    "Occupation:", occupation, "\n",
    "Sport:", sport, "\n",
    "Likes this veryyy SPECIFIC number:", specificno)
    if geraldrelation == False:
        print(" Is related to Gerald")
    else:
        print(" Is NOT related to Gerald")
    if robloxplayer == True:
        print(" Is indeed a ROBLOX player")
    else:
        print(" Is NOT a ROBLOX player")
    if inthethickofit == False:
        print("", name, "IS in the thick of it. Everybody knows")
    else:
        print("", name, "is NOT in the thick of it")
    if eamon == False:
        print("", name, "IS Eamon")
    else:
        print("", name, "IS NOT Eamon")
    if cheese == 1:
        print("", name, "likes their cheese drippy bruh")
    elif cheese == 2:
        print("", name, "likes their cheese moldy bruh")
    else:
        print("", name, "likes their cheese normal bruh\n")
    
    
    
    
    
    
    
