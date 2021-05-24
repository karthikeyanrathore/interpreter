#!/usr/bin/env python3

INTEGER = "INTEGER"
PLUS = "PLUS"
EOF = "EOF"

class Token(object):
  def __init__(self , type , value):
    self.type = type
    self.value = value
  
  def __str__(self):
    return "Token( %s , %s )" % (self.type , self.value)



class Interpreter(object):
  def __init__(self , text):
    self.text = text
    self.pos = 0
    self.current_token = None
    self.current_char = self.text[self.pos]

  def error(self):
    raise Exception("Error parsing input")

  def advance(self):
    self.pos += 1
    if(self.pos > len(self.text) - 1):
      self.current_char = None
    else:
      self.current_char = self.text[self.pos]


  def skip_whitespace(self):
    while(self.current_char is not None and self.current_char.isspace()):
      self.advance();
    
  def get_next_token(self):
    while(self.current_char is not None):
      if(self.current_char.isspace()):
        self.skip_whitespace()
        continue
      
      if(self.current_char.isdigit()):
        token = Token(INTEGER , int(self.current_char))
        self.advance()
        return token

      if(self.current_char == '+'):
        token = Token(PLUS , self.current_char)
        self.advance()
        return token

      else:
        self.error()

    return Token(EOF , None)

  def eat(self , token_type):
    if(self.current_token.type == token_type):
      self.current_token = self.get_next_token();
    else:
      print(self.current_token.type , token_type)
      self.error()


  def expr(self):
    self.current_token = self.get_next_token()

    left = self.current_token;
    self.eat(INTEGER)

    op = self.current_token;
    self.eat(PLUS)

    right = self.current_token;
    self.eat(INTEGER)

    return left.value + right.value





def func():
  while(1):
    text = input('calc> ')
    analyze = Interpreter(text)
    print(analyze.expr())

    
if __name__ == "__main__":
  func()
















