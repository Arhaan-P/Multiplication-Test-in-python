score=0
print("------------------MULTIPLICATION TABLES PRACTICE---------------------")

print("""
1: Testing (Scores are calculated and there is only one attempt)
2: Learning (No scores are calculated, three attempts for each question)
""")

choice=input("Enter the choice number(1 or 2) ")
while True:
    if choice=="1":
        print("Invoking testing module")
        break
    elif choice=="2":
        print("Invoking learning module")
        break
    else:
        choice=input("Please enter a valid option (1 or 2) ")


if choice=="1" :
    name=input("Please enter your name : ")
    while True:
        if name=="":
            name=input("Name cannot be left blank, please enter your name ")
        elif name.isdigit():
            name=input("Name cannot be a number, please enter your name ")
        else:
            break

    Mult_table=input("Enter the multiplication table, from 2 to 12 ")
    while True:
        if Mult_table.isdigit():
                if int(Mult_table)<2 or int(Mult_table)>12:
                    Mult_table=int(input("Please enter a number between 2 and 12 inclusive "))
                else:
                    Mult_table=int(Mult_table)
                    break
        elif Mult_table=="":
            Mult_table=int(input("Field cannot be left blank "))
        else:
            break
    
    import random
    for i in range (1,6):
        n=random.randint(1,12)
        print("Question", i, ": ")
        print(Mult_table, "x", n)
        answer=input("Answer: ")
        while True:
            if answer=="":
                answer=input("Answer cannot be left blank ")

            elif answer.isdigit():
                break
            else:
                answer=input("Answer cannot be in letters, please enter numbers instead ")
        if answer== str(Mult_table*n):
            score=score+1
        else:
            score=score

    if score==5:
        print(name, "your score is ", score,"/5")
        print("")
        print("Well done full marks ")
    elif score<5:
        print(name, "your score is ", score,"/5")
        print("")
        print("Have another practice ")
