#!/usr/local/bin/python3 -tt
# Copyright 2017 Ashish Kamra
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import time
import heapq
from collections import defaultdict
import argparse

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
      choice_dict[member_0] = h

  f.close()

  return choice_dict

def main():

  A_match = {}
  B_match = defaultdict(list)

  ###############################################################################
  # read in the input data from the files and create the global data structures #
  ###############################################################################

  # parse options
  # option - location for input and output files
  parser = argparse.ArgumentParser()
  parser.parse_args()

  # create Set_A tuple
  Set_A = create_sets_AB(Set_A_fname)
  print("Set_A")
  print(Set_A)

  # create Set_B tuple
  Set_B = create_sets_AB(Set_B_fname)
  print("Set_B")
  print(Set_B)

  # create choice dictionaries
  # the key is a set_A member. The value is a list
  A_choice = create_choice_dicts(A_choice_fname)
  print("A_choice")
  print(A_choice)

  B_choice = create_choice_dicts(B_choice_fname)
  print("B_choice")
  print(B_choice)
  print("\n")

  # The algo starts  
  any_offers_made = True
  any_updates = True

  # holds the offers made "to" each member of Set_A
  A_offers = defaultdict(list)
  
  # holds the offers made "by" each member of Set_B
  B_offers = defaultdict(list)

  iter = 1
  # the iterations start
  while any_offers_made is True and any_updates is True:
    time.sleep(2)
    any_offers_made = False
    any_updates = False
    print('# Iteration # - ', iter)
    iter += 1
    # every member in B_choice makes offers till it has got all candidates that it wanted
    for B_key,B_value in B_choice.items():
      if B_value[1] != 0:
        Set_A_list = B_value[0]
        any_offers_made = True

      # create A_offers and B_offers dictionaries based on the Set_A_list
      for mem in Set_A_list: # mem format: (1,'A1')
        A_offers[mem[1]].append(B_key)
        B_offers[B_key].append(mem)
   
    # if no offers were, then we can break out of the iterations and accept the matches  
    if any_offers_made is False:
      break
   
    print("A_offers")
    pprint.pprint(A_offers)

    print("B_offers")
    pprint.pprint(B_offers)
 
    # Now comes the matching part
    for mem_A in Set_A: # mem_A format: 'A1'
     #print("A_offers:", A_offers[mem_A])
     #print("A_choice[mem_A]:", A_choice[mem_A])
     for choice_B in A_choice[mem_A]: # choice_B format: (1, 'B1')
       #print("choice_B:",choice_B)
       # if choice_B is in the offers
       if choice_B[1] in A_offers[mem_A]:
         # check the ranking of the choice against the current match, update match if current choice is better
         if (A_match.get(mem_A, None)) is None or (A_match.get(mem_A, None) is not None and A_match[mem_A][0] >  choice_B[0]):
           A_match[mem_A] = choice_B
           B_match[choice_B[1]].append(mem_A)
           any_updates = True

           # delete mem_A from B_choice for all Set_B members (not just the one who made the offer)
           # as mem has accepted the offer (tentatively)
           for mem_B in Set_B:
             choice_A = B_choice[mem_B][0]
             for item in choice_A:
               if mem_A == item[1]:
                 choice_A.remove(item)
                 
             if mem_B == choice_B[1]: # but reduce the count only for the Set_B member whose offer was accepted
               B_choice[mem_B][1] -= 1

         # we can break out of the loop here because the choice is the best choice (the way we iterate over A_choice[mem]
         # is in ascending order of choice ranking)
         break;
 
    print("Current A_match")
    print(A_match)
    
    print("Current B_match")
    print(B_match)

    print("Current B_choice")
    print(B_choice)
    print("\n")

  # when no more offers are made, the final state of A_match and B_match is the stable matching
 
  print("################# Final Matching ###################\n") 
  print("Final A_match")
  print(A_match)

  print("Final B_match")
  print(B_match)
  print("\n")

  sys.exit(0) 

if __name__ == '__main__':
  main()

