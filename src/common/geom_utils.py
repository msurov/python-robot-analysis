from math import sqrt

def hypo(a : float, b : float) -> float:
  """
    returns hypotenuse of a squared triangle with sides a and b
  """
  return sqrt(a**2 + b**2)
