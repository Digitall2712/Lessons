def send_email(message, recipient,* ,sender = "university.help@gmail.com"):
    if check_email(sender,recipient) == True:
        if sender != recipient:
            if sender != "university.help@gmail.com":
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")
            else:
                print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")
        else:
            print("Нельзя отправить письмо самому себе!")
    else:
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>.")

def check_email(sender, recipient):
    good_sender = False
    good_recipient = False
    all_good = False
    domains = ('.com', '.ru', '.net')
    if sender.lower().endswith(domains):
        for i in range(len(sender)):
            if sender[i] == '@':
                good_sender = True
    if recipient.lower().endswith(domains):
        for i in range(len(recipient)):
            if recipient[i] == '@':
                good_recipient = True
    if good_sender and good_recipient == True:
        all_good = True
    return(all_good)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')




