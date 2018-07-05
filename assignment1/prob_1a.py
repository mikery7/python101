#define function
def print_list(reverse_list):
  '''
   print the input list
  '''
  print reverse_list
  #print "{0}: {1}".format(len(reverse_list), reverse_list)

def reverse_list(input_list):
  reverse_list = []
  for num in range(0,5):
    reverse_list.append(input_list[num])
  return reverse_list

L1 = [1, 10, 11, 13, 2, 17, 25]
L2 = ['a', 'A', 'b', 'B', 'c', 'C', 'd']

print_list(reverse_list(L1))
print_list(reverse_list(L2))
