"""
Write a function that satisfies the following docstring:

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
For example, if

largest_odd_times([2,2,4,4]) returns None
largest_odd_times([3,9,5,3,5,3]) returns 9
"""

def largest_odd_times(L):
  n=0
  largest =0
  for i in L:
    n=L.count(i)
    if n%2 !=0:
      if largest<i:
        largest=i
  if largest !=0:
    return largest

