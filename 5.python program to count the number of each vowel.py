vowels = 'aeiou'
input_str = input("Enter a string: ")

# make it suitable for caseless comparisions
input_str = input_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# count the vowels
for char in input_str:
    if char in count:
        count[char] += 1

print(count)
