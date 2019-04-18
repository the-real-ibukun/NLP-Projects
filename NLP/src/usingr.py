import re

item = 'b Nigeria xe2 x80 x99s Tough Decision Former Dictator or Alleged Kleptocrat Buhari Atiku'

x =  ' '.join(re.sub("^b|x\w*\d*"," ",  str(item)).split())

print(x)