str1 = 'bmw'
str2 = 'BMW'

print("Is str1 == str2, I predict False")
print(str1 == str2)

print("Is str1.upper == str2, I predict True")
print(str1.upper() == str2)

print("Is str1 == str2.lower(), I predict True")
print(str1 == str2.lower())

age1 = 12 
age2 = 15

print("Is age 1 > age 2, I predict False")
print(age1 > age2)

print("Is age2 > age 1, I predict True")
print(age2 > age1)

print("Is the sum of age 2 and age 1 < 30, I predict True")
print(age1 + age2 < 30)

print("Is age1 or age2 < 14, I predict True")
print(age1 < 14 or age2 < 14)

print("Is age1 and age 2 > 13, I predict False")
print(age1 > 13 and age2 > 13)

nums = []
for i in range(1, 11):
    nums.append(i**4)

print('Is 7 a multiple of 4, I predict False')
print(4 in nums)

print('Is 16 a multiple of 4, I predict True')
print(16 in nums)
