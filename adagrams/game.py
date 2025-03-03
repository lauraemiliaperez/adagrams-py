import random
LETTER_HAND = 10
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
SCORE_VALUES = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

# wave 1:

def check_for_values(dict,list, letter):
    count_letter = list.count(letter)
    print(f"count letter: {count_letter}, letter {letter}")
    print(dict[letter])
    if dict[letter] >= count_letter:
        return True
    else:
        return False

def draw_letters():
    
    hand_list = []
    while len(hand_list) < LETTER_HAND:
        a_letter = random.choice(list(LETTER_POOL.keys()))
        hand_list.append(a_letter)
        value_enough_times = check_for_values(LETTER_POOL, hand_list, a_letter)
        if value_enough_times is True:
            continue
        else:
            hand_list.pop()
            
    return hand_list


# Wave 2:
def uses_available_letters(word, letter_bank):

    upper_word = word.upper()
    for letter in upper_word:
        if letter not in letter_bank:
            return False
        elif upper_word.count(letter) > letter_bank.count(letter):
            return False
        else:
            continue
    return True

    

def score_word(word):
    
    word_upper = word.upper()
    lenght_of_word = len(word)
    total_score = 0
    for letter in word_upper:
        if letter in SCORE_VALUES:
            total_score += SCORE_VALUES[letter]
    if lenght_of_word > 6:
        total_score += 8
    
    return total_score


    
# Wave 4:
def higher_than(tuple1, tuple2):
    '''returns True if word1 ranks higher than word2'''
    score_word1 = tuple1[1]
    score_word2 = tuple2[1]
    if score_word1 == score_word2:
        lenght_word1 = len(tuple1[0])
        lenght_word2 = len(tuple2[0])
        if lenght_word1 == 10 and lenght_word2 != 10:
            return True
        if lenght_word2 == 10 and lenght_word1 != 10:
            return False
        return lenght_word1 < lenght_word2
    return score_word1 > score_word2


def get_highest_word_score(word_list):
    best_tuple = None
    for word in word_list:
        current_tuple = word, score_word(word)
        if best_tuple is None or higher_than(current_tuple,best_tuple):
            best_tuple = current_tuple
    return best_tuple
    



