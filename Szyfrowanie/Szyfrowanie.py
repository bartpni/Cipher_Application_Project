import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new_alphabet = ['f', 'c', 'p', 'e', 'v', 'q', 'k', 'z', 'g', 'm', 't', 'r', 'a', 'y', 'o', 'n', 'u', 'j', 'd', 'l', 'w',
                'h', 'b', 'x', 's', 'i','f', 'c', 'p', 'e', 'v', 'q', 'k', 'z', 'g', 'm', 't', 'r', 'a', 'y', 'o', 'n',
                'u', 'j', 'd', 'l', 'w', 'h', 'b', 'x', 's', 'i']

vatsayana_alphabet = {'n' : 'o', 'p' : 'q', 'r': 's', 't' : 'u', 'v' : 'w', 'x' : 'y', 'z':
                      'a', 'b' : 'c', 'd' : 'e', 'f' : 'g', 'h' : 'i', 'j' : 'k', 'l' : 'm'}

file_cont = ""
save_cont = ""
window = tk.Tk()

mainframe = Frame(window)
window.title('Aplikacja szyfrujaca')

background1 = PhotoImage( file = 'Decryption.png')
label1 = Label( window, image = background1)
label1.place( x =-50, y = 30 )


m_font = ('times', 20,)

upload_f = tk.Label(window, text='Dodaj plik z informacją w formacie .txt', width=30, font=m_font)
upload_f.grid(row=1, column=1,sticky="nw")

b_upload = tk.Button(window, text='1.   Dodaj plik', width=20, command=lambda: upload_file())
b_upload.grid(row=2, column=1, pady = 10)

b_encode = tk.Button(window, text='3.   Zaszyfruj dane', width=20, command=lambda: encode())
b_encode.grid(row=5, column=1,sticky="n", pady= 10)


b_encode = tk.Button(window, text='4.   Odszyfruj dane', width=20, command=lambda: decode())
b_encode.grid(row=6, column=1,sticky="n")

b_encode = tk.Button(window, text='5.   Zapisz dane', width=20, command=lambda: save_file())
b_encode.grid(row=7, column=1,sticky="n",pady=10)

upload_l = tk.Label(window, text='autor aplikacji: Bartłomiej Pniowski',
                    width=50, font=m_font, pady=30)
upload_l.grid(row=15, column=1)



lista = StringVar()             #Lista z wyborem typu szyfrowania
choices = { 'Cypher','ROT 13','Arbitry','Vatsayarana'}
popupMenu = OptionMenu(window, lista,*choices)
Label(window, text="2. Wybierz szyfrowanie",width=20,font = ('times', 10),pady = 10).grid(row = 3, column = 1)
popupMenu.grid(row = 4, column = 1)
lista.set('Szyfrowanie')

def Update_vidget(var, index, mode):                # Funkcja przedstawiająca dodatkowy funkcjonał podczas wyboru szyfrowania Cypher
   print ("{}".format(lista.get()))
   if lista.get() == 'Cypher':
    global shift
    shift = Spinbox(window, from_=1, to=100,state='normal')
    shift.grid(row=9, column=1)
    upload_f = tk.Label(window, text='podaj liczbę przesunięcia', width=50, font=12)
    upload_f.grid(row=8, column=1)
    window.update()
   else:
    shift = Spinbox(window, from_=1, to=100,state='disable')
    upload_f = tk.Label(window, text='                                ', width=50, font=1)
    upload_f.grid(row=8, column=1)
    upload_f = tk.Label(window, text='                                 ', width=50, font=1,)
    upload_f.grid(row=9, column=1)
    window.update()


lista.trace_variable("w", Update_vidget)            #Śledzimy zmianę wyboru szyfrowania i odświeżamy okno


def upload_file():
    """Funckja otwiera okienko wyboru pliku o rozszerzeniu .txt z tekstem do kodowania/dekodowania
    następnie formatuje go i zapisuje do zmiennej globalnej file_cont"""
    file = filedialog.askopenfilename(filetypes=[("Plik tekstowy", '.txt')])
    fob = open(file, 'r')

    global file_cont
    file_cont = fob.read().lower()


def encode():
    """Funkcja pobiera informację o rodzaju wybranego szyfru i wywołująca odpowiednią funkcje kodującą"""
    global save_cont
    if lista.get() == "Cypher":
        number = int(shift.get())
        way = 0
        encode_text = cypher(way, number)
        save_cont = encode_text
        print(encode_text)
    elif lista.get() == "ROT 13":
        way = 0
        encode_text = ROT_13(way)
        save_cont = encode_text
        print(encode_text)
    elif lista.get() == "Arbitry":
        way = 0
        encode_text = Arbitry(way)
        save_cont = encode_text
        print(encode_text)
    elif lista.get() == "Vatsayarana":
        way = 0
        encode_text = Vatsayarana(way)
        save_cont = encode_text
        print(encode_text)


def decode():
    """Funkcja pobiera informację o rodzaju wybranego szyfru i wywołująca odpowiednią funkcje dekodującą"""
    global shift
    global save_cont
    if lista.get() == "Cypher":
        number = int(shift.get())
        way = 1
        decode_text = cypher(way, number)
        save_cont = decode_text
        print(decode_text)
    elif lista.get() == "ROT 13":
        way = 1
        encode_text = ROT_13(way)
        save_cont = encode_text
        print(encode_text)
    elif lista.get() == "Arbitry":
        way = 1
        encode_text = Arbitry(way)
        save_cont = encode_text
        print(encode_text)
    elif lista.get() == "Vatsayarana":
        way = 1
        encode_text = Vatsayarana(way)
        save_cont = encode_text
        print(encode_text)

def save_file():
    """Funkcja pobiera tekst ze zmiennej save_cont, w której zapisany jest tekst po wyborze szyfru
    i opcji kodowania/dekodowania i zapisuje ją jako wybrany plik w formacie .txt"""
    fob = filedialog.asksaveasfile(filetypes=[("Plik tekstowy", '*.txt')], defaultextension='.txt', mode='w')
    fob.write(str(save_cont))
    fob.close()


def cypher(way, shift):
    """Funkcja szyfru Cezara. Pobiera argumenty 'way'- kierunek przesuwania liter alfabetu,
    'shift'- liczba oznaczająca o ile przesuwana jest litera po alfabecie. Funkcja zwraca 'cipher_text' czyli zakodowany
    lub zdekodowany tekst"""
    global file_cont
    cipher_text = ""
    for letter in file_cont:
        if letter in alphabet:
            position = alphabet.index(letter)
            if way == 0:
                new_position = position + shift
            elif way == 1:
                new_position = position - shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text


def ROT_13(way):
    """Funkcja szyfru ROT13. Pobiera argumenty 'way'- kierunek przesuwania liter alfabetu.
    Funkcja zwraca 'cipher_text' czyli zakodowany lub zdekodowany tekst"""
    global file_cont
    cipher_text = ""
    for letter in file_cont:
        if letter in alphabet:
            position = alphabet.index(letter)
            if way == 0:
                new_position = position + 13
            elif way == 1:
                new_position = position - 13
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

def Arbitry(way):
    """Funkcja szyfru ROT13. Pobiera argumenty 'way'- kierunek przesuwania liter alfabetu.
    Funkcja zwraca 'cipher_text' czyli zakodowany lub zdekodowany zgodnie z przypisanym nowym porządkiem
    alfabetu tekst"""
    global file_cont
    cipher_text = ""
    for letter in file_cont:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_alphabet_position = new_alphabet.index(letter)
            if way == 0:
                new_position = position
                cipher_text += new_alphabet[new_position]
            elif way == 1:
                new_position = new_alphabet_position
                cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text



def getPosition(table, ch):
    row = -1
    if ch in table[0]:
        row = 0
    elif ch in table[1]:
        row = 1

    if row != -1:
        return (row, table[row].index(ch))
    else:
        return (None, None)


def getOpponent(table, ch):
    row, col = getPosition(table, ch)
    if row == 1:
        return table[0][col]
    elif row == 0:
        return table[1][col]


def Vatsayarana(way):
    """Funkcja szyfru Vatsayarana. Pobiera argumenty 'way'- kierunek przesuwania liter alfabetu.
    Funkcja zwraca 'cipher_text' czyli zakodowany lub zdekodowany zgodnie z przypisanym nowym porządkiem
    alfabetu tekst"""

    global file_cont
    cipher_text = ""
    for letter in file_cont:
        if way == 0:
            if letter in vatsayana_alphabet.keys():             #Przeszukujemy czy wartość jest w kluczach
                find_key = letter
                position = list(vatsayana_alphabet.keys()).index(find_key)                 #Wyznaczamy pozycje
                new_letter = list(vatsayana_alphabet.values())[position]                   #Zamieniamy wartość na literę
                cipher_text += new_letter

            elif letter in vatsayana_alphabet.values():         #Przeszukujemy czy wartość jest w wartościach słownika
                find_value = letter
                position = list(vatsayana_alphabet.values()).index(find_value)
                new_letter = list(vatsayana_alphabet.keys())[position]
                cipher_text += new_letter

            else:
                cipher_text += letter

        elif way == 1:
            if letter in vatsayana_alphabet.keys():
                find_key = letter
                position = list(vatsayana_alphabet.keys()).index(find_key)
                new_letter = list(vatsayana_alphabet.values())[position]                #podmieniamy wartość z powrotem z wartości na klucz
                cipher_text += new_letter

            elif letter in vatsayana_alphabet.values():
                find_value = letter
                position = list(vatsayana_alphabet.values()).index(find_value)
                new_letter = list(vatsayana_alphabet.keys())[position]
                cipher_text += new_letter

            else:
                cipher_text += letter

    return cipher_text

window.mainloop()      # Domknięcie pętli interfejsu graficznego

