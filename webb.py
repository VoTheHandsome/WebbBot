import random
import pickle

with open("random_words_database.dat", "rb") as dat:
    random_words_database = pickle.load(dat) 

def generate_sentence(opener, length=random.randint(5,15)):
    "Generate a random sentence with a defined length and opener."
    opener_table = random_words_database[opener]
    sentence = [opener]
    sentence.append(random.choice(opener_table))

    for i in range(length - 2):

        if not sentence[-1] in random_words_database:
            skipper = random.choice(list(random_words_database.keys()))
        else:
            skipper = sentence[-1]

        table = random_words_database[skipper]
        if table == []:
            raise Exception("Empty table")

        sentence.append(random.choice(table))
    word = " ".join(sentence).split()

    for i in range(len(word)):
        if word[i].startswith("<@"):
            word[i] = ""
    word = " ".join(word).lower()

    return (word[0].upper() + word[1:]).replace("@", "!") 
