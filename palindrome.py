# -*- coding: utf-8 -*-
"""Palindrome.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/184jntoAdPfHbMRQDkJxnHJy8UO-1xfqd
"""

#Reverse Number or Palindrome Number
a=int(input("Enter a number: "))
temp=a;
s=0
while temp>0:
  r=temp%10
  s=s*10+r
  temp=temp//10
if (s == a):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Palindrome String
string="malayalam"
new=""
for i in string:
  new=i+new

if (string == new):
    print("Palindrome")
else:
    print("Not a Palindrome")