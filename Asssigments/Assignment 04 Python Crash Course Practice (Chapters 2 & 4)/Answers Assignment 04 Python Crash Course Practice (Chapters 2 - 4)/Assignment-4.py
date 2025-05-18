# Part 1: Variables & Input

# Q1. Movie Intro With name and movie name :

name = input("What is your name? ")                 
movie = input("What is your favorite movie? ")

print = (f"{name}'s favorite movie is {movie}.")


# Q2. Case Converter


word = input("Enter a word: ")

print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
print("Title Case:", word.title())

# Q3. Simple Math with Input


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)



# Part 2: Lists & Indexing



# Q4. My Friends List

friends = ["Ali", "Sara", "John", "Ayesha"]
for friend in friends:
    print(friend)

# Q5. Update Your List

fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Mango"
print("After replacing second fruit:", fruits)
fruits.append("Pineapple")
print("After appending a fruit:", fruits)
fruits.insert(0, "Orange")
print("After inserting at beginning:", fruits)

# Q6. List Length Reporter

animals = []
for i in range(5):
    animal = input("Enter a favorite animal: ")
    animals.append(animal)
print("Total number of animals:", len(animals))
print("First animal:", animals[0])
print("Last animal:", animals[-1])

# Part 3: For Loops & Ranges

# Q7. Print Numbers

for i in range(1, 11):
    print(i)
for i in range(2, 21, 2):
    print(i)
for i in range(5, 51, 5):
    print(i)

# Q8. Squares Table

for i in range(1, 11):
    print(f"{i} squared is {i**2}")

# Part 4: List Comprehension & Slicing

# Q9. Make a List of Cubes

cubes = [x**3 for x in range(1, 6)]
print(cubes)

# Q10. Top 3 Movies

movies = []
for i in range(5):
    movie = input("Enter a movie name: ")
    movies.append(movie)
print("First 3 movies:", movies[:3])
print("Last 2 movies:", movies[-2:])

# Q11. Top Students

students = []
for i in range(5):
    name = input("Enter student name: ")
    students.append(name)
for student in students:
    print(f"Hello, {student}!")
print("Top 3 students:", students[:3])
copied_students = students[:]
copied_students.append("Zain")
copied_students.append("Fatima")
print("Original list:", students)
print("Copied list with new names:", copied_students)

# Q12. Travel Wishlist

places = ["Japan", "Canada", "Turkey", "Switzerland", "Italy"]
print("Original list:", places)
print("Temporarily sorted list:", sorted(places))
places.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places)
places.reverse()
print("List after first reverse:", places)
places.reverse()
print("List after reversing back:", places)

# Mini Challenge: Name Art Generator

name = input("Enter your name: ")
name_chars = list(name)
for char in name_chars:
    print(char)
print("First 3 letters:", name_chars[:3])
print("Last 2 letters:", name_chars[-2:])
print("Total letters:", len(name_chars))
print("")


# what is python