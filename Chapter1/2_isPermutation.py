import heapq

def isPermutation(string1,string2):
	a=[]
	b=[]
	for i in string1:
		heapq.heappush(a,i);
	for j in string2:
		heapq.heappush(b,j);
	while a:
		x=heapq.heappop(a);
		y=heapq.heappop(b);
		if x!=y:
			return False;
	return True;


print(isPermutation('abu','uba'))
print(isPermutation('malayalam','layalamma'))

#soln: using -->from collections import Counter


