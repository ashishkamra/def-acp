#!/usr/local/bin/python3 -tt
# Copyright 2017 Ashish Kamra
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import heapq
from collections import defaultdict

# file names
Set_A_fname="Set_A"
Set_B_fname="Set_B"
A_choice_fname="A_choice"
B_choice_fname="B_choice"

# global data structures
Set_A = ()
Set_B = ()
A_choice = {}
B_choice = {}

# create the Set_A and Set_B tuples from the input files
def create_sets_AB(fname):
  with open(fname,'r') as f:
    line = f.read().lstrip().rstrip()
    tup = tuple(line.split(','))
    return tup

# create the A_choice and B_choice dictionaries from the input files
# the choices for every member are stored in a heap
def create_choice_dicts(fname):

  choice_dict = {}
  member_0 = None

  f = open(fname, 'r')
  
  for line in f:
    member_choices = line.split(',')
    i = 0
    member_n = None
    h = []
    for item in member_choices:
      item = item.lstrip().rstrip()
      if i == 0:
        member_0 = item
      else:
        if i == len(member_choices)-1 and item.isnumeric():
          member_n = int(item)
        else:
          member_i = (i, item)
          heapq.heappush(h, member_i)

      i += 1

    if member_n is not None: 
      choice_dict[member_0] = (h, member_n)
    else:
      choice_dict[member_0] = (h)

  f.close()

  return choice_dict

def main():

  ###############################################################################
  # read in the input data from the files and create the global data structures #
  ###############################################################################

  # create Set_A tuple
  Set_A = create_sets_AB(Set_A_fname)

  # create Set_B tuple
  Set_B = create_sets_AB(Set_B_fname)

  # create choice dictionaries
  A_choice = create_choice_dicts(A_choice_fname)
  B_choice = create_choice_dicts(B_choice_fname)

  
  A_offers = defaultdict(list)
  # for every member in B_choice, make 
  for B_key,B_value in B_choice.items():
    # populate the offer list for each candidate (number of candidates is specified at the end)
    Set_A_list = heapq.nsmallest(B_value[1], B_value[0])
    for mem in Set_A_list:
      A_offers[mem[1]].append(B_key)

  # test
  print("Set A") 
  print(Set_A)
  print("Set B") 
  print(Set_B)

  print("A_choice")
  for keys, values in A_choice.items():
    print(keys) 
    print(values)

  print("B_choice")
  for keys, values in B_choice.items():
    print(keys) 
    print(values)

  print("A offer list")
  for keys, values in A_offers.items():
    print(keys) 
    print(values)

  sys.exit(0) 

if __name__ == '__main__':
  main()

