# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:00:25 2022

@author: mahmoud lotfi
"""

from calculator import Calculator

# tests addition method in Calculator
def test_add():
    x,y = 1,2
    cal = Calculator(x, y)
    assert cal.add() == x + y, "Add method doesnot work"
    
# tests subtraction method in Calculator
def test_sub():
    x,y = 1,2
    cal = Calculator(x, y)
    assert cal.sub() == x + y, "subtraction method doesnot work"

# tests subtraction method in Calculator
def test_sub():
    x,y = 1,2
    cal = Calculator(x, y)
    assert cal.mul() == x + y, "multiplication method doesnot work"    

# tests subtraction method in Calculator
def test_sub():
    x,y = 1,2
    cal = Calculator(x, y)
    assert cal.div() == x + y, "division method doesnot work"