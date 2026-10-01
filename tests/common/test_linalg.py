import numpy as np

def test_identity_matrix():
  I = np.eye(3)
  assert np.allclose(I @ I, I)

def test_square_root():
  sqrt_2 = np.sqrt(2)
  assert abs(sqrt_2**2 - 2.0) < 1e-12
