#File: assignment9.py
#Name: Carole (Chia Jung) Sung
#Date: March 26 2018
#Description: MET CS201 Programming Exercises 5,7,8 of  Chapter 10

#Exercise 5
class RetailItem:
    def __init__(self,description,inventory,price):
        self.description=description
        self.inventory=inventory
        self.price=price
    
itm1=RetailItem("Jacket",12,59.95)
itm2=RetailItem("Designer Jeans", 40, 34.95)
itm3=RetailItem("Shirt",20,24.95)

#Exercise 7 (Call the method shopping())
class CashRegister:
    def __init__(self):
        self.retailItemList=[]
        
    def purchase_item(self, RetailItem):
        self.retailItemList.append(RetailItem)
        
    def get_total(self):
        total = 0
        for item in self.retailItemList:
            total += item.price
        return "%0.2f"%(total)
    
    def show_items(self):
        for item in self.retailItemList:
            print(item.description)
    def clear(self):
        self.retailItemList=[]

#Exercise 8
class Question:
    def __init__(self,question,opt1,opt2,opt3,opt4,ans):
        self.question = question
        self.option1 = opt1
        self.option2 = opt2
        self.option3 = opt3
        self.option4 = opt4
        self.ans = ans
    

#Call this method for exercise 7
def shopping():
    print("Welcome to ABC market.")
    print("\nJacket","$59.95")
    print("Designer Jeans","$34.95")
    print("Shirt","$24.95")
    print("\nIf you're done shopping, enter q")
    A = CashRegister()
    
    while True:
        item = input("\nWhat item would you like to buy? ")
        if item == "Jacket":
            A.purchase_item(itm1)
        elif item == "Designer Jeans":
            A.purchase_item(itm2)
        elif item == "Shirt":
            A.purchase_item(itm3)
        else:
            break
    print("\nList of items you've selected for purchase:")
    A.show_items()
    print("\nTotal price: ",A.get_total())
    print("Good bye!")

#Call this method for exercise 8
def trivia():
    q1 = Question("On a scale of 1 to 10, how stupid is this question?",1,2,3,10,4)
    q2 = Question("Is 10 questions too many to make up?","Yes","No","Not Sure","Whatever",1)
    q3 = Question("What year is it?","Forever 21","2018","2019","Not Sure",2)
    q4 = Question("What time is it?","7pm","5am","3am","Time for you to get a watch!",4)
    q5 = Question("What OS do you use?","macOS is Best","Windows and I hate it","Linux cuz I'm weird","None of the above",4)
    q6 = Question("What video games do you play?","League of Legends","Fortnite","Dota","I have no time for games. School is too important",4)
    q7 = Question("On a scale of 1 to 10, how badly do you want to be hired?","5","9","10","10000000",4)
    q8 = Question("What do you do on your free time?","Chat","Code","Eat","Sleep",2)
    q9 = Question("What is the capital of Canada before Ottawa?","Quebec","Ottawa has been the only chosen capital","Idk","Toronto",1)
    q10 = Question("What is your name?","bruh that's too personal","bro, cmon.","are you serious you forgot my name already","wow, that's rude",2)

    triviaLst = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
    print("Welcome to this simple trivia game!!")
    p1Lst = []
    p2Lst = []
    correctCnt1=0
    correctCnt2=0
    for i in range(10):
        print("\n")
        print(triviaLst[i].question)
        print("1)",triviaLst[i].option1)
        print("2)",triviaLst[i].option2)
        print("3)",triviaLst[i].option3)
        print("4)",triviaLst[i].option4)
        if i == 4:
            print("Player 2's Turn!")
        ans = int(input("What is the correct answer? (Choose 1,2,3 or 4) "))
        if i > 4:
            p2Lst.append(ans)
            if ans == triviaLst[i].ans:
                correctCnt2 += 1
        else:
            p1Lst.append(ans)
            if ans == triviaLst[i].ans:
                correctCnt1 +=1

    if correctCnt2 > correctCnt1:
        print("Player 2 is the winner with",correctCnt2,"points!")
        print("Player 1:",correctCnt1,"points.")
    elif correctCnt2 == correctCnt1:
        print("Players tied at",correctCnt2,"points!")
    else:
        print("Player 1 is the winner with", correctCnt1,"points!")
        print("Player2:",correctCnt2,"points.")
    
            
        
        
