#One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
#Given two strings, write a function to check if they are one edit (or zero edits) away.
#EXAMPLE
#pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false Hints:#23, #97, #130
import unittest
def oneeditReplace(s1,s2):
  edited=False;
  for c1,c2 in zip(s1,s2):
    if c1!=c2:
      if edited:
        return False;
      edited=True;
  return edited;

def oneeditInsert(s1,s2):
  index=min(len(s1),len(s2));
  i=0;
  if max(len(s1),len(s2)) - min(len(s1),len(s2)) > 1 or len(s1)==len(s2):
    return False;
  while i < min(len(s1),len(s2)):
    if s1[i]!=s2[i]:
      index=i
      i=min(len(s1),len(s2))-1
    i=i+1;
  if len(s1) > len(s2):
    s2=s2[:index]+s1[index]+s2[index:];
  elif len(s2) > len(s1):
    s1=s1[:index]+s2[index]+s1[index:];
  if s1==s2:
    return True;
  else:
    return False;

def oneAway(s1,s2):
  if s1==s2:
    return True;
  elif len(s1)==len(s2):
    return oneeditReplace(s1,s2);
  else:
    return oneeditInsert(s1,s2);

class Test(unittest.TestCase):
  '''Test Cases'''
  data=[('pales', 'pale', True),('pale', 'bale', True),('paleabc', 'pleabc', True),('pale', 'ble', False),('a', 'b', True),('', 'd', True),('d', 'de', True),('pale', 'pale', True),('pale', 'ple', True),('ple', 'pale', True),('pale', 'bale', True),('pale', 'bake', False),('pale', 'pse', False),('ples', 'pales', True),('pale', 'pas', False),('pas', 'pale', False),('pale', 'pkle', True),('pkle', 'pable', False),('pal', 'palks', False),('palks', 'pal', False),('pale','le',False)];
  def test_oneAway(self):
    for [test_s1,test_s2,expected] in self.data:
      actual = oneAway(test_s1,test_s2);
      self.assertEqual(actual,expected)

if __name__ == "__main__":
  unittest.main()



