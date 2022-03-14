import pandas as pd

import random

def user_interaction(picks): # Collects category and level of difficulty user inputs

    category = input('Pick a category: colors, math, ucsd, pets')
    
    difficulty = input('Pick a level of difficulty on a scale of 1 to 4')

    key = category + difficulty 
    
    
    if key in picks: # If statement below checks if the question has already been picked.
        print('This has already been answered, pick a new question.')
        user_interaction(picks)
    else:
        picks.append(key)
        
    return category, difficulty
        
def game_responce(category, difficulty, picks):
    
    colors = {'Questions': ['What color starts with R?',"What are UCSD's colors?", 'What is colors make purple?','What are the primary colors?'], 'Answers': ['Red','Blue and Yellow','Red and Blue','Red Yellow Blue'], 'A': ['Blue','Orange and Green','Orange and Green','Blue Orange Purple'], 'B': ['Green','Purple and Blue', 'Blue and Yellow', 'Red Yellow Orange']}
    colors = pd.DataFrame(colors)
    
    math = {'Questions': ["What is 2 + 3?","What is the square root of 25?", 'What makes calc 3 different from calc 1 & 2?','What is the quadratic formula?'], 'Answers': ['5','5','It is multidemensional','ax^2+bx+c=0'], 'A': ['2','6','It is not','m+b^2=0'], 'B': ['6','20', 'I dont know', 'a^2+b^2=c^2']}
    math = pd.DataFrame(math)
    
    ucsd = {'Questions': ["What is UCSD's mascott?","How many undergrad colleges does UCSD have?", 'What college makes you take the MMW series?','When was UCSD founded?'], 'Answers': ['A Triton','7','Eleanor Roosevelt','1960'], 'A': ['A Horn','6','Revelle','1864'], 'B': ['A Hammer','4', 'John Muir', '1999']}
    ucsd = pd.DataFrame(ucsd)
    
    pets = {'Questions': ['How many legs do dogs usually have?',"What is the most common house pet?", 'Do hamsters hibernate?',"What was ariel's pet friend in the little mermaid?"], 'Answers': ['4','Dog','Yes','Flounder'], 'A': ['3','Cat','No','Sordfish'], 'B': ['6','Cow', 'Maybe', 'Sebastian']}
    pets = pd.DataFrame(pets)

    difficulty = int(difficulty) - 1
    rad = randomize_list()

# If statement below, provides answers for the category chosen by user
    if category == 'math':
        print(math['Questions'][difficulty])
        answer = input('   A)' + math[rad[0]][difficulty] + "\n   B) " + math[rad[1]][difficulty] + "\n   C) " + math[rad[2]][difficulty] + '\n')
        
    elif category == 'colors':
        print(colors['Questions'][difficulty])
        answer = input('   A)' + colors[rad[0]][difficulty] + "\n   B) " + colors[rad[1]][difficulty] + "\n   C) " + colors[rad[2]][difficulty] + '\n')
        
    elif category == 'ucsd':
        print(ucsd['Questions'][difficulty])
        answer = input('   A)' + ucsd[rad[0]][difficulty] + "\n   B) " + ucsd[rad[1]][difficulty] + "\n   C) " + ucsd[rad[2]][difficulty] + '\n')
        
    elif category == 'pets':
        print(pets['Questions'][difficulty])
        answer = input('   A)' + pets[rad[0]][difficulty] + "\n   B) " + pets[rad[1]][difficulty] + "\n   C) " + pets[rad[2]][difficulty] + '\n')
        
    else:
        print('Select one of the exisitng categories')
        user_interaction(picks)
        
    return answer, rad

def randomize_list():
    
    lists = ['Answers', 'A', 'B']
    rad = random.sample(lists, 3)
    
    return rad

def check_answer(answer, rad, category, difficulty, points):
    answer_rad = rad.index('Answers') # returns index of where the answer is located

# assigns a number to the letter chosen to be compared to index of the answer
    if answer.lower() == 'a':
        answer = 0
        
    elif answer.lower() == 'b':
        answer = 1
        
    elif answer.lower() == 'c':
        answer = 2
        
    else:
        print('Pick a listed answer')
        game(category, difficulty)
        
    if answer == answer_rad:
        points = int(points) + int(difficulty)
        print('CORRECT!!! You have ' + str(points) + ' points!')
        
    else:
        print('INCORECT!!! You have ' + str(points) + ' points!')
        
    return points
        
