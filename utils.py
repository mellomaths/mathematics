from typing import Any


def factorial(n):
  """
  Factorial is the product of all positive integers less than or equal to n.

  Keyword arguments:
  n -- an integer

  Returns: an integer
  """

  if n == 0:
    return 1
    
  return n * factorial(n - 1)


def fibonacci(n):
  """
  In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, 
  such that each number is the sum of the two preceding ones, starting from 0 and 1.

  Keyword arguments:
  n -- an integer

  Returns: an integer
  """

  if n <= 1:
    return n

  return fibonacci(n-1) + fibonacci(n-2)  


class Queue:

  def __init__(self) -> None:
    self.q = []

  def get(self) -> Any:
    return self.q.pop(0) 
  
  def add(self, element) -> None:
    self.q.append(element)
  
