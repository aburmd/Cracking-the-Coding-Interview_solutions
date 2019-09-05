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
