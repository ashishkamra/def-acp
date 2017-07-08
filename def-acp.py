#!/usr/bin/python2.7 -tt
# Copyright 2017 Ashish Kamra
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys

def heapsort(iterable):
  h = []
  for value in iterable:
    heapq.heappush(h, value)
  return [heapq.heappop(h) for i in range(len(h))]

def main():
  heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
  sys.exit(0)


if __name__ == '__main__':
  main()

