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

def main():

  # parse options
  # inputs - 
  # 1.number of Set_A members 2.number of Set_B members (greater than or equal to Set_A members)

  parser = argparse.ArgumentParser(description='Generate synthetic data for the def-acp.py program.')
  parser.add_argument('Set_A_number', type=int, help="Number of Set_A members")
  parser.add_argument('Set_B_number', type=int, help="Number of Set_B members (>= Set_A_number)")
  args = parser.parse_args()

  if args.Set_B_number < args.Set_A_number:
    print("Error: Set_B_number must be >= Set_A_number\n")
    parser.print_help()
    sys.exit(-1)

if __name__ == main():
  main()

