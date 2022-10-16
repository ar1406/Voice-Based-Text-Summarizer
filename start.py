import text2voice as t2v
import main

s="*"*100
e="-"*1001
print(s)
print("Welcome to Voice based text summarization system (Human Computer Interaction Project)")
print(e)
t2v.speechTrans("Welcome to Voice based text summarization system (Human Computer Interaction Project)")
print("Contributors -\n 1. Aditya Roshan \n 2. Mayank Tiwary \n 3.  Sandeep Yadav \n 4. Aditya Nalini \n 5. Aniket Mishra " )
t2v.speechTrans("Contributors:  Aditya Roshan Mayank Tiwary Sandeep Yadav Aditya Nalini Aniket Mishra ")
print("\nInstructions - \n1.Make Sure python3 is installed and added to the path.\n2.If not check the python location by running location.bat file \n3.Now you need to run req.bat file to download all the dependencies.\n4.After Installing all dependencies press 1 to start with the summarizer.")
n=int(input())

while n!=1:
    print("Not a valid input")
    t2v.speechTrans("Not a valid input")
    n=int(input("Enter valid input-"))

if n==1:
    main.final()
