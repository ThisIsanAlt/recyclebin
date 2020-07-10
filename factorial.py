def factorial(n : int):
  if n == 1: return n
  else: return n*factorial(n-1)

while True:
  print(factorial(int(input('What number would you like to factorialize?'))))