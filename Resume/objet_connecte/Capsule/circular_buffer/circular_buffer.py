from __future__ import annotations
from typing import Iterable, TypeVar, Generic



T = TypeVar('T')
"""A generic type alias for any type."""



class CircularBuffer(Generic[T]):
    """A circular buffer is a data structure that uses a single, fixed-size 
    buffer as if it were connected end-to-end.
    
    The buffer is treated as a circular data structure, meaning that the buffer 
    is logically contiguous and wrapped around. This means that the buffer is 
    treated as though the memory is contiguous and circular in nature.
    
    The buffer has a fixed capacity, and when the buffer is full, pushing a new 
    element will overwrite the oldest element.
    
    The buffer is implemented using a list of fixed size, and the buffer is 
    treated as a circular list.
    
    The buffer implement the following :
     - dunder methods:
       - __str__()
       - __repr__()
       - __format__() :
         - size
         - capacity
         - load
         - raw
       - __len__() : 
         - get the number of elements in the buffer
         - this value is fixed after the buffer is fully filled (via push method)
       - __getitem__(index) : 
         - get the element at the given index
         - the index can be negative
         - the index represent the circular index and not the physical index
       - __setitem__(index, value) : set the element at the given index
         - set the element at the given index
         - the index can be negative
         - the index represent the circular index and not the physical index
       - __iter__() : get an iterator over the elements in the buffer
         - return a facade iterator over the buffer
         - the iterator is a class defined inside the CircularBuffer class
         - the iterator stop when all elements are visited once
     - properties:
         - capacity : get the capacity of the buffer
         - size : get the number of elements in the buffer
         - is_empty : check if the buffer is empty
         - is_full : check if the buffer is full
     - methods:
         - push(value) : push a new element to the buffer
         - pop(value) : remove the last element from the buffer
         - clear() : remove all elements from the buffer
    """
    
    # to do : add init_values # def __init__(self, *, capacity : int, init_values : None | T | Iterable[T] = None) -> None:
    def __init__(self, capacity : int) -> None:
        """Create a new circular buffer with the given capacity.
        
        Args:
            capacity (int): the capacity of the buffer, must be strictly positive
            
        Raises:
            TypeError: if the capacity is not an int
            ValueError: if the capacity is not strictly positive
        
        Example as doctest :
        >>> data = CircularBuffer(capacity = 5)
        >>> len(data)
        0
        >>> data.push(10)
        >>> data.push(9)
        >>> len(data)
        2
        >>> data[0], data[1]
        (10, 9)
        >>> data[-1]
        9
        >>> data.clear()
        >>> len(data)
        0
        >>> data.push(10)
        >>> data.push(9)
        >>> data.push(8)
        >>> data.push(7)
        >>> for value in data:
        ...    print(value, end='_|_')
        10_|_9_|_8_|_7_|_
        """
        if not isinstance(capacity, int):
            raise TypeError('capacity must be an int')
        if capacity <= 0:
            raise ValueError('capacity must be strictly positive')
                
        self._capacity : int = capacity
        self._data : list[CircularBuffer.T | None] = [None] * self._capacity # pre-allocate the memory!
        self._first : int = 0
        self._size : int = 0
        
    def __str__(self) -> str:
        """Get the string representation of the buffer."""
        if self.size < 4:
            txt = ', '.join(str(value) for value in self)
        else:
            txt = str(self[0])
            for i in range(1, 3):
                txt += f', {self[i]}'
            txt += ', ...'
        return f'<{txt}>'
    
    def __repr__(self) -> str:
        """Get the string representation of the buffer."""
        return f'{self.__class__.__name__}(capacity = {self._capacity}) at {id(self):#x}'
    
    def __format__(self, format_spec : str) -> str:
        """Get the formatted representation of the buffer."""
        match format_spec:
            case 'size':
                return str(self._size)
            case 'capacity':
                return str(self._capacity)
            case 'load':
                return f'{self._size} / {self._capacity} ({self._size / self._capacity * 100.0:.1f} %)'
            case 'full':
                return f"<{', '.join(str(value) for value in self)}>"
            case 'raw':
                return str(self._data)
            case _:
                return str(self)
        
    def _index_of(self, index: int) -> int:
        """Get the physical index of the given logical circular index."""
        if index < 0:
            index = self._size + index
        if not 0 <= index < self._size:
            raise IndexError(f'index out of range, {index} was given for a size of {self._size}')
        return (self._first + index) % self._capacity
        
    def __getitem__(self, index : int) -> T:
        """Get the element at the given index."""
        return self._data[self._index_of(index)]

    def __setitem__(self, index : int, value : T) -> None:
        """Set the element at the given index."""
        self._data[self._index_of(index)] = value

    def __len__(self) -> int:
        """Get the number of elements in the buffer."""
        return self._size
    
    def __contains__(self, value : T) -> bool:
        """Check if the buffer contains the given value."""
        # return value in self._data[self._first:self._first + self._size] or value in self._data[:self._capacity - (self._first + self._size)]
        if self.is_empty:
            return False
        elif self.is_full:
            return value in self._data
        elif self._first + self._size <= self._capacity:
            return value in self._data[self._first:self._first + self._size]
        else:
            return value in self._data[self._first:] or value in self._data[:self._capacity - self._first]
    
    class _Iterator:
        """A facade iterator over the elements in the buffer."""
        def __init__(self, circular_buffer : CircularBuffer) -> None:
            """Create a new iterator over the given circular buffer."""
            self._buffer = circular_buffer
            self._index = 0
            
        def __next__(self) -> T:
            """"Get the next element in the buffer."""
            if self._index >= self._buffer._size:
                raise StopIteration
            value = self._buffer[self._index]
            self._index += 1
            return value
    
    def __iter__(self) -> CircularBuffer._Iterator:
        """Get an iterator over the elements in the buffer."""
        return CircularBuffer._Iterator(self)
    
    @property
    def capacity(self) -> int:
        """Get the capacity of the buffer."""
        return self._capacity
    
    @property
    def size(self) -> int:
        """Get the number of elements in the buffer."""
        return self._size
    
    @property
    def is_empty(self) -> bool:
        """Check if the buffer is empty."""
        return self._size == 0
    
    @property
    def is_full(self) -> bool:
        """Check if the buffer is full."""
        return self._size == self._capacity
    
    def push(self, value : T) -> None:
        """push a new element to the buffer.
        
        If the buffer is full, the oldest element will be overwritten.
        
        Args:
            value (T): the value to push to the buffer
        """
        index = (self._first + self._size) % self._capacity
        self._data[index] = value
        if self.is_full:
            self._first = (self._first + 1) % self._capacity
        else:
            self._size += 1
        
    def pop(self) -> None:
        """Remove the last element from the buffer.
        
        If the buffer is empty, an IndexError will be raised.
        
        Raises:
            IndexError: if the buffer is empty
        """
        if self.is_empty:
            raise IndexError('pop from an empty buffer')
        self._first = (self._first + 1) % self._capacity
        self._size -= 1
        
    def clear(self) -> None:
        """Remove all elements from the buffer.
        
        Clear the content without changing the capacity.
        """
        self._first = 0
        self._size = 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()

