
# Function 1: Count words in a sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)


# Function 2: Find the longest word
def longest_word(sentence):
    words = sentence.split()

    if not words:
        return "No words found"

    return max(words, key=len)


# Function 3: Reverse the sentence
def reverse_sentence(sentence):
    return sentence[::-1]


# Function 4: Check whether a number is prime
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Main Program
sentence = input("Enter a sentence: ")
number = int(input("Enter a number: "))

print("\n----- Sentence Analysis -----")
print("Word Count:", count_words(sentence))
print("Longest Word:", longest_word(sentence))
print("Reversed Sentence:", reverse_sentence(sentence))

print("\n----- Prime Number Check -----")

if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is Not a Prime Number")
