from common.linalg import det2x2

def test_det2x2():
  A = [
    [1, 3],
    [0, 4]
  ]
  assert 4 == det2x2(A)
