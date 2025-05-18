from stats import *

def get_book_text(filepath):
    """
    Reads a text file and returns its content as a string.
    
    Args:
        filepath (str): The path to the text file.
        
    Returns:
        str: The content of the text file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    """
    Main function to execute the script.
    """
    # Define the path to the text file
    filepath = 'books/frankenstein.txt'
    
    # Get the content of the book
    book_text = get_book_text(filepath)
    
    # Print the first 500 characters of the book
    # print(f"{get_num_words(book_text)} words found in the document.")
    
    # Print the first 500 characters of the book
    print(f"{get_number_characters(book_text)}.")

if __name__ == "__main__":
    main()