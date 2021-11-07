#!/usr/bin/env python3
from  ast import unit
import unittest

print(unit("1 + 1"))

class ArithmeticMethods(unittest.TestCase):

  def test_add(self):
    self.assertEqual(unit("9 + 9 + 1 + 9"), 9 + 9 + 1 + 9)
  def test_subtract(self):
    self.assertEqual(unit("5 - 1 + 8 - 2"), 5 - 1 + 8 - 2)
  def test_multiply(self):
    self.assertEqual(unit("7 * 6 + 9 - 3 * 5"), 7 * 6 + 9 - 3 * 5)
  def test_division(self):
    self.assertEqual(unit("5 * 7 / 6 * 7 + 1"), 5 * 7 // 6 * 7 + 1)
  def test_multi_digit(self):
    self.assertEqual(unit("12 + 45 * 54 / 90 * 76 + 100"),12 + 45 * 54 // 90 * 76 + 100)
  def test_whitespace(self):
    self.assertEqual(unit("  32   +   400   *   1004 + 244 -  100  /  9000  *  6500   *  20000  "),32 + 400  * 1004 + 244 - 100 // 9000* 6500 * 20000)

  def test_parenthesis(self):
    self.assertEqual(unit("7 + (((3 + 2)))"), 7 + (((3 + 2))))
    self.assertEqual(unit("7 + 3 * (10 / (12 / (3 + 1) - 1))"), 7 + 3 * (10 // (12 // (3 + 1) - 1)))
    self.assertEqual(unit("7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)"), 7 + 3 * (10 // (12 // (3 + 1) - 1)) // (2 + 3) - 5 - 3 + (8))


if __name__ == "__main__":
  unittest.main()
