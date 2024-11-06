import poplib # модуль для работы с pop3-протоколом
from email import parser # парсер, который понимает большинство структур документов электронной почты
import ssl # модуль, который обеспечивает доступ к средствам шифрования транспортного уровня и одноранговой аутентификации для сетевых сокетов, как на стороне клиента, так и на стороне сервера

def read_pop3_emails(server, email, password): # функция для выполнения задачи
    try:
        # создание контекста SSL
        context = ssl.create_default_context()

        # подключение к POP3 серверу с использованием SSL
        mail_server = poplib.POP3_SSL(server, port=995, context=context)
        mail_server.user(email)
        mail_server.pass_(password)

        # получение количества писем
        num_messages = len(mail_server.list()[1])
        print(f"Количество писем: {num_messages}") # вывод количества писем

        # чтение писем
        for i in range(num_messages):
            # Получение номера письма
            raw_email = b"\n".join(mail_server.retr(i + 1)[1])
            email_message = parser.Parser().parsestr(raw_email.decode('utf-8'))

            # вывод заголовков письма
            print(f"Тема: {email_message['subject']}")
            if (num_messages < 4):
                print(f"От: {email_message['from']}")
                print(f"Дата: {email_message['date']}\n")

        # завершение работы с почтовым сервером
        mail_server.quit()

    # вывод сообщения об ошибке
    except Exception as e:
        print(f"Ошибка: {e}")
        raise

if __name__ == "__main__": # основная функция
    # POP3_SERVER = 'pop.yandex.ru'  # почтовый сервер
    # EMAIL = 'mariiamorina@yandex.ru' # адрес почты
    # PASSWORD = 'usoxwngsgsxurgsc' # пароль

    read_pop3_emails('pop.yandex.ru', 'mariiamorina@yandex.ru', 'usoxwngsgsxurgsc') # функция для работы с письмами