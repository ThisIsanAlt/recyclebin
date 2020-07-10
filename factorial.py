def recursivefactorial(n : int):
  if n == 1: return n
  else: return n*recursivefactorial(n-1)

while True:
  print(recursivefactorial(int(input('What number would you like to factorialize?'))))