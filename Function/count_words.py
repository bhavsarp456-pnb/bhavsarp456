def count_words(Sentence):
    words = Sentence.split()
    count_word = len(words)
    print(f"{count_word}")
count_words("Piyush is a good guy and hard working")