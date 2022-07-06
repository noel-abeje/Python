#Noel Abeje
#09/15/2020
#Programming Assignment #1: Guessing Game
#This code lets you play a little guessing game where you guess a number and it tells you to guess a higher number or a lower number using while loops, if and elif statements, a few other more basic things

import random

#to get the number of guesses
amount=0
while amount<5:
    while amount==0:
        name=input("Enter your name child\n")
        break
#First I get a random number
    while amount==0:
        number=int(random.randint(1,100))
        print(number)
        break
    amount=amount+1
    print(amount)
#If value error occurs
    while True:
        try:
            guess=int(input("Pick a number between 1 and 100\n"))
            break
        except ValueError:
            print("Pick a NUMBER, like actual Digits like 1 or 50 ok?")
    if number==guess:
        print("Congratulations, you wasted your time guessing a number")
        print("You won in", amount, "tries!")
        listname=name
#To get the leaderboards file
        if amount==1:
            with open("Leaderboards.txt", 'a+') as goo:
                goo.write("1."+listname+"\n")
        elif amount==2:
            with open("Leaderboards.txt", 'a+') as goo:
                goo.write("2."+listname+"\n")
        elif amount==3:
            with open("Leaderboards.txt", 'a+') as goo:
                goo.write("3."+listname+"\n")
        elif amount==4:
            with open("Leaderboards.txt", 'a+') as goo:
                goo.write("4."+listname+"\n")
        elif amount==5:
            with open("Leaderboards.txt", 'a+') as goo:
                goo.write("5."+listname+"\n")
        print("These are the top guessers")
        with open("Leaderboards.txt", 'r+') as goo:
                winners=goo.read()
        winnerslist=winners.splitlines()
        sortedlist=sorted(winnerslist)
        for i in sortedlist[0:3]:
            print(i)       
        restart=input("Do you want to waste your time again? Yes or No\n")
#Restart loop to play again or stop here
        if restart=="yes" or restart=="Yes" or restart=="y" or restart=="Y":
            print("Here we go again")
            amount=0
            continue
        elif restart!="yes" or restart!="Yes" or restart!="y" or restart!="Y":
            print("Good Choice")
            rickroll=input('Would you rather read the lyrics of the best song of all time?\n') 
            if rickroll=='yes' or rickroll=='Yes' or rickroll=='y' or rickroll=='Y':
#This part was from the internet by the way, github to be specific
                d="""ellU wTay it
                S otherRConna Qmake4 PveMndL aK'reJingHt's beenFo E gC
                (OohB
                Youz txKL q know9
                N28 how I'm feelH
                7iM4 up66)B)8giM, n2giM
                (G5 you4
                I justTannaxU47Gotta PuLerstaL03eMrQ2

                We'M9n eachR for sElongzr hearFKchH butzJxoEshyxEsSInsideTe both9ThaFCoH on
                We9xheCameqweJQplS1
                8g68let4 down8runKrouLqdesert48Pcry8sayCoodbye8tUK lieqhurt40WeJ nEstrangersxEloMz9xhe rulesqsEdEI
                A full commitment'sThat I'mxhinkH ofzTouldn'tCetxhis fromKnyRCuy31AL if4Ksk me7Don'txU me4JxoEbliLxEsee00
                B,C6)B,C556)1300"""
                for s in'UTSRQPMLKJHFECBzxq9876543210':a,b=d.split(s,1);d=b.replace(s,a)
                print(d)
                break
            elif rickroll!='yes' or rickroll!='Yes' or rickroll!='y' or rickroll!='Y':
                    makesure=input('Are you sure you do NOT want to read the lyrics of the best song of all time you monster?\n')
                    if makesure=="yes" or makesure=="Yes" or makesure=="Y" or makesure=="y":
                        print('you are a terrible person and do not deserve these lyrics')
                        exit()
                        break
                    elif makesure!="yes" or makesure!="Yes" or makesure!="Y" or makesure!="y":
                        print('yay, I knew you didnt mean it')
                        d="""ellU wTay it
                        S otherRConna Qmake4 PveMndL aK'reJingHt's beenFo E gC
                        (OohB
                        Youz txKL q know9
                        N28 how I'm feelH
                        7iM4 up66)B)8giM, n2giM
                        (G5 you4
                        I justTannaxU47Gotta PuLerstaL03eMrQ2

                        We'M9n eachR for sElongzr hearFKchH butzJxoEshyxEsSInsideTe both9ThaFCoH on
                        We9xheCameqweJQplS1
                        8g68let4 down8runKrouLqdesert48Pcry8sayCoodbye8tUK lieqhurt40WeJ nEstrangersxEloMz9xhe rulesqsEdEI
                        A full commitment'sThat I'mxhinkH ofzTouldn'tCetxhis fromKnyRCuy31AL if4Ksk me7Don'txU me4JxoEbliLxEsee00
                        B,C6)B,C556)1300"""
                        for s in'UTSRQPMLKJHFECBzxq9876543210':a,b=d.split(s,1);d=b.replace(s,a)
                        print(d)
                        break
#If value is too low
    if number>guess:
        print("Guess a higher number")
        print("You have ",5-amount," guesses")
            
#If value is too high
    elif number<guess:
        print("Guess a lower number")
        print("You have ",5-amount," guesses")
#If the amount of turns has ended
    if amount>=5:
        print("Too bad, you lose")
        try:
            print("These are the top guessers:")
            with open("Leaderboards.txt", 'r+') as goo:
                    winners=goo.read()
            winnerslist=winners.splitlines()
            sortedlist=sorted(winnerslist)
            for i in sortedlist[0:3]:
                print(i)
        except FileNotFoundError:
            print("Sorry, I can't seem to find any games you won")
        restart1 = input("Do you want to play again? Yes or No\n")
        if restart1=="yes" or restart1=="Yes" or restart1=="y" or restart1=="Y":
            print("Here we go again")
            amount=0
            continue
        elif restart1!="yes" or restart1!="Yes" or restart1!="y" or restart1!="Y":
            print("Good Choice")
            rickroll=input('Would you rather read the lyrics of the best song of all time?\n') 
            if rickroll=='yes' or rickroll=='Yes' or rickroll=='y' or rickroll=='Y':
#This part was from the internet by the way, github to be specific
                d="""ellU wTay it
                S otherRConna Qmake4 PveMndL aK'reJingHt's beenFo E gC
                (OohB
                Youz txKL q know9
                N28 how I'm feelH
                7iM4 up66)B)8giM, n2giM
                (G5 you4
                I justTannaxU47Gotta PuLerstaL03eMrQ2

                We'M9n eachR for sElongzr hearFKchH butzJxoEshyxEsSInsideTe both9ThaFCoH on
                We9xheCameqweJQplS1
                8g68let4 down8runKrouLqdesert48Pcry8sayCoodbye8tUK lieqhurt40WeJ nEstrangersxEloMz9xhe rulesqsEdEI
                A full commitment'sThat I'mxhinkH ofzTouldn'tCetxhis fromKnyRCuy31AL if4Ksk me7Don'txU me4JxoEbliLxEsee00
                B,C6)B,C556)1300"""
                for s in'UTSRQPMLKJHFECBzxq9876543210':a,b=d.split(s,1);d=b.replace(s,a)
                print(d)
                break
            elif rickroll!='yes' or rickroll!='Yes' or rickroll!='y' or rickroll!='Y':
                    makesure=input('Are you sure you do NOT want to read the lyrics of the best song of all time you monster?\n')
                    if makesure=="yes" or makesure=="Yes" or makesure=="Y" or makesure=="y":
                        print('you are a terrible person and a loser, a dumb loser who could not even guess a number correctly and you have bad taste in music')
                        break
                    elif makesure!="yes" or makesure!="Yes" or makesure!="Y" or makesure!="y":
                        print('yay, I knew you didnt mean it')
                        d="""ellU wTay it
                        S otherRConna Qmake4 PveMndL aK'reJingHt's beenFo E gC
                        (OohB
                        Youz txKL q know9
                        N28 how I'm feelH
                        7iM4 up66)B)8giM, n2giM
                        (G5 you4
                        I justTannaxU47Gotta PuLerstaL03eMrQ2

                        We'M9n eachR for sElongzr hearFKchH butzJxoEshyxEsSInsideTe both9ThaFCoH on
                        We9xheCameqweJQplS1
                        8g68let4 down8runKrouLqdesert48Pcry8sayCoodbye8tUK lieqhurt40WeJ nEstrangersxEloMz9xhe rulesqsEdEI
                        A full commitment'sThat I'mxhinkH ofzTouldn'tCetxhis fromKnyRCuy31AL if4Ksk me7Don'txU me4JxoEbliLxEsee00
                        B,C6)B,C556)1300"""
                        for s in'UTSRQPMLKJHFECBzxq9876543210':a,b=d.split(s,1);d=b.replace(s,a)
                        print(d)
                        break
#If the wrong value is put in
    elif  guess>100 or guess<1:
        print("It should be less than 101 and greater than 0 ok?")
