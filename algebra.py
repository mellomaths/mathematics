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
  if remainder == 0:
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

  return a % n == b % n


def is_prime(n) :
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
  while i >= 1:
    if i == 1:
      return True
    elif x % i == 0:
      return False
    else:
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

  # if is_prime(n):
  #   return n - 1
  
  coprimes = []
  for i in range(n):
    if are_coprime(i, n):
      coprimes.append(i)
  
  return len(coprimes)


def prime_factorization(n):
  """
  Prime factorization is the decomposition of a composite number into a product of prime numbers.

  Keyword arguments:
  n -- an integer
  
  Returns: a list of tuples (a, x), "a" being the prime number and "x" the integer of power, which mean a ** x, "a" to the power of "x"
  """
  factorization = []
  
  if is_prime(n):
    return [(n, 1)]

  x = n
  i = 2
  factor = 0
  while x != 1:
    if is_prime(i) and x % i == 0:
      x = x / i
      factor += 1
      if factor > 1:
        factorization.pop()
        factorization.append((i, factor))
      else:
        factorization.append((i, factor))
    else:
      i += 1
      factor = 0

  return factorization


def fermat_factorization(n) :
  """
  Given an odd integer n, finds 2 factors of n using
  Fermat's Algorithm, or concludes that n is a prime number

  Keyword arguments:
  n -- an integer
  
  Returns: two integers or False in case n is a prime
  """

  if n % 2 == 0 :
    return 2, n//2

  x = int(math.sqrt(n))
  if x ** 2 == n :
    return x
  
  y = 0.1
  while (y != int(y) and x <= (n + 1)/2) :
    x += 1
    y = math.sqrt(x**2 - n)

  if x >= (n + 1)/2 :
    return False

  return int(x - y), int(x + y)


def multiplicative_order(a, n):
  """
  Given an integer a and a positive integer n coprime to a, 
  the multiplicative order of a modulo n is the smallest positive integer k with

  a ** k congruent 1 (mod n)

  Keyword arguments:
  a -- an integer
  n -- an integer (modulo)
  
  Returns: an integer (k)
  """

  i = 2
  while (a ** i) % n != 1:
    i += 1

  return i


def newton_raphson(p, f, df, precision, max_iteration) :
    """
    Defines an approximate value as root of a function f
    based on Newton-Raphson Method

    Keyword arguments:
    p -- initial point
    f -- function we want to find a root
    df -- derivative of f
    precision -- accuracy of the estimate
    max_iteration -- maximum number of iterations

    Returns:
    An estimate for a root of f
    """
    
    for i in range(0, max_iteration) :
        next = p - (f(p) / df(p))
        if (abs(f(next)) < precision) :
            return next
        p = next

    return "Error"


def bisection_method(a, b, f, precision) :
    """
    Defines an approximate value as root of a function f
    based on Bisection Method

    Arguments:
    a -- lower bound of the interval
    b -- upper bound of the interval
    f -- function we want to find the root
    precision -- accuracy of the estimate

    Returns:
    An estimate for a root of f
    """
    
    maxIteration = int(((math.log(b - a) - math.log(precision)) / math.log(2))) + 1
    
    for i in range(0, maxIteration) :
        p = (a + b) / 2
        if (f(p) == 0 or abs(f(p)) < precision) :
            return p
        if (f(a) * f(p) < 0) : 
            b = p
        else :
            a = p
        if ((i + 1) == maxIteration) :
            return p
