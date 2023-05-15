import smtplib
import Email_Inputs


subject = Email_Inputs.Subject
msg = Email_Inputs.Message

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(Email_Inputs.Email_Address, Email_Inputs.Password)

except Exception as e:
    print(e)


def send_email(subject, msg):
    message = 'Subject: {}\n\n{}'.format(subject.upper(), msg)
    server.sendmail(Email_Inputs.Email_Address, Email_Inputs.Receiver, message)


for i in range(int(input("No. of times to send mail:"))):
    send_email(Email_Inputs.Subject, Email_Inputs.Message)
    i += 1
    print("["+str(i)+"] Mail sent Successfully to " + Email_Inputs.Receiver)

server.quit()
