# -*- coding: utf-8 -*-
"""Reverse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lb0Yq3CzznrNqGzv02wO_aLRI09iEx6x
"""

#Reverse each word of String
string="Hello World"
a=string[-1: :-1]
print(a)

#Reverse string
string="Hello World"
a=string.split()
b=a[-1: :-1]
c=" ".join(b)
print(c)