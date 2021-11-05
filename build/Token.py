class Token(object):
  def __init__(self, type, value):
    self.type = type
    self.value = value
  def __str__(self):
    return "Token Value %s Type %s" %(self.value, self.type)


