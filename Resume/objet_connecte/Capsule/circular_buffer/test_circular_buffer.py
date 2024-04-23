# from ..data_structure.circular_buffer import CircularBuffer
from circular_buffer import CircularBuffer

import unittest

class TestCircularBuffer(unittest.TestCase):
    
    def test_empty_buffer(self):
        buffer = CircularBuffer(capacity = 5)
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 0)
        self.assertTrue(buffer.is_empty)
        self.assertFalse(buffer.is_full)
        with self.assertRaises(IndexError):
            buffer[0]
        with self.assertRaises(IndexError):
            buffer[1]
        with self.assertRaises(IndexError):
            buffer[-1]
        with self.assertRaises(IndexError):
            buffer[5]
        with self.assertRaises(IndexError):
            buffer[-5]

    def test_push_elements_buffer_not_at_capacity(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 3)
        self.assertFalse(buffer.is_empty)
        self.assertFalse(buffer.is_full)
        self.assertEqual(buffer[0], 1)
        self.assertEqual(buffer[1], 2)
        self.assertEqual(buffer[2], 3)
        self.assertEqual(buffer[-1], 3)
        self.assertEqual(buffer[-2], 2)
        self.assertEqual(buffer[-3], 1)
        with self.assertRaises(IndexError):
            buffer[3]
        with self.assertRaises(IndexError):
            buffer[-4]

    def test_push_elements_buffer_at_capacity(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 5)
        self.assertFalse(buffer.is_empty)
        self.assertTrue(buffer.is_full)
        self.assertEqual(buffer[0], 1)
        self.assertEqual(buffer[1], 2)
        self.assertEqual(buffer[2], 3)
        self.assertEqual(buffer[-1], 5)
        self.assertEqual(buffer[-2], 4)
        self.assertEqual(buffer[-3], 3)
        with self.assertRaises(IndexError):
            buffer[10]
        with self.assertRaises(IndexError):
            buffer[-10]
            
    def test_push_elements_buffer_over_capacity(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.push(6)
        buffer.push(7)
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 5)
        self.assertFalse(buffer.is_empty)
        self.assertTrue(buffer.is_full)
        self.assertEqual(buffer[0], 3)
        self.assertEqual(buffer[1], 4)
        self.assertEqual(buffer[2], 5)
        self.assertEqual(buffer[-1], 7)
        self.assertEqual(buffer[-2], 6)
        self.assertEqual(buffer[-3], 5)
        with self.assertRaises(IndexError):
            buffer[10]
        with self.assertRaises(IndexError):
            buffer[-10]
            
    def test_pop_elements_buffer_not_empty(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.pop()
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 4)
        self.assertFalse(buffer.is_empty)
        self.assertFalse(buffer.is_full)
        self.assertEqual(buffer[0], 1)
        self.assertEqual(buffer[1], 2)
        self.assertEqual(buffer[2], 3)
        self.assertEqual(buffer[-1], 4)
        self.assertEqual(buffer[-2], 3)
        self.assertEqual(buffer[-3], 2)
        with self.assertRaises(IndexError):
            buffer[4]
        with self.assertRaises(IndexError):
            buffer[-5]
            
    def test_pop_elements_buffer_empty(self):
        buffer = CircularBuffer(capacity = 5)
        with self.assertRaises(IndexError):
            buffer.pop()
            
    def test_pop_elements_buffer_not_empty(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.pop()
        buffer.pop()
        buffer.pop()
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 2)
        self.assertFalse(buffer.is_empty)
        self.assertFalse(buffer.is_full)
        self.assertEqual(buffer[0], 4)
        self.assertEqual(buffer[1], 5)
        self.assertEqual(buffer[-1], 5)
        self.assertEqual(buffer[-2], 4)
        with self.assertRaises(IndexError):
            buffer[2]
        with self.assertRaises(IndexError):
            buffer[-3]
            
    def test_pop_elements_buffer_until_empty(self):
        buffer = CircularBuffer(capacity = 5)
        for value in range(1, 6):
            buffer.push(value)
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 5)
        self.assertFalse(buffer.is_empty)
        self.assertTrue(buffer.is_full)
        for _ in range(5):
            buffer.pop()
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 0)
        self.assertTrue(buffer.is_empty)
        self.assertFalse(buffer.is_full)
        with self.assertRaises(IndexError):
            buffer[0]
        with self.assertRaises(IndexError):
            buffer[1]
        with self.assertRaises(IndexError):
            buffer[-1]
        with self.assertRaises(IndexError):
            buffer[5]
        with self.assertRaises(IndexError):
            buffer[-5]
                
    def test_clear_buffer(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.clear()
        self.assertEqual(buffer.capacity, 5)
        self.assertEqual(buffer.size, 0)
        self.assertTrue(buffer.is_empty)
        self.assertFalse(buffer.is_full)
        with self.assertRaises(IndexError):
            buffer[0]
        with self.assertRaises(IndexError):
            buffer[1]
        with self.assertRaises(IndexError):
            buffer[-1]
        with self.assertRaises(IndexError):
            buffer[5]
        with self.assertRaises(IndexError):
            buffer[-5]
            
    def test_iterate_buffer(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        values = [value for value in buffer]
        self.assertEqual(values, [1, 2, 3, 4, 5])
        
    def test_iterate_buffer_over_capacity(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.push(6)
        buffer.push(7)
        values = [value for value in buffer]
        self.assertEqual(values, [3, 4, 5, 6, 7])
    
    def test_iterate_empty_buffer(self):
        buffer = CircularBuffer(capacity = 5)
        values = [value for value in buffer]
        self.assertEqual(values, [])
        
    def test_classic_use_case(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        buffer.push(4)
        buffer.push(5)
        buffer.pop()
        buffer.pop()
        values = [value for value in buffer]
        self.assertEqual(values, [3, 4, 5])
        buffer.push(6)
        buffer.push(7)
        values = [value for value in buffer]
        self.assertEqual(values, [3, 4, 5, 6, 7])
        self.assertEqual(sum(buffer), 25)
        
    def test_str_buffer(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(11)
        buffer.push(21)
        buffer.push(31)
        buffer.push(41)
        buffer.push(51)
        buffer.push(61)
        buffer.push(71)
        self.assertEqual(str(buffer), '<31, 41, 51, ...>')
        self.assertRegex(repr(buffer), r'CircularBuffer\(capacity = 5\) at 0x[0-9a-fA-F]+') # regex for hex id generatlization
        self.assertEqual(f'{buffer}', '<31, 41, 51, ...>')
        self.assertEqual(f'{buffer:size}', '5')
        self.assertEqual(f'{buffer:capacity}', '5')
        self.assertEqual(f'{buffer:load}', '5 / 5 (100.0 %)')
        self.assertEqual(f'{buffer:full}', '<31, 41, 51, 61, 71>')
        self.assertEqual(f'{buffer:raw}', '[61, 71, 31, 41, 51]')
        self.assertEqual(buffer[0], 31)
        self.assertEqual(buffer[1], 41)
        self.assertEqual(buffer[2], 51)
        self.assertEqual(buffer[3], 61)
        self.assertEqual(buffer[4], 71)
        self.assertEqual([value for value in buffer], [31, 41, 51, 61, 71])
        
    def test_len_buffer(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        self.assertEqual(len(buffer), 3)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        self.assertEqual(len(buffer), 5)
        buffer.pop()
        self.assertEqual(len(buffer), 4)
        buffer.pop()
        buffer.pop()
        buffer.pop()
        self.assertEqual(len(buffer), 1)
        buffer.clear()
        self.assertEqual(len(buffer), 0)
        
    def test_contain_buffer(self):
        buffer = CircularBuffer(capacity = 5)
        buffer.push(1)
        buffer.push(2)
        buffer.push(3)
        self.assertTrue(1 in buffer)
        self.assertTrue(2 in buffer)
        self.assertTrue(3 in buffer)
        self.assertFalse(4 in buffer)
        self.assertFalse(5 in buffer)
        buffer.push(4)
        buffer.push(5)
        self.assertTrue(4 in buffer)
        self.assertTrue(5 in buffer)
        self.assertFalse(6 in buffer)
        self.assertFalse(7 in buffer)
        buffer.pop()
        buffer.pop()
        buffer.pop()
        self.assertFalse(1 in buffer)
        self.assertFalse(2 in buffer)
        self.assertFalse(3 in buffer)
        self.assertTrue(4 in buffer)
        self.assertTrue(5 in buffer)
        buffer.clear()
        self.assertFalse(1 in buffer)
        self.assertFalse(2 in buffer)
        self.assertFalse(3 in buffer)
        self.assertFalse(4 in buffer)
        self.assertFalse(5 in buffer)
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()        