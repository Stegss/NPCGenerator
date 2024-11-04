# 🤖 NPC Generator

## 📚 Table of Contents

- [Features](#-features)
- [Overview](#-overview)
- [Author](#-author)
- [Code Example](#-code-example)
- [Installation](#-installation)
- [Requirements](#-requirements)
- [Feedback and Contributing](#feedback-and-contributing)

## 📋 Features

- Asks the user how many NPCs they would like to generate
- Asks the user what they want the NPC names to be
- Generates 15 other attributes for each NPC

## 📜 Overview

The NPC Generator was created for a school project, and generates NPCs with attributes such as age, height, weight, strength, IQ, race, personality, occupation, the sport they play, their favorite specific float, if they are related to Gerald, if they play ROBLOX, if they are in the thick of it, if they are eamon, and how they like their cheese. This can be used for any project that may need NPCs (or just characters in general), wether it be a video game, artwork, or a book. This is capable of making hundreds of different NPCs developers can use in their projects, allowing the user to chose what names the NPCs will have.

### 📺 [Demonstration Video](youtube.com)

## Specifications

The "race", "personality", "occupation", and "sport" variables are chosen from four [lists](https://www.w3schools.com/python/python_lists.asp). Below shows the three lists in the code. 

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
```

The "geraldrelation", "inthethickofit", and "eamon" variables all use [.find](https://www.w3schools.com/python/ref_string_find.asp) to figure out if the name contains "Gerald" (geraldrelation), "KSI" (inthethickofit), and "Eamon" (eamon).

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

## 👨‍💻 Author

Me, "Stegss" who likes learning to code. I've found Python very interesting so far, and this project was pretty fun to make.

[My Github](https://github.com/Stegss)

## 💻 Code Example

Here is an example of an NPC output if the user asked for 1 NPC and inputed the name "Stegss":

```python
Name: Stegss                                                                    
 Age: 9                                                                         
 Height: 4 Feet 5 Inches                                                        
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
## Installation 

1. **Fork the repo** on GitHub.
2. **Clone your fork**:

   ```bash
   git clone https://github.com/Stegss/NPCgenerator.git
   ```

### Requirements

- macOS 10.15 or later
- Windows 10 64-bit or later. You must have a 64-bit operating system to run GitHub Desktop.
- [More information](https://docs.github.com/en/desktop/overview/supported-operating-systems-for-github-desktop)

## Feedback and Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

