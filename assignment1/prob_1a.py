#

def print_list(reverse_list):
  '''
   Define each list item as a str, then print the list length
   followed by list items, comma-delimited
  '''
  rlist = [str(n) for n in reverse_list]
  print "{0}: {1}".format(len(reverse_list), ', '.join(rlist))


def reverse_list(input_list):
  '''
  Accept a list of any length, and use the negative indices
   to write a new list 'reverse_list' withe each item.
  '''
  reverse_list = []
  for num in range(1,len(input_list)+1):
    reverse_list.append(input_list[-num])
  return reverse_list

def main():
  L1 = [1, 10, 11, 13, 2, 17, 25]
  L2 = ['a', 'A', 'b', 'B', 'c', 'C', 'd']

  print_list(reverse_list(L1))
  print_list(reverse_list(L2))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()