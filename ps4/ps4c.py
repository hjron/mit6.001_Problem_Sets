# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    max_words = 0
    max_pad = []
    # print('ciphertext:', ciphertext)
    em = ps4b.EncryptedMessage(ciphertext)
    dmsg = ''
    
    # get a list of valid words
    valid_words = load_words('words.txt')

    # for each pad in pads
    for pad in pads:
        # decrypt the ciphertext
        msg = em.decrypt_message(pad).get_text()
        # split the decrypted string
        tmp = msg.split()
        # count the number of valid words using is_word()
        count = 0
        for w in tmp:
            if is_word(valid_words, w):
                count += 1
        if count >= max_words:
            max_words = count
            max_pad = pad
            dmsg = msg

    # print('dmsg:', dmsg, 'max_pad:', max_pad)
    dm = ps4b.PlaintextMessage(dmsg)
    dm.change_pad(max_pad)

    # return the pad and string used by the last pad with the most valid words
    return dm


def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    encrypted_text = get_story_string()
    epads = get_story_pads()
    decrypted_story = decrypt_message_try_pads(encrypted_text, epads)
    return decrypted_story.get_text()

if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    pass
