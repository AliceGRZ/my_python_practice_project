"""Create a function named medical_book_finder that receives title, author_last_name, and publication_year as its parameters.

As a medical student in the university library, you need to find the correct textbook for your study session. Your function should determine if a given book matches the specific criteria for your current study topic.

The function should return True if the book meets all the following criteria, and False otherwise:

The title contains either "Anatomy" or "Physiology" (case-insensitive).
The author's last name starts with a letter between 'A' and 'M' (inclusive, case-insensitive).
The publication year is 2010 or later.
To solve this challenge, you'll need to use string comparison methods (like lower() and startswith()), logical operators (and, or), and basic conditional statements.

Parameters:

title (str): The title of the book.
author_last_name (str): The last name of the book's author.
publication_year (int): The year the book was published.
The function returns a boolean value: True if the book meets all criteria, False otherwise."""

## Solution 1
def medical_book_finder(title, author_last_name, publication_year):
    if ("anatomy" in title.lower() or "physiology" in title.lower()) and \
        author_last_name[0].upper() in tuple("ABCDEFGHIJKLM") and \
        publication_year >= 2010:
            
            print(f"{True}: I found book titled {title} written by {author_last_name}, published in {publication_year}")
            return True  
    else:
        print("book not found")
        return False  
        

## Solution 2
def medical_book_finder2(title, author_last_name, publication_year):
    if ("anatomy" in title.lower() or "physiology" in title.lower()) and \
    'a' <= author_last_name[0].lower() <= 'm' and \
        publication_year >= 2010:
            print(f"{True}: I found book titled {title} written by {author_last_name}, published in {publication_year}")
            return True 
    else:
        print("book not found")
        return False  

  
## Solution 3 - given
def medical_book_finder3(title, author_last_name, publication_year):
    # Convert title and author_last_name to lowercase for case-insensitive comparison
    title_lower = title.lower()
    author_lower = author_last_name.lower()
    
    # Check if the title contains "anatomy" or "physiology"
    title_condition = "anatomy" in title_lower or "physiology" in title_lower
    
    # Check if the author's last name starts with a letter between 'A' and 'M'
    author_condition = 'a' <= author_lower[0] <= 'm'
    
    # Check if the publication year is 2010 or later
    year_condition = publication_year >= 2010
    
    # Return True if all conditions are met, False otherwise
    return title_condition and author_condition and year_condition


