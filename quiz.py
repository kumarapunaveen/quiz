#questions and answers 
q1 = """Which of the following is a prime number?
1. 4
2. 6
3. 9
4. 7"""
q2 = """What is the capital of France?
1. Berlin
2. Madrid
3. Paris
4. Rome"""
q3 = """Which planet is known as the Red Planet?
1. Earth
2. Venus
3. Mars
4. Jupiter"""
q4 = """Which element has the chemical symbol 'O'?
1. Hydrogen
2. Oxygen
3. Nitrogen
4. Carbon"""
q5 = """Which animal is known as the 'King of the Jungle'?
1. Elephant
2. Lion
3. Tiger
4. Gorilla"""

q6 = """Which gas do plants absorb from the atmosphere during photosynthesis?
1. Oxygen
2. Carbon Dioxide
3. Nitrogen
4. Hydrogen"""

q7 = """Who wrote the play 'Romeo and Juliet'?
1. Charles Dickens
2. Leo Tolstoy
3. William Shakespeare
4. Mark Twain"""

q8 = """Which planet is the largest in our solar system?
1. Earth
2. Mars
3. Jupiter
4. Saturn"""

q9 = """What is the boiling point of water at sea level?
1. 90°C
2. 100°C
3. 110°C
4. 120°C"""

q10 = """Which is the smallest prime number?
1. 1
2. 2
3. 3
4. 5"""

q11 = """Which country is known as the Land of the Rising Sun?
1. China
2. Japan
3. South Korea
4. Thailand"""

q12 = """What is the hardest natural substance on Earth?
1. Gold
2. Iron
3. Diamond
4. Silver"""

q13 = """What is the main ingredient in guacamole?
1. Tomato
2. Avocado
3. Onion
4. Cucumber"""

q14 = """Which ocean is the largest in the world?
1. Atlantic Ocean
2. Indian Ocean
3. Arctic Ocean
4. Pacific Ocean"""

#keep all questions and correct answer in dictionary
questions = {q1:4,q2:3,q3:3,q4:2,q5:2,
    q6:2,
    q7:3,
    q8:3,
    q9:2,
    q10:2,
    q11:2,
    q12:3,
    q13:2,
    q14:4}

name = input("enter name")
print(f"welcome {name} to quiz")
score =0
#display questions
for i in questions: # i is the key
    print()
    print(i) #displaying ith question (only keys will displayed not values)

    #to quit from quiz
    flag = input("Do you want to quit the quiz (yes/no) ")
    if flag.lower() == "yes":
        break #out of for loop

    #to skip question(skip question and continue)
    flag1 = input("do you want to skip the question(yes/no)")
    if flag1.lower() == "yes":
        continue
    
    ans = int(input("enter correcet answer(1/2/3/4)"))
    if ans == questions[i]: #questions[i] is the correct answer
        print("correct answer")
        score+=1
    else:
        print("wrong answer lost 1 point")
        score-=1
print("final score is",score)
