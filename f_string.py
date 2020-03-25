
str = "python string"

print(str)

length_of_str = len(str)
print(length_of_str)

index_of_str = str[2]
print(index_of_str)
#index starts from 0 to len(str) - 1

last_character_str = str[-1]
print(last_character_str)

#String slicing
substring_str = str[0:3]
print(substring_str)

substring_str = str[3:-1]
print(substring_str)

substring_str = str[0:1000]
print(substring_str)

substring_str = str[0:len(str)]
print(substring_str)

#String slicing with steps

substring_str = str[1:6:2]
print(substring_str)


substring_str = str[6:1:2]
print(substring_str)

substring_str = str[:]
print(substring_str)

substring_str = str[:3]
print(substring_str)

substring_str = str[3:]
print(substring_str)

substring_str = str[::-1]
print(substring_str)






