import random
import time
user_name=input("Enter your name:")
time.sleep(1)
print("Hi,",user_name)
time.sleep(1)
print("Welcome to Quiz game")
time.sleep(1)
a=print("Let's check your IQ")
print()
time.sleep(1)
score=0
correct=0
wrong=0
def q_1():
    global score
    global correct
    global wrong
    q1="What is the output of type(3/2) in Python 3?"
    print("Your first Question:-")
    time.sleep(1)
    print(q1)
    correct_ans1="float"
    time.sleep(1)
    options1=["int","float","decimal","complex"]
    random.shuffle(options1)
    for i,opt in enumerate(options1,start=1):
        print(f"{i}. {opt}")
    print()
    choice1=int(input("Enter your choice:"))
    if choice1 <1 or choice1 > len(options1):
        print("Invalid option selected")
        print()
        q_1()
        return
    elif options1[choice1-1]==correct_ans1:
        score+=5
        time.sleep(0.5)
        correct+=1
        print("You scored 5 points")
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans1}")
        wrong+=1
        print()
    time.sleep(1)
    q_2()
    
def q_2():
    global score
    global correct
    global wrong
    q2='What will print("5"*3)?'
    print("Your second Question:-")
    time.sleep(1)
    print(q2)
    correct_ans2="555"
    time.sleep(1)
    options2=["15","555","53","Error"]
    random.shuffle(options2)
    for i,opt in enumerate(options2,start=1):
        print(f"{i}. {opt}")
    print()
    choice2=int(input("Enter your choice:"))
    if choice2 <1 or choice2 > len(options2):
        print("Invalid option selected")
        print()
        q_2()
        return
    elif options2[choice2-1]==correct_ans2:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans2}")
        wrong+=1
        print()
    time.sleep(1)
    q_3()
    
def q_3():
    global score
    global correct
    global wrong
    q3='What is the len({"a":1,"b":2,"c":3})?'
    print("Your third Question:-")
    time.sleep(1)
    print(q3)
    correct_ans3="3"
    time.sleep(1)
    options3=["1","3","6","Error"]
    random.shuffle(options3)
    for i,opt in enumerate(options3,start=1):
        print(f"{i}. {opt}")
    print()
    choice3=int(input("Enter your choice:"))
    if choice3 <1 or choice3 > len(options3):
        print("Invalid option selected")
        print()
        q_3()
        return
    elif options3[choice3-1]==correct_ans3:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans3}")
        wrong+=1
        print()
    time.sleep(1)
    q_4()

def q_4():
    global score
    global correct
    global wrong
    q4="What is the output of bool([])?"
    print("Your fourth Question:-")
    time.sleep(1) 
    print(q4)
    correct_ans4="False"
    time.sleep(1)
    options4=["True","False","None","Error"]
    random.shuffle(options4)
    for i,opt in enumerate(options4,start=1):
        print(f"{i}. {opt}")
    print()
    choice4=int(input("Enter your choice:"))
    if choice4 <1 or choice4 > len(options4):
        print("Invalid option selected")
        print()
        q_4()
        return
    elif options4[choice4-1]==correct_ans4:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans4}")
        wrong+=1
        print()
    time.sleep(1)
    q_5()

def q_5():
    global score
    global correct
    global wrong
    q5="Which statement skips the current iteration of a loop?"
    print("Your fifth Question:-")
    time.sleep(1)
    print(q5)
    correct_ans5="continue"
    time.sleep(1)
    options5=["pass","break","skip","continue"]
    random.shuffle(options5)
    for i,opt in enumerate(options5,start=1):
        print(f"{i}. {opt}")
    print()
    choice5=int(input("Enter your choice:"))
    if choice5 <1 or choice5 > len(options5):
        print("Invalid option selected")
        print()
        q_5()
        return
    elif options5[choice5-1]==correct_ans5:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans5}")
        wrong+=1
        print()
    time.sleep(1)
    q_6()

def q_6():
    global score
    global correct
    global wrong
    q6='''
        def add(x, y=5):
            return x + y
        print(add(3))'''
    print("Your sixth Question:-")
    time.sleep(1)
    print(q6)
    correct_ans6="8"
    options6=["3","5","8","Error"]
    random.shuffle(options6)
    for i,opt in enumerate(options6,start=1):
        print(f"{i}. {opt}")
    print()
    choice6=int(input("Enter your choice:"))
    if choice6 <1 or choice6 > len(options6):
        print("Invalid option selected")
        print()
        q_6()
        return
    elif options6[choice6-1]==correct_ans6:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans6}")
        wrong+=1
        print()
    time.sleep(1)
    q_7()

def q_7():
    global score
    global correct
    global wrong
    q7='''
        x=10
        if x>5:
            print("A")
        elif x==10:
            print("B")
        else:
            print("C")'''
    print("Your seventh Question:-")
    time.sleep(1)
    print(q7)
    correct_ans7="A"
    options7=["A","B","C","AB"]
    random.shuffle(options7)
    for i,opt in enumerate(options7,start=1):
        print(f"{i}. {opt}")
    choice7=int(input("Enter your choice:"))
    if choice7 <1 or choice7 > len(options7):
        print("Invalid option selected")
        print()
        q_7()
        return
    elif options7[choice7-1]==correct_ans7:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans7}")
        wrong+=1
        print()
    time.sleep(1)
    q_8()

def q_8():
    global score
    global correct
    global wrong
    q8='''
        t = (1, 2, [3, 4])
        t[2][0] = 99
        print(t)
        '''
    print("Your eighth Question:-")
    time.sleep(1)
    print(q8)
    correct_ans8="(1, 2, [99, 4])"
    options8=["(1, 2, [3, 4])","(1, 2, [99, 4])","Error","(1, 2, 99, 4)"]
    random.shuffle(options8)
    for i,opt in enumerate(options8,start=1):
        print(f"{i}. {opt}")
    choice8=int(input("Enter your choice:"))
    if choice8 <1 or choice8 > len(options8):
        print("Invalid option selected")
        print()
        q_8()
        return
    elif options8[choice8-1]==correct_ans8:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong option, Correct answer:{correct_ans8}")
        wrong+=1
        print()
    time.sleep(1)
    q_9()

def q_9():
    global score
    global correct
    global wrong
    q9='''
          for i in range(3):
            print(i, end="-")
          else:
            print("End")
       '''
    print("Your ninth Question:-")
    time.sleep(1)
    print(q9)
    correct_ans9="0-1-2-End"
    options9=["0-1-2-End","0-1-2-","End","Error"]
    random.shuffle(options9)
    for i,opt in enumerate(options9,start=1):
        print(f"{i}. {opt}")
    choice9=int(input("Enter your choice:"))
    if choice9 <1 or choice9 > len(options9):
        print("Invalid option selected")
        print()
        q_9()
        return
    elif options9[choice9-1]==correct_ans9:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans9}")
        wrong+=1
        print()
    time.sleep(1)
    q_10()

def q_10():
    global score
    global correct
    global wrong
    q10='''What is the output
        x = 5
        def f():
            global x
            x = 10
        f()
        print(x)'''
    print("Your tenth Question:-")
    time.sleep(1)
    print(q10)
    correct_ans10="10"
    time.sleep(1)
    options10=["5","10","Error","None"]
    random.shuffle(options10)
    for i,opt in enumerate(options10,start=1):
        print(f"{i}. {opt}")
    print()
    choice10=int(input("Enter your choice:"))
    if choice10 <1 or choice10 > len(options10):
        print("Invalid option selected")
        print()
        q_10()
        return
    elif options10[choice10-1]==correct_ans10:
        score+=5
        time.sleep(0.5)
        print("You scored 5 points")
        correct+=1
        print()
    else:
        score-=2
        time.sleep(1)
        print(f"You selected the wrong answer, Correct answer:{correct_ans10}")
        wrong+=1
        print()

q_1()
time.sleep(1)
print("Analysis:-")
time.sleep(1.5)
print(f"Total correct: {correct}  Total Wrong: {wrong}")
time.sleep(1.5)
print(f"Final score of {user_name}:",score)
