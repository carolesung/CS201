#File: assignment8.py
#Name: Carole (Chia Jung) Sung
#Date: Mar 20 2018
#Description: Programming exercises 4,5,6,8 from chapter 9

import os.path

#Question 4
def uniqueWords(file):
    '''Opens a specified text file and then displays a list of all
    the unique words found in the file.'''
    lst = []
    f = open(file,'r')
    for line in f:
        for word in line.split(" "):
            if word not in lst:
                lst.append(word)
    return lst

#Question 5
def wordFrequency(file):
    '''Reads contents of a text file and displays the
    frequency of each word.'''

    d = {}
    f = open(file,'r')
    for line in f:
        for word in line.split(" "):
            if word in d:
                d[word]+=1
            else:
                d[word] = 1
    keys = d.keys()
    for k in keys:
        print(k,"appeared",d[k],"time(s)")

#Question 6
def fileAnalysis(file1,file2):
    '''Reads the contents of two text files and compares them in
    the following ways:
    a. Displays a list of all the unique words contained in both files.
    b. Displays a list of the words that appear in both files.
    c. Displays a list of the words that appear in the 1st file but not
    the 2nd
    d. Displays a list of the words that appear in the 2nd file but
    not the 1st
    e. Displays a list of the words that appear in either the first
    or second file but not both'''
    d1 = []
    f1 = open(file1,'r')
    for line in f1:
        for word in line.split(" "):
            d1.append(word)
    
    d2=[]
    f2 = open(file2,'r')
    for line in f2:
        for word in line.split(" "):
            d2.append(word)

    print("Part a:", set(d1) | set(d2))
    print("Part b:", set(d1) & set(d2))
    print("Part c:", set(d1) - set(d2))
    print("Part d:", set(d2) - set(d1))
    print("Part e:", set(d1) ^ set(d2))
    
#Question 8
def emailDict():
    '''Keeps names and email addresses in a dictionary.
    Lets user look up a person's email address, add a new name
    and email address, change information and also delete an entry.'''
    if os.path.exists("/Users/edwinsung/Documents/METCS201/contacts.txt"):
        d = {}
        f = open("contacts.txt","r")
        for line in f:
            lst = line.split(" ")
            d[lst[0]]=lst[1]
    else:
        d={}
    while True:
        print("\nWelcome to your phone book.")
        print("a)Look up a person's email address")
        print("b)Add a new contact")
        print("c)Delete a contact")
        print("d)Quit")
        choice = input("\nPlease choose an option: ")
        if choice == "a":
            contact = input("\nWhat is the name of the contact you are looking for? ")
            if contact not in d:
                print("Contact not found!")
            else:
                print(d[contact])
        elif choice == "b":
            name = input("\nWhat is the new contact's name? ")
            email = input("\nWhat is the new contact's email? ")
            d[name]=email
            print("Contact Added!")
        elif choice == "c":
            contact = input("\nWhat is the name of the contact? ")
            if contact in d:
                d.pop(contact)
                print("Contact Deleted.")
            else:
                print("Contact not found!")
        elif choice == "d":
            break
        else:
            print("Please enter a valid choice.")
    print("Good bye!")
    f = open("contacts.txt","w")
    keys = d.keys()
    for k in keys:
        f.write(k+" "+d[k])
    f.close()
            
        
