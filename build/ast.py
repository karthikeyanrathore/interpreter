#!/usr/bin/env python3
from Token import Token
from objects import PLUS, MINUS, MULT, DIV, LP, RP, INTEGER, EOF

class AST(object):
  pass


class BinNode(AST):
  def __init__(self, left, op, right):
    self.left = left
    self.token = op
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
    sum = ""
    while current_char.isdigit():
      sum += str(current_char)
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
    else:
      return Token(EOF, None)
 
class Parser(Lexer):
  def push_check(self , token_type):
    if self.current_token.type == token_type:
      self.current_token = self.get_token()
    else:
      return "error"
  
  # Numbers (integers)
  def factor(self):
    if self.current_token.type == INTEGER:
      token = (self.current_token)
      self.push_check(INTEGER)
      return Num(token)

    elif self.current_token.type == LP:
      self.push_check(LP)
      node = self.solve()
      self.push_check(RP)
      return node
  
  # Operations ( * , // )
  def term(self):
    node = self.factor()
    while self.current_token.type in (MULT , DIV):
      token = self.current_token
      if self.current_token.type == MULT:
        self.push_check(MULT)
      elif self.current_token.type == DIV:
        self.push_check(DIV)
      node = BinNode(node, token , self.factor())
    return node 
  
  # Expression
  def solve(self):
    node = self.term()
    while self.current_token.type in (PLUS, MINUS):
      token = self.current_token
      if self.current_token.type == PLUS:
        self.push_check(PLUS)
      elif self.current_token.type == MINUS:
        self.push_check(MINUS)
      node = BinNode(node , token , self.term()) 
    return node 


def unit(inp):
 x = Parser(inp)
 return (x.solve())


if __name__ == "__main__":
  x = Parser("2+3")
  node = x.solve()
  


