# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:00:25 2022

@author: m
"""

from calculator_class import Calculator

# tests addition method in Calculator
def test_add():
    x,y = 1,2
    instance = Calculator(x, y)
    assert instance.add() == x + y, "Add method doesnot work"
    
# tests subtraction method in Calculator
def test_sub():
    x,y = 1,2
    instance = Calculator(x, y)
    assert instance.sub() == x + y, "subtraction method doesnot work"
        