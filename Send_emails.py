import smtplib 

def send_email(username, pswrd, to, sender, subject, message)
	conn = smtplib.SMTP('smtp.gmail.com',587) #gmail smtp and port number
	conn.ehlo() #connection start
	conn.starttls() #to encrpyt pws
	conn.login(username,pswrd) 
	conn.sendmail(sender, to,subject + ':\n\n' + message)
	conn.quit()

