def Punctuation(string): 
  punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
  for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
  a=(string.lower())
  print a
  a=(a.split('. '))
  print a

string=raw_input("enter the string")
Punctuation(string)
