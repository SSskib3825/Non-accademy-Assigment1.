

# Data & Type
name = "Sakib"
age = 26
is_student = True


print("Name:", type(name))
print("Age:", type(age))
print("Is Student:", type(is_student))
print("\n")

# Arithmetic Operation

print("Age + 5 =", age + 5)
print("Age - 3 =", age - 3)
print("Age * 2 =", age * 2)
print("Age / 2 =", age / 2)
print("\n")

# Composition Operation

print("Is age > 18?", age > 18)
print("Is age == 26?", age == 26)
print("Is age != 30?", age != 30)
print("Is age < 18?", age < 18)
print("\n")

# Logical Opeartion

condition1 = age > 18
condition2 = is_student == True

print("condition1 and condition2:", condition1 and condition2)
print("condition1 or condition2:", condition1 or condition2)
print("not condition1:", not condition1)
print("\n")

# Assigment Operati0n

x = 10
print("Initial x:", x)

x += 5
print("After x += 5:", x)

x -= 3
print("After x -= 3:", x)

x *= 2
print("After x *= 2:", x)

x /= 4
print("After x /= 4:", x)
print("\n")

# Identity Operator

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not b:", a is not b)
print("\n")

# Memmbership Operator

print("7. Membership Operators:")
fruits = ["apple", "banana", "mango"]

print("'apple' in fruits:", "apple" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)
