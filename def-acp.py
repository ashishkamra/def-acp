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
A_choice = []
B_choice = []

def create_sets_AB(fname):
  with open(fname,'r') as f:
    line = f.read().lstrip().rstrip()
    tup = tuple(line.split(','))
    return tup

def create_choice_lists(fname):

  h = []
  choice_list = []
  member_n = None

  with open(fname, 'r') as f:
    for line in f:
      member_choices = line.split(',')
      i = 0
      for item in member_choices:
        item = item.lstrip().rstrip()
        if i == 0:
          member_0 = item
          i += 1
        else:
          if i == len(member_choices)-1 and item.isnumeric():
            member_n = item
          else:
            member_i = (i, item)
            heapq.heappush(h, member_i)
            i += 1
      if member_n is not None: 
        choice_list.append([member_0, h, member_n])
      else:
        choice_list.append([member_0,h])

      return choice_list

def main():

  ###############################################################################
  # read in the input data from the files and create the global data structures #
  ###############################################################################

  # create Set_A tuple
  Set_A = create_sets_AB(Set_A_fname)

  # create Set_B tuple
  Set_B = create_sets_AB(Set_B_fname)

  # create choice lists
  A_choice = create_choice_lists(A_choice_fname)
  B_choice = create_choice_lists(B_choice_fname)

  # test
  print(Set_A)
  print(Set_B)
  print(A_choice)
  print(B_choice)
 
  sys.exit(0) 

if __name__ == '__main__':
  main()

