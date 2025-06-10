size = int(input("Enter list size: "))

str_list = []
for i in range(size):
    name = input("Enter a name: ")
    str_list.append((name))

filtered = list(filter(lambda name: name.startswith('A'), str_list))
print(len(filtered))