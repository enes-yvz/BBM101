import threading
import sys
import time
def big(a):
    if "i" in a:
        a = a.replace("i", "İ")
    if "ı" in a:
        a = a.replace("ı", "I")
    return a
def small(a):
    if "İ" in a:
        a = a.replace("İ","i")
    if "I" in a:
        a = a.replace("I","ı")
    return a
if len(sys.argv)!=3:
    print("You must write two arguments for this program")
else:
    dict1={}
    dict2={}
    score=0
    finish=[]
    total=[]
    allGuesses=[]
    myList=[]
    letter_values = open(sys.argv[2],encoding='utf-8-sig')
    for line in letter_values:
        line=line.strip("\n")
        i=line.split(":")
        dict2[i[0]]=i[1]
    letter_values.close()
    correct_words = open(sys.argv[1],encoding='utf-8-sig')
    for line in correct_words:
        line = line.strip("\n")
        i=line.split(":")
        dict1[i[0]] = i[1]
    correct_words.close()
    correct_words = open(sys.argv[1],encoding='utf-8-sig')
    for line in correct_words:
        i=line.split(":")
        sletters =i[0]
        sletters=small(sletters)
        for item in dict1[big(sletters)].split(","):
            myList.append(item)
        print("Shuffled letters are:", sletters.lower(), "Please guess words for these letters with the minimum three letters")
        start_time = time.time()
        def myfun():
            while time.time()-start_time < 30:
                print("Guessed Word:",end=" ")
                temporary=input()
                if temporary=="":
                    print("Your guessed word not a valid word")
                    print("You have", int(30 - (time.time() - start_time)), "time")
                else:
                    if len(temporary)<3:
                        print("Please guess words with the minimum three letters")
                        print("You have", int(30 - (time.time() - start_time)), "time")
                    else:
                        guess=temporary
                        guess=big(guess)
                        guess=guess.upper()
                        if guess in myList and guess not in allGuesses :
                            for i in guess:
                                global score
                                score+=int(dict2[i])
                            if guess not in allGuesses:
                                total.append(len(guess*score))
                            score=0
                            allGuesses.append(guess)
                        elif guess in allGuesses :
                            print("This word is guessed before")
                        elif guess not in myList:
                            print("Your guessed word not a valid word")
                        print("You have", int(30 - (time.time() - start_time)), "time")
        myfun_thread = threading.Thread(target=myfun)
        myfun_thread.daemon = True
        myfun_thread.start()
        myfun_thread.join(30)
        print("Your time is up")
        myList = []
        if len(allGuesses)>0:
            sletters=small(sletters)
            print("Score for",sletters.lower(),"is",sum(total),"and guessed words are:",end=" ")
            finish.append(sum(total))
            for i in allGuesses:
                if i==allGuesses[-1]:
                    i = small(i)
                    print(i.lower())
                else:
                    i = small(i)
                    print(i.lower(),end="-")
        else:
            sletters=small(sletters)
            print("Score for", sletters.lower(),"is",sum(total),"There isn't correctly guessed word")
        total=[]
        allGuesses=[]
    print("Total score is:",sum(finish))
    correct_words.close()