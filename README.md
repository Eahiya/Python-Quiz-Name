# Python-Quiz-Game
# A MCQ quiz game using python Program

print (" \n                                                   Quiz Game \n ")
nam = input(" Please Enter Your Name: ")
print(' Hello! ',nam)
quistion = input(" Do you want to play a computer quiz game ? (yes|no): \n ")
if quistion != "yes":
    quit()
print(" Okay let's play :)")
score = 0

answer1 = input(" 1. What is the cleanest country in thr world? \n  ")
if answer1.lower() == "switzerland":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer2 = input(" 2. Who was the most highy paid UFC athlete in 2021? \n ")
if answer2.lower() == "connor mcgregor" or "connor":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorect Answer! \n ")

answer3 = input(" 3. When was the 1st World War started? \n ")
if answer3.lower() == "1914" or "nineteen fourteen":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer4 = input(" 4. Who was the founder and the C.E.O OF amazon.com? \n ")
if answer4.lower() == "jeff bezzos" or "jeffry":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(' Incorrect Answer! \n ')

answer5 = input(" 5. What is the capital of United States of America? \n ")
if answer5.lower() == "washington dc" or "washington":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer6 = input(" 6. Which country has the highest population? \n ")
if answer6.lower() == "china":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer7 = input(" 7. How many countries are there in this world? \n ")
if answer7.lower() == "195" or "hundred and ninety five":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer8 = input(" 8. Who was the first person to step on the moon? \n ")
if answer8.lower() == "niel amstrong":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer9 = input(" 9. What is the study of weather called? \n ")
if answer9.lower() == "meterology":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer10 = input(" 10. Which is the biggest continent in the world? \n ")
if answer10.lower() == "asia" or "asian":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer11 = input(" 11. What is the coldest planet of our solar system? \n ")
if answer11.lower() == "neptune":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorect Answer! \n ")

answer12 = input(" 12. Approximately how many kilometers are represented by 1 degree of latitude? \n ")
if answer12.lower() == "111 km" or "hundred and eleven":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer13 = input(" 13. Who is the most viewed and liked person in the internet? \n ")
if answer13.lower() == "rock" or "dwyn jhonson":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer14 = input(" 14. What is the most expensive thing built in the entire world that costs around 100 billion US dollars? \n ")
if answer14.lower() == "the international space station" or "iss":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer15 = input(" 15. What is the tallest mountain in the world? \n ")
if answer15.lower() == "mt everest" or "everest":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer16 = input(" 16. Which planet was first to be discovered through a telescope by Herchel in 1781? \n ")
if answer16.lower() == "uranus":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer17 = input(" 17. How many times a person can be elected as the President of USA? \n ")
if answer17.lower() == "two times" or "2":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer18 = input(" 18. What is the 10th largest state in the United States of America? \n ")
if answer18.lower() == "machigen" or "machigen state":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer19 = input(" 19. Where is the Area 51 located in the USA? \n ")
if answer19.lower() == "ohio":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

answer20 = input(" 20. What is the abbrivation of GPU? \n ")
if answer20.lower() == "graphical processing unit" or "graphic processing unit":
    print(" Correct Answer! \n ")
    score += 1
else:
    print(" Incorrect Answer! \n ")

print(" Congradulations!")
print(" You have got " + str(score) + " questions correct!")
print(" You have scored " + str((score/20) * 100) + "%.")

