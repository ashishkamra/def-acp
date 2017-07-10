#!/usr/local/bin/python3 -tt
# Copyright 2017 Ashish Kamra
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import heapq

# file names
Set_A_fname="Set_A"
Set_B_fname="Set_B"
A_choice_fname="A_choice"
B_choice_fname="B_choice"

# global data structures
Set_A = ()
Set_B = ()

def read_file(fname):
  with open(fname,'r') as f:
    line = f.read().lstrip().rstrip()
    tup = tuple(line.split(','))
    return tup

def main():

  ###############################################################################
  # read in the input data from the files and create the global data structures #
  ###############################################################################

  # create Set_A tuple
  Set_A = read_file(Set_A_fname)

  # create Set_B tuple
  Set_B = read_file(Set_B_fname)

  # test
  print(Set_A)
  print(Set_B)
 
  sys.exit(0) 

if __name__ == '__main__':
  main()

