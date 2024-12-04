import random

def create_random_array(size):
  """Vytvoří pole s náhodnými čísly od 0 do 100.

  Args:
    size: Velikost pole.

  Returns:
    Seznam s náhodnými čísly.
  """

  return [random.randint(0, 100) for _ in range(size)]

# Vytvoření pole o velikosti 10
array = create_random_array(10)
print("Neuspořádané pole:", array)
