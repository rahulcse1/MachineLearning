#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:59:37 2022

@author: amar
"""

welcome = '''
    Hello world
    this is amar jeet
    we are learning python for machine learning
    i am a backend developer
    java spring boot microservices react 
'''

print (welcome)

s_demo = 'amarjeet'
print(s_demo[:3])
print(s_demo[1:-1])

print(len(s_demo))

i = 1
while(i <= 10):
    print('*' * i)
    i += 1

for item in s_demo:
    print(item)
    
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# 2 lines break after function def 

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print('move')
        
    def draw(self):
        print('draw')
        
p1 = Point(10, 20)
p1.move()
p1.draw()
print(p1.x)

class Person:
    
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'hi i am {self.name}')

amar = Person("Amar")
amar.talk()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    