import random

def random_array():

  return [random.randint(0, 100) for _ in range(10)]

array = random_array(10)
print("Neuspořádané pole:", array)

def bubble_sort(array):

  n = len(array)
  for i in range(n):
    for j in range(0, n-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]


bubble_sort(array)
print("Bubble sort:", array)

import random

def is_sorted(array):


  Args:
    array: Seznam čísel.

  Returns:
    True, pokud je seznam seřazen, jinak False.

  for i in range(0, len(array) - 1):
    if array[i] > array[i+1]:
      return False
  return True

def bogo_sort(array):


  Args:
    array: Seznam čísel k setřídění.

  while not is_sorted(array):
    random.shuffle(array)

bogo_sort(array)
print("Bogo sort:", array)


def selection_sort(array):

  Args:
    array: Seznam čísel k setřídění.

  for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
      if array[min_idx] > array[j]:
        min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i] 1    

selection_sort(array)
print("Selection sort:", array)

def insertion_sort(array):


  Args:
    array: Seznam čísel k setřídění.

  for i in range(1, len(array)):
    key = array[i]
    j = i-1
    while j >= 0 and key < array[j]:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = key

insertion_sort(array)
print("Insertion sort:", array)
