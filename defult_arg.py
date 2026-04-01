# default_args.py - Example 1

def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice")        # Uses default age = 18
greet("Bob", 25)      # Overrides default

# default_args.py - Example 2

def student(name, course="Python", duration="3 months"):
    print(f"{name} is learning {course} for {duration}.")

student("Rahul")  
student("Priya", "Java")  
student("Amit", "C++", "6 months")

# default_args.py - Example 3

def calculate_price(price, tax=5):
    total = price + (price * tax / 100)
    print(f"Total price: {total}")

calculate_price(100)      # Uses default tax = 5%
calculate_price(100, 18)  # Uses custom tax