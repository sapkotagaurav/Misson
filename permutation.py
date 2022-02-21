'''A program to compute permutation of a word'''
import time

time_init =time.time()
def get_word():  # get word from user and return lower form of it
    word = input("Enter any word")
    return word.lower()


def factorial(n: int):  # calculates factorial of an integer O(n)
    prod = 1
    for a in range(1, n+1):
        prod *= a
    return prod


def permutation(word: str):
    divide_by = 1
    dividend = factorial(len(word)) #O(n)
    for index in range(0, len(word)):
        letter = word[index]
        repeat_count = 0
        temp = 1
        if letter == "_": #if letter is _ skip it
            continue
        for i in range(index, len(word)):
            if letter == word[i]:
                repeat_count += 1 #if letters repeat, count the times of repeatition 
        word = word.replace(letter, "_")#replace the letter with _ so processed and repeated letters become _
        temp = factorial(repeat_count)
        divide_by *= temp
    return int(dividend/divide_by)


def main():
    word = get_word()
    print("The times word",word,"can be arranged is ",permutation(word))
    print(time.time()-time_init)


main()
