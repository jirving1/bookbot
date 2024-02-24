def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    letter_count = get_letter_count(text)
    char_sorted_list = sort_letter_count_list(letter_count)
   
    print(f"--- Report for {book_path} ---")
    print(f"A total of {num_words} were found in the document")
    
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the character {item['char']} was found {item['num']} times in the document." )


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    text = text.lower()
    words = text.split()
    letter_count = {}
    letters = []
    

    for w in words: 
        letters = list(w)
        for i in letters:
            if i.isalpha():
                letter_count[i] = letter_count.get(i, 0) + 1 
                
    return letter_count

def sort_letter_count_list(letter_count):
    sorted_list = []
    for ch in letter_count:
        sorted_list.append({"char": ch, "num": letter_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

main()
