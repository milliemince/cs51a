#millie mince and sam white 
#cs51a
#assignment 5
#10/4/19

# ----------------------------------------------------------
# Sentence Stats

def tokenize(string):
    """
    This function takes as input a string that represents a sentence. The
    function then splits the words into a new list that is returned, in which 
    all of the words are lowercased and all of the punctuation is removed.
    """
    lowercase_string = string.lower()
    split_string = lowercase_string.split()
    new_list = []
    for word in split_string:
        if word[-1] in [".", ",", ";", ":", "!", "?"]:
            word_without_punctuation = word[0:-1]
            new_list.append(word_without_punctuation)
        else:
            new_list.append(word)
    return new_list

def get_sentence_length(filename):
    """
    This function takes as input a filename as a string, tokenizes the 
    lines/sentences within the file, and then returns a list of the number of 
    words in each line/sentence.
    """
    my_file = open(filename, "r")
    new_list = []
    for line in my_file: 
        split_line = tokenize(line)
        words_in_line = len(split_line)
        new_list.append(words_in_line)
    my_file.close()
    return new_list

def print_sentence_stats(filename):
    """
    This function takes as input a filename as a string, and prints out four
    statistics about each sentence from the file: 1. the total number of
    sentences, 2. which sentence is the longest, 3. which sentence is the
    shortest, and 4. the average length of the sentences in the file. 
    The sentence lengths are compared to each other through the use of for loops
    and conditional statements, indicating which sentence is the longest and 
    the shortest, while the sum of the lengths of the sentences is continuously
    added to itself to find the average length of the sentences.
    """
    my_file = open(filename, "r")
    sentence_lengths = get_sentence_length(filename)
    total_sentences = len(sentence_lengths)
    longest_sentence = sentence_lengths[0]
    shortest_sentence = sentence_lengths[0]
    sum = 0
    for length in sentence_lengths:
        if length > longest_sentence:
            longest_sentence = length
        if length < shortest_sentence:
            shortest_sentence = length
        sum += length
    average_length = sum/(total_sentences)
    my_file.close()
    #add tab
    print("Total sentences: " + str(total_sentences))
    print("Longest sentence: " + str(longest_sentence))
    print("Shortest sentence: " + str(shortest_sentence))
    print("Average sentence length: " + str(average_length))

def add_words_to_dict(d, l_strings):
    """
    This function takes both a dictionary, in which the key is a string and its
    corresponding value is an integer that represents how often the word 
    appears in the dictionary as it is already, and a list of strings that 
    represents the words. The function analyzes each word that has not appeared 
    before by adding 1 to the count of the word in the dictionary, while words 
    that have appeared before are incremented by 1 in the dictionary. This 
    function mutates the dictionary and does not return a value.
    """
    for key in l_strings:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

def get_word_counts(filename):
    """
    This function takes as input a filename as a string, creating a dictionary
    of the words with their corresponding frequencies from the file. The
    tokenize function is used to split the lines up, extracting the words from
    the lines and adding them to the dictionary. The new dictionary
    is then returned. 
    """
    d = dict()
    my_file = open(filename, "r")
    for line in my_file:
        split_line = tokenize(line)
        add_words_to_dict(d, split_line)
    return d

def dict_count_max(d):
    """
    This function takes as input a dictionary of words and their frequencies,
    analyzes which words appear the most frequently within the dictionary by
    comparing each of the values (frequencies) to each other. The corresponding
    key, which represents the word, to the highest frequency is then returned.
    """
    most_frequent = 0
    for key in d:
        value = d[key]
        if value > most_frequent:
            most_frequent = value
            new_key = key
    return new_key

def print_top_ten(filename):
    """
    This function takes as input a filename as a string, analyzes how often
    each word appears within the file by utilizing a for loop and the function
    dict_count_max, and then uses the pop function to remove the key-value pair
    (the word and its frequency) from the list. The key-pairs are then arranged
    in order of the most frequent to the least frequent.
    """
    print("Top ten most frequent words")
    word_counts = get_word_counts(filename)
    count = 0
    for i in range(10):
        count += 1
        max_count = dict_count_max(word_counts)
        frequency = word_counts[max_count]
        print (str(count) + ": " + "\t" + str(max_count) + "\t" + str(frequency))
        word_counts.pop(max_count)

def print_all_stats(filename):
    """
    This function takes as input a filename as a string and uses the 
    print_sentence_stats function and the print_top_ten function to compile
    the information for each of the sentences in the file and the top ten
    frequencies of each word.
    """
    print ("---------------------------")
    print_sentence_stats(filename)
    print ("---------------------------")
    print_top_ten(filename)

# -----------------------------------------------------------------
# Analysis Section
        
# "normal.txt"
"""---------------------------
Total sentences: 99903
Longest sentence: 158
Shortest sentence: 1
Average sentence length: 23.068286237650522
---------------------------
1:the	168759
2:of	88769
3:and	69105
4:in	62498
5:to	50870
6:a	45793
7:is	24285
8:as	22400
9:was	21085
10:for	18114"""

# "simple.txt"
"""---------------------------
Total sentences: 99925
Longest sentence: 142
Shortest sentence: 1
Average sentence length: 15.491488616462346
---------------------------
1:the	108691
2:of	50242
3:and	40841
4:in	40083
5:a	35468
6:to	31615
7:is	29836
8:was	17399
9:it	14363
10:are	13385"""

"""The main differences between the two files is that the normal.txt file has
a much higher average sentence length than the simple.txt file (23 vs. 15.5),
and the longest sentence from the normal.txt file has 158 words, while the
longest sentence from the simple.txt file has a length of 142 words. However,
the simple.txt file has slightly more total sentences than the normal.txt file 
(99925 vs. 99903). Overall, every word in the normal.txt file has a higher
frequency than the words in the simple.txt file. The fact that the simple.txt
file has more total sentences does not coincide with the rest of the data, as
we would assume that the normal.txt file would have more total sentences
because the sentences in the file are longer on average."""

def unique_words(filename):
    """
    This function takes as input a filename as a string, creates a list
    of the words that are unique (i.e. only appear once) and uses a for loop
    to analyze each word on whether it has a frequency of one or not. If it does
    only appear once, the word (as a key) is added to the list of words that
    appear once. This list is then returned.
    """ 
    word_counts = get_word_counts(filename)
    words_that_appear_once = []
    for key in word_counts:
        value = word_counts[key]
        if value == 1:
            new_key = key
            words_that_appear_once.append(new_key)
    return len(words_that_appear_once) 

"""unique_words("normal.txt")
66091
unique_words("simple.txt")
40412"""

"""There are 66091 unique words (words that only appear once) in the normal
while there are only 40412 unique words in the simple text file. There are 
25679 more unique words in the normal text file than in the simple text file.
This implies that the simple text file (surprisingly!) is more simple
because it has less unique words."""
