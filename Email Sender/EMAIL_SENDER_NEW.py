import smtplib
import schedule


FROM = ""                # Sender Email ID(Gmail)
Password = ""                                   # Password of Email ID(Gmail)
print(FROM)
TO = ''
SUBJECT = 'scheduled mail'.upper()
TEXT = 'hello this is a test mail to check the schedule which will send 2 mail in every 2 minutes'.capitalize()

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


def job():
    print("this is test")
    # server.sendmail(FROM, TO, BODY)


for i in range(1):
    schedule.every(1).minutes.do(job)
    # i += 1
    # print("[" + str(i) + "] Mail sent Successfully to " + TO)
