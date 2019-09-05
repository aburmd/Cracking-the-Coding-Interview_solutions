#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
#Hints: #44, #7 7 7, #732


def isUnique(string):
	a=[];
	for i in string:
		if i in a:
			return False;
		else:
			a.append(i);
	return True;


print (isUnique('aaaaaa'))
print (isUnique('abcdefg'))
print (isUnique(''))
print (isUnique('abcdefghijklmnopqrstuvwxyzz'))
print (isUnique('abcdefghijklmnopqrstuvwxyz'))
