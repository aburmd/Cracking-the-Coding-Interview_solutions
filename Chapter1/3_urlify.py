#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
#EXAMPLE
#Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith" Hints: #53, #118

def urlify(string):
	val=string;
	valList=val.split(" ");
	lastword=valList[-1];
	output=None
	conjuction='%20';
	for i in valList[:-1]:
		if not output:
			output=i+conjuction;
		else:
			output=output+i+conjuction;	
	return output+lastword


print(urlify("birthday cake was presented by abu"))
