#!/usr/bin/env python

def int2bin(x):
  result = format(x, "08b")
  return result

def int2hex(x):
  result = hex(x)
  return result

for num in range(1001):
  bin_val = int2bin(num) 
  hex_val = int2hex(num)
  print("{} {} {}".format(num, bin_val, hex_val))
