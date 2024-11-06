import smtplib # модуль для работы с smtp-протоколом

# данные о пользователях
from_address = "mariiamorina@yandex.ru" # адрес почты отправителя
password = "usoxwngsgsxurgsc" # пароль отправителя

to_address = "mariiamorina17@mail.ru" # адрес почты получателя

# текст письма
message = """\
From: mariiamorina@yandex.ru
To: mariiamorina17@mail.ru
Subject: Lab1.
Content-Type: text/plain; charset="UTF-8";

Lab is working!
"""

# создание объекта SMTP и отправка письма
smtp_server = smtplib.SMTP_SSL('smtp.yandex.ru:465') # связываемся с почтовым сервером
smtp_server.login(from_address, password) # заходим в почтовый ящик
smtp_server.sendmail(from_address, to_address, message) # отправляем письмо
smtp_server.quit() # закрываем соединение с сервером
