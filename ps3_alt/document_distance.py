# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split()


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note:
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    # freak = {}
    # for e in input_iterable:
    #     # if e in freak:
    #     #     freak[e] += 1
    #     # else:
    #     #     freak[e] = 1
    #     # terse version of the above
    #     freak[e] = freak.get(e, 0) + 1

    # return freak
    return {s:input_iterable.count(s) for s in input_iterable}


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    # return get_frequencies(word)
    return {s:word.count(s)
            for s in string.ascii_lowercase if word.count(s) != 0}


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    # DIFF, ALL = 0, 0
    # for w in freq_dict1:
    #     if w in freq_dict2:
    #         DIFF += abs(freq_dict1[w] - freq_dict2[w])
    #         ALL += (freq_dict1[w] + freq_dict2[w])
    #     else:
    #         DIFF += freq_dict1[w]
    #         ALL += freq_dict1[w]

    # for w in freq_dict2:
    #     if w not in freq_dict1:
    #         DIFF += freq_dict2[w]
    #         ALL += freq_dict2[w]

    # return round(1 - (DIFF / ALL), 2)
    all = sum(freq_dict1.values()) + sum(freq_dict2.values())
    diff = sum(abs(freq_dict1[k] - freq_dict2[k])
               for k in freq_dict1 if k in freq_dict2)
    diff += sum(freq_dict1[k] for k in freq_dict1 if k not in freq_dict2)
    diff += sum(freq_dict2[k] for k in freq_dict2 if k not in freq_dict1)
    return round(1 - (diff / all), 2)

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    mfw = freq_dict1.copy()

    # for w in freq_dict2:
    #     if w in mfw:
    #         mfw[w] += freq_dict2[w]
    #     else:
    #         mfw[w] = freq_dict2[w]

    # max_freq = 0
    # retval = []
    # for w in sorted(mfw, key=mfw.get, reverse=True):
    #     if mfw[w] >= max_freq:
    #         max_freq = mfw[w]
    #         retval.append(w)
    for k, v in freq_dict2.items():
        if k in mfw:
            mfw[k] += v
        else:
            mfw[k] = freq_dict2[k]

    # return sorted(retval)
    return [k for k, v in mfw.items() if v == max(mfw.values())]

### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    # open and read a file into a string, convert to a list of words,
    # then convert the list to a dictionary of word frequencies
    # file_string = load_file(file_path)
    # word_list = text_to_list(file_string)
    # freaks = get_frequencies(word_list)
    frequencies = get_frequencies(text_to_list(load_file(file_path)))

    # # get the total number of words in the document
    # total_words = len(word_list)
    total = sum(frequencies.values())

    # tf = {}
    # for w in freaks:
    #     tf[w] = freaks[w] / total_words

    # return tf
    return {k:(v / total) for k, v in frequencies.items()}

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    # # open and read each file into a list of strings
    # strings = []
    # for f in file_paths:
    #     strings.append(load_file(f))

    # # convert each string into a list
    # words = []
    # for s in strings:
    #     words.append(s.split())

    # dedupe each list of words
    # uniq_words = []
    # for wl in words:
    #     uniq_words.append(list(dict.fromkeys(wl)))
    dedupe_list = []
    for f in file_paths:
        dedupe_list += get_frequencies(text_to_list(load_file(f)))

    # # count how many files have each word
    # doc_freak = {}
    # for l in uniq_words:
    #     for w in l:
    #         doc_freak[w] = doc_freak.get(w, 0) + 1

    # # calc idf for each word
    # idf = {}
    # doc_count = len(file_paths)
    # for el in doc_freak:
    #     idf[el] = math.log10(doc_count / doc_freak[el])

    # return idf
    return {k:(math.log10(len(file_paths) / v))
            for k, v in get_frequencies(dedupe_list).items()}

def get_tfidf(tf_file_path, idf_file_paths):
    """
    Args:
        tf_file_path: name of file in the form of a string (used to calculate TF)
        idf_file_paths: list of names of files, where each file name is a string
        (used to calculate IDF)
    Returns:
       a sorted list of tuples (in increasing TF-IDF score), where each tuple is
       of the form (word, TF-IDF). In case of words with the same TF-IDF, the
       words should be sorted in increasing alphabetical order.

    * TF-IDF(i) = TF(i) * IDF(i)
    """
    tfs = get_tf(tf_file_path)
    idfs = get_idf(idf_file_paths)

    # tfidf = {}
    # for k in tfs:
    #     if k in idfs:
    #         tfidf[k] = tfs[k] * idfs[k]
    tfidf = [(k, (v*idfs[k])) for k, v in tfs.items()]

    # return sorted(tfidf.items())
    return sorted(tfidf, key=lambda x:x[1])


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
