#!/usr/bin/env python

def int2bin(x):
  result = format(x, "04b")
  return result

print('NUM X    |   NUM Y  |   AND    |     OR    |   XOR')
print('-------------------------------------------------')

for x in range(9):
  for y in range(9):
    bitwise_and = x & y 
    bitwise_or = x | y 
    bitwise_xor = x ^ y 
    print(f'{int2bin(x)} ({x}) | {int2bin(y)} ({y}) | {int2bin(bitwise_and)} ({bitwise_and}) | {int2bin(bitwise_or)} ({bitwise_or})  | {int2bin(bitwise_xor)} ({bitwise_xor})') 
