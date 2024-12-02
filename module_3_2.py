def send_email(recipient: str, *, sender='university.help@gmail.com'):
    if not all(['@' in recipient,'@' in sender, recipient.endswith('.ru') or
                recipient.endswith('.com') or recipient.endswith('.net'), sender.endswith('.ru') or
                sender.endswith('.com') or sender.endswith('.net')]):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email('vasyok1337@gmail.com')
send_email('urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

