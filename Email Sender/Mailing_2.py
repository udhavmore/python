import smtplib
import schedule
import time
import datetime

FROM = ""  # Sender Email ID(Gmail)
Password = ""  # Password of Email ID(Gmail)
print(FROM)
TO = ""
SUBJECT = "test mail".upper()
TEXT = "this is to test code to send 3 mails every hour ".capitalize()
now = datetime.datetime.now()

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % FROM,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server = smtplib.SMTP('smtp.gmail.com:587', timeout=None)
    server.ehlo()
    server.starttls()
    server.login(FROM, Password)
    print("Login Successful")
    server.timeout = None
except Exception as e:
    print(e)


def mailing():
    server.sendmail(FROM, TO, BODY)


def job():
    for i in range(1):
        i = + 1
        mailing()
        time_now = now.strftime("%Y-%m-%d %H:%M:%S")
        print("[" + str(i) + "] Mail sent Successfully to " + TO + "at : " + str(now.strftime("%Y-%m-%d %H:%M:%S")))


print("Time>>" + str(now.strftime("%Y-%m-%d %H:%M:%S")))
print("Sending Mail...")
# schedule.every(1).hours.do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
