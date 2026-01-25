def con(a,b):
    if a==1:
        student=0.3
        if b==1:
            dining=0.75
        else:
            dining=0.25
    if a==2:
        student=0.7
        if b==1:
            dining=0.6
        else:
            dining=0.4
        print("Probability of B: ",dining)
    prob=student*dining
    return round(prob,3)
print("Check the probabilty of an event occuring, Enter your choices")
print("Is the student a freshmen?(Y/N)")
a=int(input("Enter your Choice.(1/2)"))
print("Is student is eating in dining room?(Y/N)")
b=int(input("Enter your Choice.(1/2)"))
print("Probability of both the events occuring: ",con(a,b))