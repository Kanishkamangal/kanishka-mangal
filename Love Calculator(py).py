print("Welocme to Love Calculator")
name1=input("What is your name? ")
print(name1)
name2=input("What is their name? ")
print(name2)
t=(name1+name2).count("t")
r=(name1+name2).count("r")
u=(name1+name2).count("u")
e=(name1+name2).count("e")
true= t+r+u+e
l=(name1+name2).count("l")
o=(name1+name2).count("o")
v=(name1+name2).count("v")
e=(name1+name2).count("e")
love=l+o+v+e
LoveScore= int(str(true)+str(love))
if LoveScore<10 or LoveScore>90:
    print(f"your score is {LoveScore}%, you go together like coke and mentos")
elif LoveScore>=40 and LoveScore<=50:
    print(f"your score is {LoveScore}%, you are alright together")
else:
    print(f"your score is {LoveScore}%")




