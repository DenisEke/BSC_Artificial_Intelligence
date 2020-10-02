# Solution to assignment 5 task 5

# Introduce user to program and ask for his salary
print(
    "Hey, I would like to calculate your taxes. What is you gross salary in € ? (Enter it like that: 5000, 35435,34 ...): ")

# get input in type float because salary can contain cents
salary = float(input())

# basic taxrate
taxRate = 0;

# set taxrate based on salary
# Why doesn't python have a switch-case :'( ?!
if salary > 50000:
    taxRate = 0.50
elif salary > 25000:
    taxRate = 0.25
elif salary > 10000:
    taxRate = 0.10

# Print users gross salary, tax rate and net-income
print("You are earning", salary, "€ and you have to pay", taxRate * 100, "% taxes. So your net income is",
      (1 - taxRate) * salary, "€.")

# for the lolz
if salary > 50000:
    print("Consider moving to Marocco to save on taxes :P")
if salary < 50000:
    print("Consider getting a degree at the VU to earn more money :D")
