import smtplib
import imaplib
import email
import time
#copy the placeholder to config.py and fill in your values
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, PHONE_ADDRESS
SMTP_SERVER='smtp.gmail.com'

def read_text(message):
    for part in message.walk():
        ctype = part.get_content_type()
        if ctype in ["text/plain"]:
            message = (part.get_payload(decode=True))
            return message.decode()

if __name__=="__main__":
	#authenticate with smtp server
	#note that this does not handle reauthenticating when google wants you to
	server = smtplib.SMTP_SSL(SMTP_SERVER, 465)
	server.ehlo()
	print(server.login(EMAIL_ADDRESS, EMAIL_PASSWORD))
	
	#Send a text
	input("Press enter to send a text")
	print("Sending text...")
	server.sendmail(EMAIL_ADDRESS, PHONE_ADDRESS, "Hello friend")
	
	#Receiving Texts
	mail = imaplib.IMAP4_SSL(SMTP_SERVER)
	print(mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD))
	print("Let's look at your mailbox")
	print(mail.select('inbox'))
	
	print("uh oh byte strings. That's not human")
	print("Now let's get our messages")
	_, ids = mail.search(None, "ALL")
	ids=ids[0].split()
	old_ids=ids.copy()
	print(ids)
	#parse it
	input("Big welcome message coming are you ready? press enter")
	print(mail.fetch(ids[0], '(RFC822)')[1])
	
	#very ugly. let's use the email library to read it
	message=email.message_from_bytes(mail.fetch(ids[0], '(RFC822)')[1][0][1])
	for part in message.walk():
		ctype = part.get_content_type()
		if ctype in ["text/plain"]:
			message = (part.get_payload(decode=True))
			print(message.decode())
			
	input("Reply to the text you got earlier and WAIT TILL IT SHOWS IN GMAIL AND THEN\nEnter to continue...")
	print("Starting listener loop. Control+C to quit")

	while True:
		mail.select('inbox')#this refreshes your inbox
		_, ids = mail.search(None, "ALL")
		ids=ids[0].split()
		print(ids)
		if len(ids)!=len(old_ids):
			for id in ids:
				if id not in old_ids:
					message=email.message_from_bytes(mail.fetch(id, '(RFC822)')[1][0][1])
					text=read_text(message)
					print(message.get("from"), text)
					server.sendmail(EMAIL_ADDRESS, PHONE_ADDRESS, text+"?")
		old_ids=ids
		time.sleep(1)