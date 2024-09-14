#List comprehension examples from the fifth lesson

#Example 1
name = 'Pasha'
n = [x for x in name]

print(n)


#Example 2
nums = [i for i in range(100)]

print(nums)


#Example 3
my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + "2" for i in my]

print(my2[1:3])


#Example 4
nums = [i for i in range(1,11)]
chotnie = [num for num in nums if num % 2 == 0]
nechotnie = [num for num in nums if num % 2 != 0]

print(chotnie, nechotnie)


#Example 5
names = ['Pavel', 'Jordan', 'Sasha']
names2 = [name for name in names if 'o' in name]

print(names2)


#Example 6
my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for i in my if 'a' in i]

print(my2)


#Example 7
my_list = [i for i in range(1, 11, 2)]

print(my_list)