# Esercizio 0. Scrivere un programma in Python che stampi a schermo il seguente:
print("VERSIONE 1")
print("ciao, mondo!") # la scritta "ciao, mondo!"
print(40+2) # il risultato della somma dei numeri 40 e 2
#print(40/0) # il risultato della divisione del numero 40 per 0 (commentato per non generare l'errore)
print("L'ultimo punto si trova commentato nel codice per evitare lo ZeroDivisionError")

print("VERSIONE 2")
frase_prova= "ciao, mondo!" # la scritta "ciao, mondo!"
print(frase_prova)

a = 40
b = 2
summarize = (a + b)
print(f"La somma di {a} + {b} è uguale a",summarize) # il risultato della somma dei numeri 40 e 2

c = 0
#divide = (a/c)
#print(f"Il quoziente di {a} diviso {b} è uguale a", divide) # il risultato della divisione del numero 40 per 0 (commentato per non generare l'errore)
print("L'ultimo punto si trova commentato nel codice per evitare lo ZeroDivisionError")

print("VERSIONE 3")
frase_prova = (input("Traduci in italiano la frase 'hello, world!': "))
frase_prova = frase_prova.lower()
print("La traduzione che hai dato è: ", frase_prova) # la scritta "ciao, mondo!" (invitando l'utente a inserirla)

num1 = int(input("Inserisci un numero: "))
num2 = int(input("Inserisci un altro numero: "))
choose_op = input("Inserisci l'operatore somma (+) o divisione (/): ")

try:
    if choose_op == "+":
        print(num1 + num2)
    else:
        print(num1/num2)
except ZeroDivisionError:
    print("Attenzione: divisione per zero, impossibile eseguirla.") #il risultato della somma di due numeri scelti dall'utente e/o della loro divisione, gestendo l'errore della divisione per zero

print("BONUS")
#(effettuato, però, avendo scaricato il file e non avendo effettuato il fork e push sulla repo)
print("Il contenuto del documento 'Readme' è il seguente: ")
file_toread = open('../../../../lez0/README.md')
var_toread = file_toread.read()
print(var_toread)
file_toread.close()