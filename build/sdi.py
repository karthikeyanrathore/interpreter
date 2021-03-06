#!/usr/bin/env python3
import math
from Token import Token
from objects import INTEGER, PLUS, MINUS, MULT, DIV, EOF, LP, RP

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
    while current_char.isspace():
      if self.forward():
        current_char = self.str[self.pos]
      else:
        break

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
    
    if current_char == "*":
      token = Token(MULT, (current_char))
      self.pos += 1
      return token
  
    if current_char == "/":
      token = Token(DIV, (current_char))
      self.pos += 1
      return token
   
    if current_char == "(":
      token = Token(LP, (current_char))
      self.pos += 1
      return token
  
    if current_char == ")":
      token = Token(RP, (current_char))
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
  
  def factor(self):
    result = None
    if self.current_token.type == INTEGER:
      result = int(self.current_token.value)
      self.push_check(INTEGER)
      return result
    
    elif self.current_token.type == LP:
      self.push_check(LP)
      result = self.solve()
      self.push_check(RP)
      return result

  def term(self):
    result = self.factor()
    while self.current_token.type in (MULT, DIV):
      if self.current_token.type == MULT:
        self.push_check(MULT)
        result *= self.factor() 
      
      elif self.current_token.type == DIV:
        self.push_check(DIV)
        result //= self.factor()
  
    return result

  def solve(self):
    #self.current_token = self.get_token()
    result = self.term()

    while self.current_token.type in (PLUS, MINUS):
      if self.current_token.type == PLUS:
        self.push_check(PLUS)
        result += self.term() 
      
      elif self.current_token.type == MINUS:
        self.push_check(MINUS)
        result -= self.term() 
    
    return result
   
    '''JUNK'''
    '''
    left = self.current_token
    print("left", self.current_token)
    self.push_check(INTEGER)
    
    mid = self.current_token
    print("mid", self.current_token)
    
    if self.current_token.type == PLUS:
      self.push_check(PLUS)
    if self.current_token.type == MINUS:
      self.push_check(MINUS)  
    if self.current_token.type == MULT:
      self.push_check(MULT)  
    if self.current_token.type == DIV:
      self.push_check(DIV)  
    
    right = self.current_token
    print("right", self.current_token)
    self.push_check(INTEGER)
   
    if mid.type == PLUS:
      return int(left.value)  + int(right.value)
    if mid.type == MINUS:
      return int(left.value)  -  int(right.value)
    if mid.type == MULT:
      return int(left.value)  *  int(right.value)
    if mid.type == DIV:
      return int(left.value)  /  int(right.value)
    '''

def unit(inp):
  x = Interpreter(inp)
  x.current_token = x.get_token()
  return (x.solve())


if __name__ == "__main__":
  while 1:
    inp = input("add> ")
    if inp == "exit":
      break
    x = Interpreter(inp)
    x.current_token = x.get_token()
    print(x.solve())


