
def det2x2(A):
  assert len(A) == 2
  assert len(A[0]) == 2
  assert len(A[1]) == 2

  a11, a12 = A[0]
  a21, a22 = A[1]

  return a11 * a22 - a21 * a22
