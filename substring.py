#get the input from user
n=input()
#check if user entered is alphabets or not
if(n.isalpha()==True):
    #if user entered in a upper case convert into lower case
    b=n.lower()
    #it set is used to remove the distint elements
    s=set(b)
    print(len(s))
else:
    print("please enter alphabets")
