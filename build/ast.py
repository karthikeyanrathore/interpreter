#!/usr/bin/env python3
from Token import Token
from objects import PLUS, MINUS, MULT, DIV, LP, RP, INTEGER, EOF

class AST(object):
  pass


class BinNode(AST):
  def __init__(self, left, op, right):
    self.left = left
    self.token = self.op = op
    self.right = right
  

class Num(AST):
  def __init__(self, token):
    self.token = token
    self.value = token.value

class Lexer(object):
  def __init__(self, inp):
    self.str = inp
    self.pos = 0
    self.current_token = self.get_token()
    
  def forward(self):
    if len(self.str) - 1 <= self.pos:
      return 0
    else:
      self.pos += 1
      return 1

  def multidigit(self):
    current_char = self.str[self.pos]
    sum = 0
    while current_char.isdigit():
      sum += int(current_char)
      if self.forward():
        current_char = self.str[self.pos]
      else:
        self.pos += 1
        break
    return sum

  def get_token(self):
    if len(self.str) - 1 < self.pos:
      return Token(EOF, None)

    current_char = self.str[self.pos]
    while current_char.isspace():
      if self.forward():
        current_char = self.str[self.pos]
      else:
        break

    if current_char.isdigit():
      return Token(INTEGER, self.multidigit())

    if current_char == "+":
      self.pos += 1
      return Token(PLUS, "+")
    if current_char == "-":
      self.pos += 1
      return Token(MINUS, "-")
    if current_char == "*":
      self.pos += 1
      return Token(MULT, "*")
    if current_char == "/":
      self.pos += 1
      return Token(DIV, "/")
    if current_char == "(":
      self.pos += 1
      return Token(LP, "(")
    if current_char == ")":
      self.pos += 1
      return Token(RP, ")")

 
class Parser(Lexer):
  def push_check(self , token_type):
    if self.current_token.type == token_type:
      self.current_token = self.get_token()
    else:
      return "err"
  
  def factor(self):
    pass
  def term(self):
    pass

  def solve(self):
    #print( self.current_token )
    pass


if __name__ == "__main__":
  x = Parser("  83   + 91 + 100 ")
  x.solve()




