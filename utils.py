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
