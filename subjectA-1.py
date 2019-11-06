'''

subject A

'''

# A-1
users = ["Bob", "Tom", "Ken"]
print(users)

# A-2
int_numbers = [1, 2, 3, 4, 5, ]
print(int_numbers)

# A-3
kazuma_info = ['kazuma', 'takashi', 35]
print(kazuma_info)

# A-4 範囲指定はコロン
members = ["Kazuma", "Makoto", "Ohira"]
print(members[0:2])

# A-5
kazuma_info = ["Kazuma", "Takahashi", 35]
print('Name: ' + kazuma_info[1] + kazuma_info[0] + f'Age: {kazuma_info[2]}')

# A-6
odd_numbers = [1, 3, 5, 7, 9]
for odd_number in odd_numbers:
    print(odd_number)

# A-7
even_numbers = [2, 4, 6, 8]
for even_number in even_numbers:
    print(even_number * 2)

# A-8
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

print('name: ' + users_info[0][0] + f', Age: {users_info[0][1]}')
print('name: ' + users_info[1][0] + f', Age: {users_info[1][1]}')
print('name: ' + users_info[2][0] + f', Age: {users_info[2][1]}')

# A-9
kazuma_info = {'first_name': 'Kazuma', 'family_name': 'Takahashi', 'age': 35}

print(kazuma_info["first_name"])
print(kazuma_info["family_name"])
print(kazuma_info["age"])
