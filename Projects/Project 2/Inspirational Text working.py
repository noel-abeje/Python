#Noel Abeje
#Due 7th Oct 2020
#Allows the user to interract with and alter a txt file of their choosing and a few other operations for recreation to an extent


#To pick a txt file with a plan if they enter an invalid file or if they forgot to add .txt
while True:
    try:
        Greeting=input('Hey there! Pick a txt file, any that exists within your system that is in the same location as this little code\n')
        if Greeting.endswith('.txt'):
            with open(Greeting,"r+") as goo:
                contents=goo.read()
                break
        else:
            Greeting+=".txt"
            with open(Greeting,"r+") as goo:
                contents=goo.read()
                break
    except FileNotFoundError:
        print('Please put in an existing txt file in your system and in the same file location as this code.')

#This is the main menu
while True:
    print('What would you like to do?')
    print('1.If you want to search for a specific word or phrase in the textfile and see how many times it occurs, press 1')
    print('2.If you want to search for a specific word or phrase and print a string of about 100 characters around the word or phrase, press 2')
    print('3.If you would like to search for and replace a word or phrase, press 3')
    print('4.If you want to encode the txt file then save it as a new file, press 4')
    print('5.If you want to play a guessing game, press 5')
    print('6.If you want to send an email with a keyword and some context or a random chunk of text from the selected txt file, press 6')
    print('7.If you want to quit, press 7')
   
#Where the user should pick an option with plans that user may put letters or wrong numbers
    while True:
        try:
            choice=int(input('So which option would you like to pick?\n'))
            if choice<1 or choice>7:
                print("pick number between 1 and 7")
                continue
            break
        except ValueError:
            print('Please pick a NUMBER between 1-6')
#If user picks choice 1

    if choice==1:
        while True:
            word=input('Input a word or phrase you want to search for\n')
            word=word.lower()
            lower = contents.lower() #To make sure it finds all the words that match the user's word
            count=lower.count(word)
            print(count)
            again=input('Do you want to search for another word or phrase? Yes or No\n')
            if again.lower().startswith("y"):
                continue
            else:
                break
      
#If user picks choice 2
    if choice==2:
        while True:
            word2=input('Input a word or a phrase you want to find some context for\n')
            word2=' '+word2+' '    #To leave out words within other words
            find=contents.find(word2)
            if contents[find]=="?":    #If the typed word does not exist in the txt file
                print("That word does not exist in the selected txt file, Try again")
                continue
            else:
                print(contents[find-50:find], contents[find:find+51])
                again2=input('Do you want to search for another word or phrase? Yes or No\n')
                if again2.lower().startswith("y"):
                    continue
                else:
                    break
#If user picks choice 3
    if choice==3:
        while True:
            toreplace=input('What word or phrase would you like to replace?\n')
            replaced=input('What word or phrase would you like to replace the chosen word with?\n')
            replace=contents.replace(toreplace,replaced)
            newfile=input("What do you want to call the new file with the replaced word? Make sure it's not an existing file unless you want that file to be erased.\n")
            if newfile.endswith('.txt'):       #If the name they entered is not formatted correctly
                None
            else:
                newfile+=".txt"
            with open(newfile,"w+") as goo:
                goo.write(replace)
            print(toreplace,'has been replaced by',replaced, 'in the txt file',newfile,"\nThank you for using this tool")
            again3=input('Do you want to replace another word or phrase? Yes or No\n')
            if again3.lower().startswith("y"):
                continue
            else:
                break

#If the user picks option 4
    if choice==4:
        def caesar(text,shift):     #previously created caesar function 
            text=text.lower()
            output = ""
            for char in text:
                if char.isalpha():
                    output+=chr((ord(char)+shift-97)%26+97)
                else:
                    output+=char
            return output
        while True:
            while True:
                try:
                    skip=int(input("By how much would you like to shift each letter in the txt file by? Please pick a number\n"))
                    break
                except ValueError:
                    print('Please pick a NUMBER')
            fname=input('What do you want to call the encoded file? Make sure it is not an existing file unless you want that file to be erased\n')
            if fname.endswith('.txt'):     #If the name they entered is not formatted correctly
                None
            else:
                fname+=".txt"
            encoded=caesar(contents,skip)
            with open(fname,'w+') as goo:
                goo.write(encoded)
            print('File has been successfully encoded as', fname)
            again4=input('Do you want to encode the file again? Yes or No\n')
            if again4.lower().startswith("y"):
                continue
            else:
                break

#If the user picks choice 5
    if choice==5:
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
                break
            amount=amount+1
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
                        winners = goo.read()
                    winnerslist = winners.splitlines()
                    sortedlist = sorted(winnerslist)
                    for i in sortedlist[0:3]:
                        print(i)
                except FileNotFoundError:
                    print("Sorry, I can't seem to find any games you won")
                restart1=input("Do you want to play again? Yes or No\n")
                if restart1=="yes" or restart1=="Yes" or restart1=="y" or restart1=="Y":
                    print("Here we go again")
                    amount = 0
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
#If the user picks choice 7
    if choice==7:
        bye=input('Type quit if you really want to quit\n')
        if bye.lower()=='quit':
            print("Goodbye! Thanks for using my code")
            quit()
        else:
            continue
#If user picks choice 6
    if choice==6:
        #Starter code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
        #Info on ports here: https://support.desk.com/customer/portal/articles/1741-configuring-smtp-servers-to-send-email

        import smtplib, random
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        def sendEmail(sender, sendee, header, body, password):
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login(sender, password)
            msg = MIMEMultipart()
            msg['From']= sender
            msg['To']= sendee
            msg['Subject']= header
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)
            del msg
            s.quit()
        while True:
            print('If you want to send an email that has a keyword of your choosing with some context from your txt file, press 1')
            print('If you want to send a random chunk of text from the chosen txt, press 2')
            while True:
                try:
                    ask=int(input('So which option would you like to pick?\n'))
                    if ask<1 or ask>2:
                        print("pick number between 1 and 2")
                        continue
                    break
                except ValueError:
                    print('Please type 1 or 2')
            if ask==1:
                email="testersthing@gmail.com"
                password="Verymuchatest123"
                recipient=input('Enter your email\n')
                subject=input('Enter the subject(header) of your email?\n')
                while True:
                    keyword=input('Input your keyword for the chunk of text to send\n')
                    keyword=' '+keyword+' '    #To leave out words within other words
                    find=contents.find(keyword)
                    if contents[find]=="?":    #If the typed word does not exist in the txt file
                        print("That word does not exist in the selected txt file, Try again")
                        continue
                    else:
                        hunk=contents[find-100:find]+" "+contents[find:find+101]
                        break
                body=hunk
                sendEmail(email, recipient, subject, body, password)
                print('Your email has been successfully sent!')
                break
            if ask==2:
                email="testersthing@gmail.com"
                password="Verymuchatest123"
                recipient=input('Enter your email\n')
                subject=input('Enter the subject(header) of your email?\n')
                import random
                rand=random.randint(0,len(contents)-200)
                amount=rand+200
                chunk=contents[rand:amount]
                body=chunk
                sendEmail(email, recipient, subject, body, password)
                print('Your email has been successfully sent!')
                break
                    
        
        
            
                    
                    
                    
        

    
    
