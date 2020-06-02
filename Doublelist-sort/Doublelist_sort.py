
print('Enter characters for the list1 seperated by single space : ')

list1 = [num for num in input().split(' ')]


print('Enter numbers for the list2 seperated by single space : ')

list2 = [ int(num) for num in input().split(' ')]


# Function to sort list2 w.r.t. the values in list1

def sort_list(list1, list2):                 
	
	zipped_list = zip(list1, list2)

	sorted_pairs = sorted(zipped_list)

	z = zip(*sorted_pairs)                     # * is used to unpack the tuples 

	list1, list2 = [list(x) for x in z]        # The unpacked tuples, list1 ,list2

	return list1, list2


print(sort_list(list1, list2))

