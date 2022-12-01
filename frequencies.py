"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies={}
    for a in items: 
        a=str(a)
        if a in frequencies.keys(): 
            frequencies[a]+=1
        else:
            frequencies[a]=1 
    return frequencies
