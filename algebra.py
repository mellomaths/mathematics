import math


def greatest_common_divisor(a, b):
  """
  Based on the Euclidean Algorithm, this function will calculate the greatest common divisor between two integers.

  Keyword arguments:
  a -- an integer
  b -- another integer

  Returns: an integer
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

  Returns: a boolean
  """

  remainder_a = a % n
  remainder_b = b % n
  return remainder_a == remainder_b


def prime(n) :
  """
  Defines if an integer is a prime number or not.

  Keyword arguments:
  n -- an integer

  Returns: a boolean
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


def are_coprime(a, b):
  """
  Two integers a and b are relatively prime, mutually prime, or coprime 
  if the only positive integer that evenly divides (is a divisor of) both of them is 1

  Keyword arguments:
  a -- an integer
  b -- another integer

  Returns: a boolean
  """
  return greatest_common_divisor(a, b) == 1


def phi(n):
  """
  Calculate how many relative primes there are up to a given integer.
  Euler's totient function counts the positive integers up to a given integer n that are relatively prime to n.

  Keyword arguments:
  n -- an integer

  Returns: an integer
  """

  if n == 1:
    return 1
  
  coprimes = []
  for i in range(n):
    if are_coprime(i, n):
      coprimes.append(i)
  
  return len(coprimes)
