import math

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


def has_congruence_relation(a, b, n):
  """
  Defines if the integer a and the integer b has a congruence relation modulo n.

  Rule:
  For a given positive integer n, two integers a and b are called congruent modulo n
  if a-b is divisible by n (or equivalently if a and b have the same remainder when divided by n).

  This algorithm uses the second rule, calculating the remainders and comparing.

  Keyword arguments:
  a -- an integer
  b -- another integer
  n -- another integer (modulo)
  """

  remainder_a = a % n
  remainder_b = b % n
  return remainder_a == remainder_b


def prime(n) :
  """
  Defines if an integer is a prime number or not.

  Keyword arguments:
  n -- an integer

  Return value: boolean
  """

  x = abs(n)
  if x == 1 or x < 1 :
    return False
  
  square = math.trunc(math.sqrt(x))
  i = square
  while i >= 1 :
    if i == 1 :
      return True
    elif x % i == 0 :
      return False
    else :
      i -= 1


def distance_between_points(x1, y1, z1, x2, y2, z2) :
  """
  Calculates the distance between two points in space (3D).
  To use this function in 2D, pass both z1 and z2 as 0.

  Keyword arguments:
  x1 - x position of point 1
  y1 - y position of point 1
  z1 - z position of point 1
  x2 - x position of point 2
  y2 - y position of point 2
  z2 - z position of point 2
  """

  distance_x = (x2 - x1) * (x2 - x1)
  distance_y = (y2 - y1) * (y2 - y1)
  distance_z = (z2 - z1) * (z2 - z1)
  distance = math.sqrt(distance_x + distance_y + distance_z)
  return distance

