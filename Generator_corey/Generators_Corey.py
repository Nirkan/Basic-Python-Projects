
'''
def square_numbers(nums):
	result = []
	for i in nums:		
		result.append(i*i)
	return result

my_nums = square_numbers([1,2,3,4,5])

print (my_nums)

'''


'''
def square_numbers(nums):
	for i in nums:
		yield(i*i)

my_nums = square_numbers([1,2,3,4,5])

#print(next(my_nums))

for num in my_nums:
	print (num)

'''


# my_nums = [x*x for x in [1,2,3,4,5])

'''
my_nums = (x*x for x in [1,2,3,4,5])     # generator with () instead of []

print(my_nums)

for num in my_nums:
	print (num)

'''

# Generator is better with performance because it is not holding values in memory.


#import mem_profile
import random
import time
import timeit
t1 = time.time()
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math','Engineering', 'CompSci', 'Arts', 'Business']

#print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource())


def people_list(num_people):
	result = []
	for i in range(num_people):
		person = {
				'id':i,
				'name': random.choice(names),
				'major': random.choice(majors)
			}
		result.append(person)
	return result


def people_generator(num_people):
	for i in range(num_people):
		person = {
				'id': i,
				'name': random.choice(names),
				'major': random.choice(majors)
			}
		yield person

'''
t1 = time.time()
people = people_list(1000000)
t2 = time.time()
'''

t1 = timeit.default_timer()
people = people_generator(1000000)
t2 = timeit.default_timer()


#print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_resource())
print('Took {} Seconds'.format(t2-t1))



