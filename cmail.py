import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
<<<<<<< HEAD
    server.login('ytsofficial111@gmail.com','phoqgxytashtakjj')
=======
    server.login('ytsofficial111@gmail.com','xkqphycckfdsaxsa')
>>>>>>> da999b4148f9628c2715c2844124923b400f0ea2
    msg=EmailMessage()
    msg['From']='ytsofficial111@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
