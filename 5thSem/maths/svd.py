import numpy as np

def svd(A):
  C = np.dot(A.T, A)
  eigenvalues, eigenvectors = np.linalg.eigh(C)

  sorted_indices = np.argsort(eigenvalues)[::-1]
  eigenvalues = eigenvalues[sorted_indices]
  eigenvectors = eigenvectors[:, sorted_indices]


  sigma = np.sqrt(eigenvalues)


  left_singular_vectors = np.dot(A, eigenvectors)

  #i/sigma1 AV1


  left_singular_vectors /= np.linalg.norm(left_singular_vectors, axis=0)


  right_singular_vectors = eigenvectors

  return left_singular_vectors, sigma , right_singular_vectors

if __name__ == "__main__":

  A = np.array([[1, 2], [3, 4], [5,6]])
  U, S, V = svd(A)
  print("U:")
  print(U)
  print("S:")
  print(S)
  print("Vt:")
  print(V)