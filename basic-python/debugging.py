import pdb

letters = ['a', 'b', 'c', 'd']

for i in letters:
    pdb.set_trace()  # This line is now outside the loop
    print(i)
