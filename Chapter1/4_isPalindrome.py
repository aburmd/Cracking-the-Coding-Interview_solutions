def isPalindrome(string):
	for i in range(0,len(string)-1):
		if string[i]!=string[len(string)-1-i]:
			return False;
	return True;


print(isPalindrome('malayalam'));
print(isPalindrome('tamil'));
print(isPalindrome('hanunah'));


		
