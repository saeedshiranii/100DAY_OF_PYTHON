with open('file1.txt') as one:
    one = one.readlines()
    one_list = [line.strip() for line in one]
    print('one:    ', one_list)


with open('file2.txt') as twe:
    twe = twe.readlines()
    twe_list = [line.strip() for line in twe]
    print('twe:    ', twe_list)


same = [int(member) for member in one if member in twe]
print('same numbers are:    ', same)


