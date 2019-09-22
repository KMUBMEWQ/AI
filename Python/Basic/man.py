# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:55:10 2019

@author: WEI QUN

P35
"""

class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def hello(self):
        print("Hello " + self.name +" "+ self.age + "!")
        
    def goodbye(self):
        print("Good-bye " + self.name +" "+self.age+ "!")
        
m = Man("WQ", "35")
m.hello()
m.goodbye()