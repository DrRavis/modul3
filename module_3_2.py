def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if check_email(recipient) == True and check_email(sender) == True:
        if sender != recipient:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print('Нельзя отправить письмо самому себе')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

def check_email(email):
    end = ['.com', 'net', 'ru']
    check_email = False
    for e in end:
        if '@' in email:
            if email.endswith(e) == True:
                check_email = True
                break
            else:
                continue
        else:
            break
    return check_email

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

