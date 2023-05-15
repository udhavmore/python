import smtplib


FROM = ""                # Sender Email ID(Gmail)
Password = ""                                   # Password of Email ID(Gmail)
print(FROM)
TO = input("Enter Email ID:")
SUBJECT = input("Subject:").upper()
TEXT = input("Enter message:").capitalize()

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % FROM,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])
try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(FROM, Password)
except Exception as e:
    print(e)


def send_mail():
    server.sendmail(FROM, TO, BODY)


for i in range(int(input("No. of times to send mail:"))):
    send_mail()
    i += 1
    print("["+str(i)+"] Mail sent Successfully to " + TO)

server.quit()
buffer=["A"]
while len(buffer) <= 10:
    buffer.append()