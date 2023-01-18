import random, sys

def random_dictionary_words(word_count, dictionary_file):
  #open/read dictionary file 
  with open(dictionary_file) as f: 
    random_dict_words = f.read().splitlines()
    #select a random set of words from file and store in a data type
    #number of words requested in string
    user_input= random.choices(random_dict_words, k=int(word_count))
    output = " ".join(user_input)
    #print sentence
    return print(output)

if __name__ == "__main__":
  random_dictionary_words(int(sys.argv[1]), '/usr/share/dict/words')