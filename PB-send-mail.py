import smtplib
import os
message = 'Subject: {}\n\n{}'.format('Subject', 'DESCRIPTIONS')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
email= 'YOUR EMAIL'
server.login(email, os.getenv("CLV")) # CLV as environment variable if you would like to do so. You need the app password of gmail, you can generate in your gmail account manager

server.sendmail(email, 'email-receptor', message)

server.quit()
print('Enviado')
print("Prueba de mi git")