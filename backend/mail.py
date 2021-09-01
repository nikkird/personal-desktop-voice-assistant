import smtplib

from backend.stt import listen
from backend.tts import Speak
from res.credentials import credentials


def send_email():
    subject = ""
    message = ""
    Speak('What is the subject? >')
    subject = listen()
    Speak('What should I say? >')
    message = listen()
    if "subject blank" in subject.lower():
        subject = ""
    if "message blank" in message.lower():
        message = ""
    content = 'Subject: {}\n\n{}'.format(subject, message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login(credentials.cred['demo_id'], credentials.cred['demo_pas'])
    server.sendmail(credentials.cred['demo_id'], credentials.cred['to_nik'], content)
    server.close()
    Speak("Done")
