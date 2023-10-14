# -*- coding: utf-8 -*-
"""
Использую только переменную S. нерезание (S[1:2]) и конкатенацию (string + string)
выведите переменную  S = slam

"""

def change_string(s):
    s = s[:1] + s[4:] + s[2:4]
    return s
    
s = "spaml"
s = change_string(s)
print(s)



