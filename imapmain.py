import imaplib # модуль для работы с imap-протоколом
import email # модуль для чтения, записи и отправки простых сообщений
from email.header import decode_header # функция для декодирования значения заголовка сообщения без преобразования набора символов

# подключение к серверу
imap_server = imaplib.IMAP4_SSL('imap.yandex.ru') # связываемся с почтовым сервером
imap_server.login("mariiamorina@yandex.ru", "usoxwngsgsxurgsc") # заходим в почтовый ящик

# получение информации о папке
mailbox = 'INBOX' # папка "входящие"
typ, response = imap_server.select(mailbox) # выбор папки "входящие" для просмотра сообщений
if typ != 'OK': # возникла ошибка
    print(f'Failed to select folder {mailbox}') # выводим сообщение об ошибке
    imap_server.close() # закрываем соединение с сервером
    imap_server.logout() # выходим из почтового ящика
    exit() # выходим из программы

# вывод количества писем в папке
typ, num_messages = imap_server.search(None, 'ALL') # поиск по всей папке
if typ == 'OK': # если не возникло ошибок
    message_ids = num_messages[0].split() 
    num_messages = len(message_ids)
    print(f'\nNumber of letters in {mailbox}: {num_messages}\n\n')

# поиск письма по заголовку
search_subject = 'Lab number 6. Mail server.' # заголовок
typ, msgnums = imap_server.search(None, f'HEADER Subject "{search_subject}"') # поиск сообщения по заголовку
if typ == 'OK': # если сообщение найдено
    message_ids = msgnums[0].split() # получаем id сообщений
    if len(message_ids) > 0:
        # получение информации о первом найденном письме
        msgnum = message_ids[0]
        typ, msg_data = imap_server.fetch(msgnum, '(RFC822)') # получаем письмо
        email_message = email.message_from_bytes(msg_data[0][1]) # декодируем письмо

        # извлечение заголовков и тела письма
        # записываем имя отправителя
        sender, sender_encoding = decode_header(email_message['From'])[0]
        if isinstance(sender, bytes): # если тип имени отправителя - байты
            sender = sender.decode(sender_encoding) # то декодируем строку из заданных байтов
        # записываем заголовок
        subject, subject_encoding = decode_header(email_message['Subject'])[0]
        if isinstance(subject, bytes): # если тип заголовка - байты
            subject = subject.decode(subject_encoding) # то декодируем строку из заданных байтов
        # записываем дату
        sent_date = email.utils.parsedate_to_datetime(email_message['Date'])
        # записываем тело сообщения
        body = ''
        for part in email_message.walk(): # обходим полученный объект
            if part.get_content_type() == 'text/plain': # если тип сообщения - простой текст
                body = part.get_payload(decode=True).decode('utf-8') # то декодируем сообщение
                break

        # вывод информации о найденном письме
        print(f'From: {sender}') # отправитель
        print(f'Subject: {subject}') # заголовок
        print(f'Sending time: {sent_date}') # время отправления
        print(f'Message:\n{body}\n') # само сообщение

# вывод заголовков пяти последних писем
typ, response = imap_server.search(None, 'ALL') # поиск по всей папке
if typ == 'OK': # если не возникло ошибок
    message_ids = response[0].split() # получаем id сообщений
    num_messages = min(5, len(message_ids)) # выбираем минимальное количество сообщений для вывода
    for i in range(num_messages):
        # получение информации о письмах
        msgnum = message_ids[-(i+1)]
        typ, msg_data = imap_server.fetch(msgnum, '(RFC822)') # получаем письмо
        email_message = email.message_from_bytes(msg_data[0][1]) # декодируем письмо
        print(f'Letter #{i+1}: {email_message["From"]} ~ {email_message["Subject"]}') # выводим имя отправителя и заголовок письма

imap_server.close() # закрытие соединения
imap_server.logout() # выход из почтового ящика