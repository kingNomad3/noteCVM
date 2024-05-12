
# NumPy Matrix Operations and Vector Norms

This document demonstrates Python operations involving matrices using NumPy, particularly focusing on generating matrices, computing vector norms, and normalizing vectors.

## Importing NumPy

```python
import numpy as np
```

## Generating Random Matrices

- **Create a random integer matrix** with values from 0 to 2:
  ```python
  m = np.random.randint(0, 3, (5, 3))
  ```

## Operations

### Display the Matrix

- **Initial matrix**:
  ```python
  array([[1, 1, 1],
         [1, 1, 1],
         [0, 0, 0],
         [2, 1, 2],
         [2, 1, 2]])
  ```

- **New random matrix**:
  ```python
  array([[1, 2, 2],
         [1, 1, 0],
         [1, 2, 0],
         [2, 0, 0],
         [0, 1, 2]])
  ```

### Compute the Norms

- **Norm of the entire matrix** (Frobenius norm):
  ```python
  np.linalg.norm(m)  # 4.898979485566356
  ```

- **Row-wise norms** of the matrix:
  ```python
  np.linalg.norm(m, axis = 1)
  ```
  Output:
  ```
  array([3.        , 1.41421356, 2.23606798, 2.        , 2.23606798])
  ```

### Normalizing Rows

- **Normalize each row** of the matrix to have unit length:
  ```python
  (m.transpose()/np.linalg.norm(m, axis=1)).transpose()
  ```
  Resulting matrix:
  ```
  array([[0.33333333, 0.66666667, 0.66666667],
         [0.70710678, 0.70710678, 0.        ],
         [0.4472136 , 0.89442719, 0.        ],
         [1.        , 0.        , 0.        ],
         [0.        , 0.4472136 , 0.89442719]])
  ```

## Conclusion

These examples illustrate how to work with matrices in NumPy, including generating random matrices, calculating vector norms, and normalizing vectors for unit length. This capability is useful in various applications such as data normalization in machine learning and statistics.
