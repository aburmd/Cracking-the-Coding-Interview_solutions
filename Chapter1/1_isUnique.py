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
