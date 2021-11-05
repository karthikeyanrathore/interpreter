#!/usr/bin/env python3
import math
INTEGER="INTEGER"
PLUS="PLUS"
MINUS="MINUS"
EOF= "EOF"

class Token(object):
  def __init__(self, type, value):
    self.type = type
    self.value = value
  def __str__(self):
    return "Token Value %s Type %s" %(self.value, self.type)

class Interpreter(object):
  def __init__(self, inp):
    self.str = inp
    self.current_token = None
    self.pos = 0
  
  def forward(self):
    if self.pos >= len(self.str) - 1 :
      return 0
    else:
      self.pos += 1
      return 1

  def multidigit(self):
    sum = ""
    current_char = self.str[self.pos]
    while current_char.isdigit():
      sum+= str(current_char)
      if self.forward():
        current_char = self.str[self.pos]
      else:
        self.pos += 1
        break
    return sum
    
  def get_token(self):
    if self.pos > len(self.str) - 1:
      return Token(None, EOF)

    current_char = self.str[self.pos]
    if current_char.isdigit():
      token = Token(INTEGER,self.multidigit())
      return token

    if current_char == "+":
      token = Token(PLUS, (current_char))
      self.pos += 1
      return token
    
    if current_char == "-":
      token = Token(MINUS, (current_char))
      self.pos += 1
      return token
  
    else:
      return Token(None, EOF)
  
  def push_check(self, token_type):
    if token_type == self.current_token.type:
      self.current_token = self.get_token()
    else:
      print("error in pushing")
      exit()
    
  def solve(self):
    self.current_token = self.get_token()
    
    left = self.current_token
    print("left", self.current_token)
    self.push_check(INTEGER)
    
    mid = self.current_token
    print("mid", self.current_token)
    if self.current_token.type == PLUS:
      self.push_check(PLUS)
    if self.current_token.type == MINUS:
      self.push_check(MINUS)  

    right = self.current_token
    print("right", self.current_token)
    self.push_check(INTEGER)
    
    if mid.type == PLUS:
      return int(left.value)  + int(right.value)
    if mid.type == MINUS:
      return int(left.value)  -  int(right.value)





if __name__ == "__main__":
  while 1:
    inp = input("add> ")
    if inp == "exit":
      break
    x = Interpreter(inp)
    print(x.solve())


