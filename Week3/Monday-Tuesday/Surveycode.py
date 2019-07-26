import time
import json

answers=[]

def start():
    startquestion=input("Would you like to take a survey? ")
    if startquestion=="yes":
        questions()
    if startquestion=="no":
        print("okay, bye")
        averageage()
        #sibstat()
def next():
    next=input("Is there anyone more people? ")
    if next=="yes":
        time.sleep(1)
        print("Next Person")
        questions()
    if next=="no":        
        with open('data.json','r')as myDataFile:
            list= json.load(myDataFile)

        with open('data.json','w') as myDataFile:
            list.extend(answers)
            json.dump(list, myDataFile)
        print(answers)
        averageage()
        #sibstat()
def questions():

    dict={}
    answer1=input("What is your name? ")
    dict["Name"]=answer1

    answer2=int(input("What is your age? "))
    dict["Age"]=answer2

    answer3=input("Do you have any siblings? ")
    dict["Siblings"]=answer3

    answer4=input("What is your hometown? ")
    dict["School"]=answer4

    answers.append (dict)

    next()

#analyze data
def averageage():
    with open('data.json','r')as myDataFile:
            list= json.load(myDataFile)
            list[1]["Age"]
            total=0
            for i in list:
                total+=int(i["Age"])
                average= total/len(list)
    print("The average age is...")
    print(average)
    
#def sibstat():
   # if answer3=="yes">answer3=="no":
     #   print("Most people have siblings")
    #else:
        #print("Most people dont have siblings")
start()
