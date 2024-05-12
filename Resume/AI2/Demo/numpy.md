
# NumPy Array Operations in Python

This document outlines various operations performed with NumPy arrays, demonstrating creation, reshaping, and basic arithmetic operations.

## Importing NumPy

```python
import numpy as np
```

## Creating Arrays

- **Simple Array Creation**:
  ```python
  a = np.array([1, 2, 4, 8, 6])
  ```

- **Creating an Array with `arange`**:
  ```python
  a = np.arange(12)
  ```

## Array Manipulations

- **Reshaping an Array**:
  ```python
  ar = a.reshape(3, 4)
  ```

- **Attempt to Reshape Incorrectly** (leads to an error because the new shape must align with the number of elements in the array):
  ```python
  a.reshape(3, 5)  # ValueError: cannot reshape array of size 12 into shape (3,5)
  ```

## Working with Matrix (2D Arrays)

- **Creating a Zero Matrix**:
  ```python
  m = np.zeros((4, 4))
  ```

- **Modifying Elements**:
  ```python
  m[2][3] = 5
  m[1, 2] = 77
  ```

- **Matrix Element-wise Operations**:
  ```python
  m[1] - m[2]  # Element-wise subtraction
  m[1]**2      # Element-wise squaring
  ```

## Generating Random Numbers

- **Using NumPy's Random Generator**:
  ```python
  default = np.random.default_rng(seed=23)
  a = default.integers(low=0, high=10, size=(5,5))
  ```

## Defining Functions for Array Operations

- **Function to Compute the Sum of Differences Between Arrays**:
  ```python
  def somme_difference(u, v):
      return np.sum(u-v)
  ```

- **Comparing Rows Within a Matrix**:
  ```python
  for i in range(a.shape[0]):
      for j in range(a.shape[0]):
          print(f'somme_difference(a[{i}], a[{j}]) = {somme_difference(a[i], a[j])}')
  ```

This summary showcases the flexibility of NumPy arrays for scientific computing, from handling multi-dimensional data to performing complex array operations efficiently.
