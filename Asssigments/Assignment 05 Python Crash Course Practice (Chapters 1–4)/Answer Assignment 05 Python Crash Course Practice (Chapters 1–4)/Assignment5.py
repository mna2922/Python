
# Question 01. Palindrome Check
# Write a program that takes a string input from the user and prints whether it is a palindrome (a string that reads the same forwards and backwards). Test the code with twi cases one where the input string is a palindrome and the other where it is not a palindrome.


input_str1 = "madam"  # First test string
input_str2 = "hello"  # Second test string

print("Original:", input_str1, "→ Palindrome:", input_str1 == input_str1[::-1])
print("Original:", input_str2, "→ Palindrome:", input_str2 == input_str2[::-1])

# Explanation:

# [::-1] reverses the string.

# We compare the original with the reversed version using ==.

# If equal, it's a palindrome.



# Question 02. Formatted Table
# Create a list of tuples where each tuple contains an item name (string) and its price (float).First print the list and then Use a for loop to print each item and its price along with serial nu
    
items = [("Apple", 0.99), ("Milk", 1.49), ("Bread", 2.50)]
print("S.No\tItem\tPrice")
for i in range(len(items)):
    print(str(i+1) + "\t" + items[i][0] + "\t" + str(items[i][1]))




# Explanation:

# A list of tuples holds item name and price.

# \t adds a tab space for formatting.

# Loop prints each item with a serial number.


# Question 03. Vowel Counter
# •	Given a string sentence, write a program that counts and print how many vowels it contains.
# o	print the original string
# o	print the count of vowels

sentence = "This is a sample sentence"
vowels = "aeiouAEIOU"
count = 0

for ch in sentence:
    if ch in vowels:
        count += 1

print("Original sentence:", sentence)
print("Vowel count:", count)



# Explanation:

# Loop through each character.

# If it's a vowel, increment the count.

# Print total vowels found.


# ________________________________________
# Question 04. Discount Calculator
# •	You have a list of product prices (floats), e.g. [19.99, 5.50, 100.0]. Apply a 15% discount to each price and store the new prices in a separate list. Then print original list, discounted list and each original and discounted price side by side.

prices = [19.99, 5.50, 100.0]
discounted = []

for price in prices:
    discounted.append(round(price * 0.85, 2))

print("Original prices:", prices)
print("Discounted prices:", discounted)

for i in range(len(prices)):
    print("Original:", prices[i], "→ Discounted:", discounted[i])




# Explanation:

# Multiply each price by 0.85 to apply a 15% discount.

# Use round(..., 2) to round to 2 decimal places.

# Show original and discounted prices side-by-side.



# ________________________________________
# Question 05. Phone Number Formatter
# •	You have a list of 11-digit strings like ["03123456789", "03001234567"]. Convert each into the format "+92-XXX-XXXXXXX" and print them. Print Original and Formatted number side by side.

numbers = ["03123456789", "03001234567"]

print("Original\tFormatted")
for num in numbers:
    formatted = "+92-" + num[1:4] + "-" + num[4:]
    print(num + "\t" + formatted)




# Explanation:

# Use string slicing to break the number.

# Replace the first 0 with +92.

# Format output neatly with tabs.



# ________________________________________
# Question 06. Score Statistics
# •	You have a tuple of exam scores, e.g. (72, 85, 91, 58, 76).
# o	print the provided tuple
# o	Convert it to a list and print it.
# o	Compute and print the minimum, maximum, and average score.

scores_tuple = (72, 85, 91, 58, 76)
scores_list = list(scores_tuple)

print("Original tuple:", scores_tuple)
print("Converted to list:", scores_list)
print("Minimum:", min(scores_list))
print("Maximum:", max(scores_list))
print("Average:", sum(scores_list)/len(scores_list))



# Explanation:

# Convert tuple to list using list().

# Use min(), max(), and sum()/len() to calculate stats.



# ________________________________________
# Question 07. Reverse Each Word in a Sentence
# •	Given a sentence string, reverse each word individually but keep the word order.
# o	print the original sentence
# o	print the formatted sentence

sentence = "Python is amazing"
words = sentence.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

new_sentence = " ".join(reversed_words)
print("Original sentence:", sentence)
print("Formatted sentence:", new_sentence)



# Explanation:

# Split sentence into words.

# Reverse each word with [::-1].

# Join them back into a sentence.



# ________________________________________
# Question 08. Running Sum List
# •	From a given list create a list where each element is the sum of all previous elements (inclusive). Print both the lists.

nums = [1, 2, 3, 4]
running_sum = []
total = 0

for num in nums:
    total += num
    running_sum.append(total)

print("Original list:", nums)
print("Running sum list:", running_sum)


# Explanation:

# Use a variable total to track cumulative sum.

# Append total to new list after each addition.


# ________________________________________
# Question 09. Interleave Two Lists
# •	Combine two equal-length lists into a single one by alternating elements.
# o	Input: [1, 2, 3] and ['a', 'b', 'c']
# o	Output: [1, 'a', 2, 'b', 3, 'c']
# •	Print all three lists.


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
interleaved = []

for i in range(len(list1)):
    interleaved.append(list1[i])
    interleaved.append(list2[i])

print("List 1:", list1)
print("List 2:", list2)
print("Interleaved list:", interleaved)


# Explanation:

# Add one element from each list alternately.

# Resulting list interleaves numbers and letters.

# ________________________________________
# Question 10. Repeat Letters
# •	Given a string, return a new string where each letter is repeated twice. Print both the strings


text = "Hello"
repeated = ""

for ch in text:
    repeated += ch * 2
print("Original:", text)
print("Repeated:", repeated)


# Explanation:

# Loop through characters.

# Double each character and build a new string.