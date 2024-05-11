'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"


def fix_text(mystr):
    #Write your alghoritm here.
    words = mystr.split() #split the string to words
    fixed_words = []
    for word in words:
        if word.startswith("(") and word.endswith(")"):
            #Remove parenthesis and keep the word as is
            fixed_words.append(word[1:-1]) #using "slicing syntax" to get the word inside parentheses (string without parentheses)
        else:
            #Reverse the word
            fixed_words.append(word[::-1])
    return ' '.join(fixed_words) #concatenates the words in the fixed_words list and makes it a string again
    #It already goes index by index and adds, so it is added sequentially.


if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
