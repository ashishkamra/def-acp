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
      choice_dict[member_0] = [h, member_n]
    else:
      choice_dict[member_0] = [h]

  f.close()

  return choice_dict

def main():

  A_match = {}
  B_match = defaultdict(list)

  ###############################################################################
  # read in the input data from the files and create the global data structures #
  ###############################################################################

  # create Set_A tuple
  Set_A = create_sets_AB(Set_A_fname)

  # create Set_B tuple
  Set_B = create_sets_AB(Set_B_fname)

  # create choice dictionaries
  # the key is a set_A member. The value is a list
  A_choice = create_choice_dicts(A_choice_fname)
  B_choice = create_choice_dicts(B_choice_fname)

  # The algo starts  
  any_offers_made = True

  # holds the offers made "to" each member of Set_A
  A_offers = defaultdict(list)
  
  # holds the offers made "by" each member of Set_B
  B_offers = defaultdict(list)

  # the iterations start
  while any_offers_made = True
    any_offers_made = False
    # every member in B_choice makes offers
    for B_key,B_value in B_choice.items():
      # populate the offer list for each candidate (number of candidates is specified at the end)
      # grab the number of Set_A members that a Set_B member wants to offer (B_value[0])
      Set_A_list = heapq.nsmallest(B_value[1], B_value[0])

      # if any Set_A member has been offered then the algo continues
      if Set_A_list is not None
        any_offers_made = True

      # create A_offers and B_offers dictionaries based on the Set_A_list
      for mem in Set_A_list: # mem format: (1,'A1')
        A_offers[mem[1]].append(B_key)
        B_offers[B_key].append(mem)
   
    # if no offers were, then we can break out of the algo and accept the matches  
    if any_offers_made = False
      break
    
    # Now comes the matching part
    # for each member in Set_A select its best choice as yet
    for mem in Set_A # mem format: 'A1'
      best_choice = heapq.heappop(A_choice[mem]) # best_choice format: (1,'B1')
      # if the best choice still exists 
      if best_choice is not None
        # if the best choice is in the current offer iterations
        if best_choice[1] is in A_offers[mem]
          # update A_match
          A_match[mem] = best_choice[1]
    
          # delete the Set_A member from B_offers
          B_offers[best_choice[1]].delete(mem)
    
          # update B_match
          B_match[best_choice[1]].append(mem)      
        else
          # push back the best_choice back on the A_choice dictionary
          heapq.heappush(A_choice[mem], best_choice)
    
    # put the remaining members from B_offers back in B_choice 
    for key, val_list in B_offers:
      for item in val_list
        heapq.heappush(B_choice[key][0], item)
      B_choice[key][1] = len(val_list)

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

  print("A_match")
  for keys, values in A_match.items():
    print(keys) 
    print(values)

  print("B_match")
  for keys, values in B_match.items():
    print(keys) 
    print(values)

  sys.exit(0) 

if __name__ == '__main__':
  main()

