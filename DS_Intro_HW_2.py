#Gal Giller 209264555
#1
def reverse(sentence, reverse_word):
    if type(reverse_word) == str:
        if reverse_word in sentence:
                reverse_index = sentence.find(reverse_word) #the word we want to reverse- index
                word = reverse_word[::-1] #the word reversed
                prior = sentence[:reverse_index] #the sentence till the reverse_word
                post = sentence[(reverse_index+len(reverse_word)):] #the sentence after the reverse_word
                new_sentence = prior + word + post
                return new_sentence.lstrip()
        else:
            return "The word was not found"
    else:
        return "Invalid input"
