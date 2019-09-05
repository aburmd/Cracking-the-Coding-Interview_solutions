#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
#EXAMPLE
#Input: Tact Coa
#Output: True (permutations: "taco cat", "atco eta", etc.) Hints:#106,#121,#134,#136

def isPalindrome(string):
	for i in range(0,len(string)-1):
		if string[i]!=string[len(string)-1-i]:
			return False;
	return True;


print(isPalindrome('malayalam'));
print(isPalindrome('tamil'));
print(isPalindrome('hanunah'));


		
