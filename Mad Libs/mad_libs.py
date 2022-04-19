noun_list = ['magnet', 'cabin', 'pumpkin', 'kitten']
verb_list = ['defending', 'cleaning', 'giggling at', 'honoring']
adj_list = ['scenic', 'plastic', 'zigzag', 'rectangular']
adv_list = ['happily', 'carefully', 'frantically', 'quietly']

word_dict = {'nouns': noun_list, 'verbs': verb_list, 'adjectives': adj_list, 'adverbs': adv_list}

print(word_dict['nouns'])


def choose_noun():
    for idx, val in enumerate(word_dict['nouns']):
        print(idx + 1, val)
    user_noun = ''
    while user_noun not in noun_list:
        user_noun = input('Please select a noun: ')
    word_dict['nouns'].remove(user_noun)
    return user_noun


def choose_verb():
    for idx, val in enumerate(word_dict['verbs']):
        print(idx + 1, val)
    user_verb = ''
    while user_verb not in verb_list:
        user_verb = input('Please select a verb: ')
    word_dict['verbs'].remove(user_verb)
    return user_verb


def choose_adjective():
    for idx, val in enumerate(word_dict['adjectives']):
        print(idx + 1, val)
    user_adjective = ''
    while user_adjective not in adj_list:
        user_adjective = input('Please select an adjective: ')
    word_dict['adjectives'].remove(user_adjective)
    return user_adjective


def choose_adverb():
    for idx, val in enumerate(word_dict['adverbs']):
        print(idx + 1, val)
    user_adverb = ''
    while user_adverb not in adv_list:
        user_adverb = input('Please select an adverb: ')
    word_dict['adverbs'].remove(user_adverb)
    return user_adverb


def mad_lib():
    user_noun_list, user_verb_list, user_adj_list, user_adv_list = [], [], [], []
    for i in range(2):
        user_noun_list.append(choose_noun())
        user_verb_list.append(choose_verb())
        user_adj_list.append(choose_adjective())
        user_adv_list.append(choose_adverb())
    return user_noun_list, user_verb_list, user_adj_list, user_adv_list


if __name__ == '__main__':
    f = open('Lake_Patrol.txt', 'w')
    user_noun_list, user_verb_list, user_adj_list, user_adv_list = mad_lib()
    f.write(f"Ranger Robin's job is to patrol the state park. One morning Ranger Robin was {user_adv_list[0]} "
            f"checking the park's {user_adj_list[0]} lake.\nMany tourists liked to visit the {user_noun_list[0]} "
            f"there. Some came for the swimming. Some came for picnic.\nOthers came to {user_adv_list[1]} boat and "
            f"fish. The clean waters of the park were well known.\nThey were protected by the park rules and state "
            f"laws. It was her job to make sure people were {user_verb_list[0]}.\nThe park's {user_noun_list[1]} "
            f"was beautiful in the sunrise. The pink sunlight looked {user_adj_list[1]} as it softly colored the "
            f"lake water.\nRanger Robin felt content {user_verb_list[1]} this stunning resource")
    f.close()
    print(f.read())
