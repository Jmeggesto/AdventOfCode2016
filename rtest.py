import sys

def recursive_print(string):
  if not string:
    return
  print(string[0])
  recursive_print(string[1:])
  
recursive_print("".join(sys.stdin))