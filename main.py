day=int(input("enter a number from 1 to 7: "))
if day<7 or day>1:
    if day==1:
        print("monday")    
    elif day==2:
        print("thuesday")
    elif day==3:
        print("wednesday")
    elif day==4:
        print("thursday")
    elif day==5:
        print("friday")
    elif day==6:
        print("saturday")
    elif day==7:
        print("sunday")
else:
    print("try again")