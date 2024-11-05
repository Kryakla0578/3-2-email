def send_emails(message, recipient, *, sender='university.help@gmail.com'):
    if ('@' and ('com' or '.ru' or '.net')) not in (recipient and sender) and recipient != sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Невозможно отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'Неизвестный отправитель {sender}')
    else:
        print('Что-то пропустил :)')

send_emails('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_emails('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_emails('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_emails('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

