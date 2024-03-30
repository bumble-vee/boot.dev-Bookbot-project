

def main():
    book_path = "github.com/bumble-vee/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words=get_wordcounts(text)
    letter_frequency = count_letters(text)
    

    unsorted_list = convert_to_list(letter_frequency)
    
    sorted_list = sort_list(unsorted_list)
    
    print_analysis(sorted_list,num_words)

    #print(sorted_list)
    #print(f"{num_words} words founds in the document.")
    #print(f"Letter frequency is as follows:")
    #print(letter_frequency)
    #print(unsorted_list)

def get_wordcounts(text):  # accepts list, splits, returns word count as int
    words = text.split()
    return len(words)

def get_book_text(path): # accepts file path as string, returns contents of file as string
    with open(path) as f:
        return f.read()

def count_letters(text): # accepts string, returns dictionary of all unique characters as string
    letter_freq = {} 
    lowercased = text.lower()
    index_counter = 0

    for i in lowercased:
        letter = lowercased[index_counter]
        if lowercased[index_counter] not in letter_freq:
            letter_freq[lowercased[index_counter]] = 1
        else:
            letter_freq[lowercased[index_counter]] += 1
        index_counter += 1
    return letter_freq

def convert_to_list(dictionaries): # accepts dictionary, breaks dictionary into list of dictionaries, returns list of dictionaries containing 'char' and 'count' keys
    unsort_list = []
    for dict_key in dictionaries:
        unsort_list.append({"char": dict_key , "count": dictionaries[dict_key]})
        
    return unsort_list

def sort_list(unsorted): # accepts unsorted list of dictionaries; returns sorted list of dictionaries):
    unsorted.sort(key=sort_on, reverse=True)
    return unsorted

def sort_on(dict): # accepts dictionary, returns arbitrary key. For use in sort function
    return dict["count"]

def print_analysis(sort_dict,wordcount): # accepts a dictionary; prints an character count analysis to terminal
    print(f"Total character count: {wordcount}")
    out_num = 0
    index_counter = 0

    for key in sort_dict:
        out_num = sort_dict[index_counter] 
        if out_num['char'].isalpha():       #removes non alphabet characters
            print(f"The '{out_num['char']}' character appears {out_num['count']} times.")
        index_counter +=1 


main()