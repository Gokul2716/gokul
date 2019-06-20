"""get the input from user"""
n=input()
"""if the user entered in a caps convert into smaller"""
low=n.lower()
"""convert the given input into set so that duplicates are been removed"""
s=set(low)
"""print the length of set"""
print(len(s))
