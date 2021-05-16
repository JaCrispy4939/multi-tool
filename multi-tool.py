import random
import datetime
import time
import requests
from googlesearch import search
import webbrowser
while True:
    tool = input("1. Choice Helper, 2. Time, 3. Heads or Tails, 4. google search, 5. Day Calc, 6. Magic 8ball, 7. Number Game, 8. Exit: ")


    if tool ==("1"):

        choice1 = input("choice 1: ")

        choice2 = input("Choice 2: ")

        vars = [choice1,choice2]

        print (random.sample(vars, 1))

        



    if tool ==("2"):
        def jls_extract_def():
            return 


        now = datetime.datetime.now
        print(now.strftime("%I:%M:%S %p"))

        x = datetime.datetime.now()

        print(x.year)

        print(x.strftime("%A"))

        

   
        

    if tool ==("3"):

        print("flipping.")

        time.sleep(1) 
        print("flipping..")
        time.sleep(1)
        print("flipping...")
        coin = (random.randint(1, 2))
        time.sleep(1)

        if coin == 1:

            print("Coin landed on Heads")

        if coin == 2:

            print("Coin landed on Tails")



    if tool ==("4"):
        query = input("what do you want to search: ")
        #  iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % query)


    if tool ==("5"):

        print("year-month-date example (2021-6-20)")
        from datetime import datetime

        firstdate_str = input("first date: ")

        seconddate_str = input("second date: ")

        firstdate_dt = datetime.strptime(firstdate_str,"%Y-%m-%d").date()

        seconddate_dt = datetime.strptime(seconddate_str,"%Y-%m-%d").date()

        days = seconddate_dt - firstdate_dt

        print(days.days)



    if tool ==("6"):

        askball = input("whats your question: ")

        response = random.randint(1, 5)

        if response == 1:

            print("Most definitely")

        if response == 2:

            print("Its possible")

        if response == 3:

            print("I dont know")

        if response == 4:

            print("Probably not")

        if response == 5:

            print("Not a chance")



    if tool ==("7"):

        print("work in progress")
        end

        print("I am thinkning of a number between 1 and 20 ")

        number = random.randint(1, 20)

        guess = int(input("Guess: "))

        if guess == number:

            print("you win")

        if guess < number:

            print("too low")

        if guess > number:

            print("too high")
   
    if tool == "8":
        print("goodbye")
        time.sleep(3)
        quit()