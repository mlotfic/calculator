# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:00:25 2022

@author: mahmoud lotfi
"""
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'src')


from calculator_mlotfic import calculator

# tests addition method in Calculator
def test_add():
    x,y = 1,2
    cal = calculator.Calculator(x, y)
    assert cal.add() == x + y, "Add method doesn't work"
    
# tests subtraction method in Calculator
def test_sub():
    x,y = 1,2
    cal = calculator.Calculator(x, y)
    assert cal.sub() == x - y, "subtraction method doesn't work"

# tests multiplication method in Calculator
def test_mul():
    x,y = 1,2
    cal = calculator.Calculator(x, y)
    assert cal.mul() == x * y, "multiplication method doesn't work"    

# tests division method in Calculator
def test_div():
    x,y = 1,2
    cal = calculator.Calculator(x, y)
    assert cal.div() == x / y, "division method doesn't work"

