import smtplib  # Для отправки email через SMTP
import ssl  # Для безопасного соединения
import imghdr  # Для определения формата изображения
from email.message import EmailMessage  # Для создания email-сообщения
import tkinter as tk  # Для графического интерфейса
from tkinter import Entry, Text, Button, Label, filedialog, messagebox  # Для элементов GUI

# Функция выбора файлов (изображений) для прикрепления

def vali_pilt():
    files = filedialog.askopenfilenames()  # Открывает диалоговое окно для выбора файлов
    attach_entry.delete(0, tk.END)  # Очищает поле ввода файлов
    attach_entry.insert(0, "; ".join(files))  # Вставляет выбранные файлы в поле ввода

# Функция отправки письма

def saada_kiri():
    kellele = email_entry.get().split(",")  # Получатели, разделенные запятыми
    teema = subject_entry.get()  # Тема письма
    kiri = message_text.get("1.0", tk.END).strip()  # Текст письма
    failitee = attach_entry.get().split("; ")  # Список прикрепленных файлов
    
    smtp_server = "smtp.gmail.com"  # SMTP сервер Gmail
    port = 587  # Порт для TLS соединения
    sender_email = "denielkruusman@gmail.com"  # Email отправителя
    password = "nafm ojez sqpx mgon"  # Пароль приложения Google

    # Проверка на заполненность полей email и сообщения
    if not kellele or not kiri:
        messagebox.showerror("Viga", "Palun sisestage e-posti aadress ja kiri!")
        return

    # Создание email-сообщения
    msg = EmailMessage()
    msg.set_content(kiri)  # Устанавливаем содержимое письма
    msg['Subject'] = teema  # Тема письма
    msg['From'] = sender_email  # Отправитель
    msg['To'] = ", ".join(kellele)  # Получатели

    # Добавление вложений
    for file in failitee:
        if file:
            try:
                with open(file, 'rb') as fpilt:
                    pilt = fpilt.read()
                msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
            except Exception as e:
                messagebox.showerror("Viga", f"Faili lisamine ebaõnnestus: {e}")
                return

    # Отправка письма
    try:
        context = ssl.create_default_context()  # Создаем безопасное соединение
        server = smtplib.SMTP(smtp_server, port)  # Подключаемся к SMTP серверу
        server.starttls(context=context)  # Включаем защищенное соединение
        server.login(sender_email, password)  # Логинимся
        server.send_message(msg)  # Отправляем письмо
        server.quit()  # Закрываем соединение
        messagebox.showinfo("Informatsioon", "Kiri saadetud edukalt!")  # Уведомление об успешной отправке
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Viga: {e}")  # Сообщение об ошибке

# Создание главного окна GUI
root = tk.Tk()
root.title("E-kirja saatmine")  # Заголовок окна
root.configure(bg="white")  # Цвет фона
root.geometry("500x350")  # Размер окна

# Определение цветов
bg_color = "blue"
fg_color = "white"
btn_color = "darkblue"
btn_fg = "white"

# Создание меток (Label)
labels = ["EMAIL:", "TEEMA:", "LISA:", "KIRI:"]
for i, text in enumerate(labels):
    label = Label(root, text=text, bg=bg_color, fg=fg_color, font=("Arial", 12, "bold"), width=10, anchor="w")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="nsew")

# Поля ввода (Entry, Text)
email_entry = Entry(root, width=40)  # Поле ввода email
email_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

subject_entry = Entry(root, width=40)  # Поле ввода темы
subject_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

attach_entry = Entry(root, width=40)  # Поле ввода прикрепленных файлов
attach_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

message_text = Text(root, width=40, height=8)  # Поле ввода сообщения
message_text.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

# Кнопки (Buttons)
add_image_btn = Button(root, text="LISA PILT", bg=btn_color, fg=btn_fg, font=("Arial", 12, "bold"), command=vali_pilt)
add_image_btn.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

send_btn = Button(root, text="SAADA", bg=btn_color, fg=btn_fg, font=("Arial", 12, "bold"), command=saada_kiri)
send_btn.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# Настройка колонок для растяжения
root.columnconfigure(1, weight=1)

root.mainloop()
