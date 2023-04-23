import random
import tkinter as tk

# Ana pencereyi oluşturma
root = tk.Tk()
root.title("Şifre Oluşturucu")
root.geometry("500x500")

# Pencereyi ekranın tam ortasına yerleştirme
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))

# Frame'i oluşturma
frame = tk.Frame(root)
frame.pack(pady=50)

# Şifre oluşturma fonksiyonu
def generate_password(length, use_letters, use_numbers, use_symbols):
    # Olası karakterler
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!@#$%^&*()_+"
    # Şifre oluşturma
    password = ""
    characters = ""
    if use_letters:
        characters += letters
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols
    if not characters:
        return "Lütfen en az bir karakter türü seçin."
    for i in range(length):
        password += random.choice(characters)
    return password

# Şifre oluşturma işlevini tetikleyen fonksiyon
def generate():
    # Kullanıcı tarafından belirlenen uzunluk
    length = length_entry.get()
    if length.isdigit():
        length = int(length)
        # Karakter türleri seçimleri
        use_letters = use_letters_var.get()
        use_numbers = use_numbers_var.get()
        use_symbols = use_symbols_var.get()
        # Şifre oluşturma
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        # Şifre etiketine yazdırma
        password_label.config(text="Oluşturulan Şifre: " + password)
    else:
        # Uyarı mesajı verme
        password_label.config(text="Lütfen bir sayı girin.")

# Uzunluk etiketi ve giriş kutusu
length_label = tk.Label(frame, text="Şifre Uzunluğu:", fg="black", bg="white")
length_label.pack()
length_entry = tk.Entry(frame)
length_entry.pack()

# Checkboxlar
use_letters_var = tk.BooleanVar()
use_letters_var.set(True)
use_letters_checkbox = tk.Checkbutton(frame, text="Harfleri Kullan", variable=use_letters_var, bg="white")
use_letters_checkbox.pack()

use_numbers_var = tk.BooleanVar()
use_numbers_var.set(True)
use_numbers_checkbox = tk.Checkbutton(frame, text="Sayıları Kullan", variable=use_numbers_var, bg="white")
use_numbers_checkbox.pack()

use_symbols_var = tk.BooleanVar()
use_symbols_var.set(True)
use_symbols_checkbox = tk.Checkbutton(frame, text="Özel Karakterleri Kullan", variable=use_symbols_var, bg="white")
use_symbols_checkbox.pack()

# Şifre oluşturma düğ
generate_button = tk.Button(frame, text="Şifre Oluştur", command=generate, bg="white")
generate_button.pack(pady=10)

#Oluşturulan şifre etiketi
password_label = tk.Label(frame, text="", fg="black", bg="white")
password_label.pack(pady=10)

#Ana döngüyü başlatma
root.mainloop()
