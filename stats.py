def get_num_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def get_number_characters(text):
    counters = {}
    for letter in text:
        letter = letter.lower()
        try:
            counters[letter] += 1
        except:
            counters[letter] = 1
    return counters

def sort_on(dict):
    return dict["num"]

def sort_character_dictionary(dict):
    char_list = []
    for elem in dict:
        if elem.isalpha():
            char_list.append({"char": elem, "num": dict[elem]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list