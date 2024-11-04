# 🤖 NPC Generator

## 📚 Table of Contents

- [Features](#-features)
- [Overview](#-overview)
- [Attributes](#-attributes)
- [Author](#-author)
- [Code Example](#-code-example)
- [Installation](#-installation)
- [Requirements](#-requirements)
- [Feedback and Contributing](#feedback-and-contributing)

## 📋 Features

- Asks the user how many NPCs they would like to generate
- Asks the user what they want the NPC names to be
- Generates 15 other [attributes](#-attributes) for each NPC

## 📜 Overview

The NPC Generator was created for a school project, and generates NPCs with attributes such as age, height, weight, strength, IQ, race, personality, occupation, the sport they play, their favorite specific float, if they are related to Gerald, if they play ROBLOX, if they are in the thick of it, if they are eamon, and how they like their cheese. Some atributes like "robloxplayer" or "inthethickofit" are more gimicky or jokey, but you can use whatever atributes you wish for your NPCs. To see how they're gotten, check [attributes](#-attributes). This can be used for any project that may need NPCs (or just characters in general), wether it be a video game, artwork, or a book, though it was mainly designed with an open world game in mind. This is capable of making hundreds of different NPCs developers can use in their projects, allowing the user to chose what names the NPCs will have. Some atributes like "strength" are more rpg or open world based while others like "age" or "height" can be used in mostly any type of media. 

## 🛒 Attributes

- The "name" variable is chosen from the "names" list that all of the user inputed names are appended.
```python
while len(names) < count:
    names.append(input("Enter an NPC name: "))
```
- The "age" variable is a random number between 1 and 100.
```python
 age = random.randint(1, 100)
```
- The height is a combination of the "feet" and "inches" variables. Feet is a random number between 2 and 6 while inches is a random number between 0 and 11.
```python
feet = random.randint(2, 6)
    inches = random.randint(0, 11)
```
- The "weight" variable is a random number between 80 and 300.
```python
weight = random.randint(80,  300)
```
- The "strength" variable is a random number between 1 and 500. It is made as a point value for potential enemy NPCs.
```python
strength = random.randint(1, 500)
```
- The "IQ" variable is a random number between 80 and 160.
```python
iq = random.randint(80, 160)
```
- The "race", "personality", "occupation", and "sport" variables are chosen from four [lists](https://www.w3schools.com/python/python_lists.asp). Below shows the three lists in the code. 

```python
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

race = random.choice(potential_race)
    
personality = random.choice(potential_personality)
    
occupation = random.choice(potential_occupation)
    
sport = random.choice(potential_sport)
    
```

- The "geraldrelation", "inthethickofit", and "eamon" variables all use [.find](https://www.w3schools.com/python/ref_string_find.asp) to figure out if the name contains "Gerald" (geraldrelation), "KSI" (inthethickofit), and "Eamon" (eamon).

```python
geraldrelation = name.find("Gerald")
    if geraldrelation == -1:
        geraldrelation == False
    else:
        geraldrelation == True
        
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
```

If the name does contain the certain word, the variable will be the index of where the word appears. If it is not there, the varialbe will be -1 as the world never shows up. We can then change the variable to False if it is equal to -1 and true if otherwise.

- The "specificno" variable is a random float.
```python
specificno = random.random()
``` 
- The "robloxplayer" variable is a random number between 1 and 10, and if the number is 1 the variable is True. Otherwise, it's false.
```python
robloxplayer = random.randint(1, 10)
    if robloxplayer == 1:
        robloxplayer == True
    else:
        robloxplayer == False
```
- The "cheese" variable is a random number between 1 and 17. If the number is less than 6, the variable is set to 1 (later drippy). If it's less than 11 but more than 6, the variable is set to 2 (later moldy). If the number is more than 11, the variable is set to 3 (later normal).
```python
 cheese = random.randint(1, 17)
    if cheese < 6:
        cheese = 1
    elif cheese < 11:
        cheese = 2
    elif cheese > 11:
        cheese = 3
```

## 👨‍💻 Author

Me, "Stegss" who likes learning to code. I've found Python very interesting so far, and this project was pretty fun to make. I enjoyed puting some silly ideas into the generator and think this could actually be used to generate tons of NPCs for whatever if integrated correctly. [Github](https://github.com/Stegss)

## 💻 Code Example

Here is an example of a program output:

```python
How many NPCs do you wish to make? 1 # user inputed the 1                                            
Enter an NPC name: Stegss # user inputed the "Stegss"
Name: Stegss                                                                    
 Age: 9                                                                         
 Height: 4 Feet 8 Inches                                                        
 Weight: 133 LBS                                                                
 Strength: 68                                                                   
 IQ: 155                                                                        
 Race: Korean                                                                   
 Personality: Passionate                                                        
 Occupation: Florist                                                            
 Sport: Diving                                                                  
 Likes this veryyy SPECIFIC number: 0.18368189824270897                         
 Is NOT related to Gerald                                                       
 Is NOT a ROBLOX player                                                         
 Stegss is NOT in the thick of it                                               
 Stegss IS NOT Eamon                                                            
 Stegss likes their cheese moldy bruh
```
## ✅ Installation 

1. **Fork the repo** on GitHub.
2. **Clone your fork**:

   ```bash
   git clone https://github.com/Stegss/NPCGenerator.git
   ```

### 📝 Requirements

- macOS 10.15 or later
- Windows 10 64-bit or later. You must have a 64-bit operating system to run GitHub Desktop.
- [More information](https://docs.github.com/en/desktop/overview/supported-operating-systems-for-github-desktop)

## Feedback and Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

