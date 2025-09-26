# Zochord Internship Assignment - Task 3
# Author: Vicky Kumar

def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    try:
        age = int(age)
        print(f"Hello {name}, great to meet you! You are {age} years old and already exploring coding. Keep learning!")
    except ValueError:
        print("Invalid age. Please enter a number.")

if __name__ == "__main__":
    main()
