import os
from email.message import EmailMessage
import ssl 
import smtplib
import Receiver
# Import buat bisa konek ke email/send email
email_1 = 'KentzoIndoAi@gmail.com' 
email_2 = 'kentzopietro@gmail.com'
email_1_password = 'hwtlghjidscesfok'
# My email, target email, password
Isi = 'Halo'
isi = 'Selamat Siang'
# email pengirim, email penerima, pw email
em = EmailMessage()
em['From'] = email_1
em['To'] = email_2
em['Subject'] = Isi
em.set_content(isi)
# Untuk mengirim email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# Email Server
# Smtp = Simple Mail Transfer Protocol
    smtp.login(email_1, email_1_password)
# Login email/password 16 digits
    smtp.send_message(em)
# Message yang akan dikirim (em)

