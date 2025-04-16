#!/usr/bin/env python3
import sys
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    if len(sys.argv) != 3:
        print("Usage: python hello_world.py <name> <birthday (YYYY-MM-DD)>")
        sys.exit(1)
    
    name = sys.argv[1]
    try:
        birthday = datetime.strptime(sys.argv[2], "%Y-%m-%d")
    except ValueError:
        print("Error: Birthday must be in YYYY-MM-DD format")
        sys.exit(1)
    
    current_age = calculate_age(birthday)
    future_age = current_age + 3
    
    print(f"Hello, {name}!")
    print(f"In three years, you will be {future_age} years old!")

if __name__ == "__main__":
    main()

    #comments go here

    
