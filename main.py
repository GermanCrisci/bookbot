from stats import *
import sys

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
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    
    filepath = sys.argv[1]
    
    try:
        book_text = get_book_text(filepath)
    except:
        print("Error: Couldn't get book contents, did you send a valid file path?")
        exit()
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    sorted_char_list = sort_character_dictionary(get_number_characters(book_text))
    for elem in sorted_char_list:
        print(f"{elem['char']}: {elem['num']}")

if __name__ == "__main__":
    main()