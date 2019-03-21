height = 22
idk = list(" "*height)
import time


def christmas(symb0, symb1, symb2):
 top = """{0}\|/{0}-|-  MERRY CHRISTMAS!!!{0}/|\\""".format("\n" + (" "*(height-1)))
 print(top)
 temp = ""
 for i in range(height):
  temp += (" "*(height-i)) + (("".join(symb1*i)) + (symb0) + ("".join(symb2*i)))+"\n"
  topp = 0
 for i in range(int(height/3)):
  temp += (" "*height + symb0) + "\n"
 return temp 
 

symb0 = ["*", "+", "X", "O", "#", "I"]
symb1 = ["/", "[", "{", "("]
symb2 = ["\\", "]", "}", ")"][::-1]
a ,b  = 0, 0
for i in range(10):
 if a == len(symb1):
  a = 0
 if b == len(symb0):
  b = 0
 print(christmas(symb0[b], symb1[a], symb2[a]), end="\r")
 time.sleep(1)
 print("\n"*5)
 a += 1
 b += 1




