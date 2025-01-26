# Scrivere il codice degli esercizi qui dentro
# PARTE PRIMA
def my_divmod():
    try:
        num1 = int(input("Inserisci un dividendo: "))
        num2 = int(input("Inserisci un divisore: "))
        result = ((num1 // num2), (num1 % num2))
        print(f"Il risultato intero e il resto della divisione tra {num1} e {num2} è rappresentato da: {result}")
    except ZeroDivisionError:
        print("Impossibile dividere per zero.")

my_divmod()

#PARTE SECONDA
def pow_list(li1):
    li2 = []
    for x in li1:
        li2.append(x ** 2)
    return li2



def count_words(word_to_count):
    words_list = word_to_count.split()
    sum_words = len(words_list)
    return sum_words


def reverse_string(word):
    reversed_result = word[::-1]
    return reversed_result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_palindrome(possible_palindrome):
    palindrome = possible_palindrome == possible_palindrome[::-1]
    return palindrome


def sum_even_numbers(listed):
    even_list = []
    for num in listed:
        if num % 2 == 0:
            even_list.append(num)
            total_even = sum(even_list)
    return total_even


def find_max(li_ex):
    num = max(li_ex)
    return num


def count_vowels(words):
    vow_list = []
    for x in words:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            vow_list.append(x)
    return len(vow_list)

# PARTE TERZA
# vedi file crash.py
