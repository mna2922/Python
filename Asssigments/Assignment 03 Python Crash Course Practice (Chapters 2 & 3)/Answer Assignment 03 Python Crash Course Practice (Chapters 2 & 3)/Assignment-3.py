
# Assignment 3 



                                # Chapter 2: Variables and Simple Data Types (10 Questions)



#  Q1 : Create a variable called greeting and store any message. Print it.

Greeting = "Hello World "
print(Greeting)


# Q2 : Change the value of greeting to a new message. Print the updated message.

Greeting = "Assalamo Alaikum who am i"
print(Greeting)

# Q3 : Create two variables first_name and last_name. Combine them into a full name using an f-string.

first_name = "My name is "
last_name = "Numan"

print( f"{first_name}{last_name}")

# Q4 : Print a quote along with the author's name using an f-string.

quote = "The only limit to our realization of tomorrow is our doubts of today."
author = "Franklin D. Roosevelt"

print(f'"{quote}", {author}')

# Q5 : Store a person's name with extra spaces. Strip the spaces before printing.

person = "      Awan       "

print(person.strip())

# Q6 : Take a number, add 5, multiply by 2, subtract 3, and print the final result.

number = 6

print( (number) +5 *2 -3)

# Q7 : Create two numbers a and b and print their sum, difference, product, and quotient.

a = 3 
b = 4

                                                                     # /// Sum ///

# sum of a and b value                       //////      Sum  = kisi number ko kissi dusry number m jama krna Sum kahlata hai //////

sum = a+b

print("Sum =", sum)

                                                                    # /// Difference ///


# difference of a and b value               //////         kisi number ko kissi dusry number m sy minus  krna Difference kahlata hai //////

difference= a-b

print("Difference =", difference)

                                                                    # /// Product ///

# product of a and b value                  //////         kisi number ko kissi dusry number sy zarab dena Product kahlata hai //////                              

product= a*b

print("Product =", product)

                                                                    # /// Quotient ///

# quotient of a and b value                 //////         kisi number ko kissi dusry number pr taqseem krna Product Quotient hai ////// 

quotient= a/b

print("Quotient =", quotient )


# Q8 : Find the square and cube of a number using the ** operator.

num1= 8
num2= 4

square = num1**2
cube = num2**3

print("Square of", num1, "is", square)
print("Cube of", num2, "is", cube)

# Q9 : Print the sum of three floating-point numbers.

flt_number1 = 2.3
flt_number2 = 5.6
flt_number3 = 3.4

All_flt_number = flt_number1 + flt_number2 + flt_number3

print("The Sum of all floating numbers", All_flt_number)

# Q10 : Assign three variables x, y, z in a single line and print them.

x,y,z= 5,10,15

print("x =",x ,"\n y =", y , "\n z =",z)







                                        
                                                        # Chapter 3: Introducing Lists (10 Questions)

# Q1 : Create a list of 5 favorite fruits and print each fruit separately.

Fruits = ["Apple","Banana","Mango","Orange","Grapes"]

print(Fruits[0])
print(Fruits[1])
print(Fruits[2])
print(Fruits[3])
print(Fruits[4])


# Q2 : Modify the second item in the list and print the updated list.

Fruits = ["Apple","Banana","Mango","Orange","Grapes"]

print(Fruits)

Fruits [1]= "Pear"

print(Fruits)

# Q3 : Append a new fruit and insert another at the beginning of the list.                  not solve 

Fruits = ["Apple","Banana","Mango","Orange","Grapes"]

Fruits.append ("Strawberry")                 #  append method use hota hai last m koi cheez add krny ky liye 

print(Fruits)
Fruits.insert (0,"Peach")                     # insert method use hota hai start m koi cheez add krny ky liye

print(Fruits)




# Q4 : Demonstrate deleting an item using del, pop(), and remove().



# The remove() method removes the specified item.

Fruits = ["Apple","Banana","Mango","Orange","Grapes"]

Fruits.remove("Mango")

print(Fruits)

#                   pop() method

# The pop() method removes the specified index.

Fruits = ["Apple","Banana","Mango","Orange","Grapes"]

Fruits.pop(0)

print(Fruits)


# The del() keyword also removes the specified index:

Fruits = ["Apple","Banana","Mango","Orange","Grapes"]

del Fruits[0]

print(Fruits)

            #    ///////   Note   ////////

 #  | Method     | Works By                   | Use When                          |
# | ---------- | -------------------------- | --------------------------------- |
# | `del`      | Index                      | You know the position of the item |
# | `pop()`    | Index (or last by default) | You want to use the deleted item  |
# | `remove()` | Value                      | You know the value, not the index |



# Q5 : Sort the list permanently with sort() and temporarily with sorted(). Print before and after each.








