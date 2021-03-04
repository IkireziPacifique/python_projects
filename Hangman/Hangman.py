#Author Pacifique Linda IKIREZI
# Question1 HangMan Game

def hangman():
    # Game instructions
    print("You are going to answer questions about ALU")
    print("Ready When you are!!")
    print("Here is the game instructions:")
    print("Every time you miss a question (you are hanging the man)")
    print("If you miss six questions (the man dies) and the game stops")
    print("If you get all the questions right , your man lives.\n")
    print("------------------------------------------------------------\n")
    # variable for wins
    a = int(0)
    #varibale for losses
    b = int(0)
    # First Question
    one = input("1. When was ALU founded: ")
    if one == '2015' or one.lower() == 'two thousand and fifteen' or one.lower() =='two thousand fifteen':
        print("You're Correct!")
        a += 1
    else:
        print("Alu was founded in 2015")
        b += 1
    # Second Question
    two = input("2. Who is the CEO of ALU: ")
    if two.lower() == 'fred swaniker':
        print("You're Correct")
        a += 1
    else:
        print("Fred Swaniker is the CEO of ALU")
        b += 1
    # third Question
    three = input("3. Where are ALU campuses: ")
    if three.lower() == 'rwanda and mauritius':
        print("You're Correct")
        a += 1
    else:
        print("ALU's campuses are in Rwanda and Mauritius")
        b += 1
    # forth Question
    four = input("4. How many campuses does ALU have: ")
    if four == '2' or four.lower() =='two':
        print("You're Correct")
        a += 1
    else:
        print("ALU has 2 campuses")
        b += 1
    # fifth Question
    five = input("5. What is the name of ALU Rwandaâ€™s Dean: ")
    if five.lower() == 'gaidi faraj':
        print("You're Correct")
        a += 1
    else:
        print("ALU Rwanda Dean is Gaidi Faraj")
        b += 1
    # sixth Question
    six = input("6. Who is in Charge of Student Life: ")
    if six.lower() == 'sila ogidi':
        print("You're Correct")
        a += 1
    else:
        print("The correct answer is Sila Ogidi")
        b += 1
        if b == 6:
            print("You hanged the man")
            return()
    # seventh Question
    seven = input("7. What is the name of our Lab: ")
    if seven.lower() == 'nigeria':
        print("You're Correct")
        a += 1
    else:
        print("Our Lab is called Nigeria")
        b += 1
        if b == 6:
            print("You hanged the man")
            return()
    # eight Question
    eight = input("8. How many students do we have in year 2 Cs: ")
    if eight == '32' or eight.lower() == 'thirty two':
        print("You're Correct")
        a += 1
    else:
        print("Year 2 CS students are 32")
        b += 1
        if b == 6:
            print("You hanged the man")
            return()
    # nineth Question
    nine = input("9. How many degrees does ALU offer: ")
    if nine == '8' or nine.lower() == 'eight':
        print("You're Correct")
        a += 1
    else:
        print("ALU offers 8 degree programs")
        b += 1
        if b == 6:
            print("You hanged the man")
            return()
    # tenth Question
    ten = input("10. Where are the headquarters of ALU: ")
    if ten.lower() == 'mauritius':
        print("You're Correct")
        a += 1
    else:
        print("ALU headquarters are in Mauritius")
        b += 1
        if b == 6:
            print("You hanged the man")
            return()
    # After game conditions
    win = 0
    win = win + a
    loss =0
    loss = loss + b
    if b < 6:
        print("\nCongrats you have reached the end. You have " , win ,"Wins and " , loss , "losses")
    else:
        print("\nCongrats you have won!!!")
#calling the function
hangman()
x = 1
y = True
while y == y:
    y = input("\nDo you want to try again if 'yes' enter Y if 'no' enter N: ")
    if y.upper() == 'Y':
        hangman()
        x += 1
    elif y.upper() == 'N':
        print("\nYou have played " , x)
        exit("See you next time Byeee!!!")
    else:
        print("You have played ", x)
        print("You did not choose any option. Bye!!!")
        exit("See you next time Byeee!!!")