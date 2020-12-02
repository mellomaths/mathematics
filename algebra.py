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

def primo(n) :
    #Recebe um número inteiro e retorna True caso ele seja primo ou False caso
    #seja composto.
    #A ideia é a variável j funcionar como limite para até onde testaremos o
    #resto da divisão de i por j. Só precisamos testar até a parte inteira da raiz
    #de i para definir se o número é ou não primo
    
    import math

    if n == 1 or n < 1 :
        return False
    
    i = n
    j = math.sqrt(i)
    j = math.trunc(j)

    while j >= 1 :
        if j == 1 :
            return True
        elif i % j == 0 :
            return False
        else :
            j -= 1
