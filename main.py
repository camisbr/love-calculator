print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



names_combined = name1 + name2
names_lower_case = names_combined.lower()
t = names_lower_case.count("t")
r = names_lower_case.count("r")
u = names_lower_case.count("u")
e = names_lower_case.count("e")
l = names_lower_case.count("l")
o = names_lower_case.count("o")
v = names_lower_case.count("v")

true_cont = t + r + u + e
love_cont = l + o + v + e
score = int(str(true_cont) + str(love_cont))
if (score <= 10) or (score >= 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
