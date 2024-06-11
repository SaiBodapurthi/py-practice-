n=int(input("enter a year : "))
if n%100==0 and n%400!=0:
    print("not leap year")
elif n%4==0:
    print("leap year")