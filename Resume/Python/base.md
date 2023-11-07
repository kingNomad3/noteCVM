age = 20
print(age)
price = 19.95
# multiple words better to use _
first_name = "Mosh"
# case sensitive language
is_online = True

# receiving inputs
# we need the space after the ?
name  = input("what is your name? ")
print("Hello "+ name )

# type convesion
birth_year = input("Enter your birth year")
#
# age = 2023 - int(birth_year)
# # float() pour les nombre a virgule
# bool()
# str()
print(age)
print("votre age est " + str(age))

# uppercase

course = "python is cool"
print(course)
print(course.upper())
print(course.lower())
print(course.find("y"))
print(course.find("is"))
print(course.replace("y", "i"))
# check if we have python in course
print("python" in course)

# operator
# == to compare

# logical operator

price 25

print(price > 10 and price < 30)
print(price > 10 or price < 30)
print( not price > 10 or price < 30)

# condition
temperature = 35

# l'espace est important
if temperature > 30:
    print("its a hot day")
    print("drink water")
elif temperature > 20:
    print("its a a nice day")
else:
    print("its cold")
# will print no matter what cuz no space
print("done")


# while loops

i = 1
while i <= 5:
    print(i)
    i+=1

# list
names = ["john","bob","jack","yurk",]
print(names)
print(names[0])
print(names[-2])
# will give the first 3 names
print(names[0:3])

# list methodes
numbers = [1,2,3,4,5]
# at the end
numbers.append(6)
print(numbers)
# ou on veut
numbers.insert(0,-1)
# va remove le numero 3 pas celui a la troisiem position
numbers.remove(3)
# remove all the items
numbers.clear()
# exist?
print(1 in numbers)
# number of elements in the list
print(len(numbers))

# for loops
numbers2 = [1,2,3,4,5]

# will print the item in a new line
for item in numbers2:
    print(item)

i = 0
while i <len(numbers2):
    print(numbers2[i])
    i+=1

# range of fonction
# on va avoir les numero 0 to 5 exluding 5
numers3 = range(5)
print(numers3)
# result: range(0,5)
#on doit alors utilise un for loop
for numer in numers3:
    print(numer)

# we want to jump 2 number at the time
# va imprimer de 5 a 9 et va faire des bon de deux
numers4 = range(5,10,2)
for numer in numers4:
    print(numer)

# tuples kind of list but cannot be change once its created
number1 = (1,2,3,4,5)
number1[0] = 1
# result: error message