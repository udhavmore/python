import smtplib

content = 'My sec Email'
mail = smtplib.SMTP("smtp.gmail.com:587")
print("SMTP")
mail.ehlo()
print("ehlo")
mail.starttls()
print("tls")
mail.login('', '')
print("Login successful")


for i in range(3):
    mail.sendmail('', '', content)
    i += 1
    print("[" + str(i) + "] Mail sent Successfully ")
