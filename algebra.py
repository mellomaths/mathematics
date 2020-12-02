def greatest_common_divisor(a, b):
  """
  Based on the Euclidean Algorithm, this function will calculate the greatest common divisor between two integers.

  Keyword arguments:
  a -- an integer
  b -- another integer
  """
  remainder = a % b
  if (remainder == 0):
    return b
    
  return abs(greatest_common_divisor(b, remainder))

