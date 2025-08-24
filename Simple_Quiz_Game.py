print("Welcom to the simple quiz game!")
score=0
print("\n Quetion.1: What is the capital of india?")
answer1=input("a.Mumbai\nb.Delhi\nc.Kolkata\nd.Chennai\n")
if answer1.lower()=="b" or answer1.lower()=="delhi":
    print("correct answer!\n")
    score+=1
else:
    print("wrong answer!,The correct answer is delhi\n")
print("\n Quetion.2:What was the language of this code? ")
answer2=input("a.c\nb.JAVA\nc.Python\nd.C++")
if answer2.lower()=="c" or answer2.lower()=="python":
    print("Correct answer!\n")
    score+=1
else:
    print("Wrong answer!, The correct answer is Python")
print("\n Quetion.3 What is 5+6?")
answer3=input("a.10\nb.5\nc.11\nd.4")
if answer3.lower()=="c" or answer3.lower()=="11":
    print("Answer correct!\n")
    score+=1
else:
    print("Wrong answer!,the Correct answer is 11")
print(f"\n Your final score is {score} out of 3")
print("Thank you for playing game!")
    