import random
import hashlib
import datetime
from twilio.rest import Client

def timeChunk():
	a = datetime.datetime.now().timestamp()
	return a//30
def send_sms(text,userph):
	account_sid = '.'
	auth_token = '.'

	client = Client(account_sid, auth_token)
	message = client.messages.create(
								from_='',
								body = text,
								to = userph,
							)

def passw():
	plainText = random.randint(0,2000)
	plainText = str(plainText)
	userph = input("What is your phone number? \n:")
	send_sms(plainText,userph)
	encryptedText = hashlib.md5(plainText.encode())
	encryptedText = encryptedText.hexdigest()
	time = timeChunk()
	encryptedText = encryptedText + str(time)

	f = open("test.FAT", "a+")
	f.write(encryptedText)
	f.write("\n")
	f.close()
	test()
def test():
	plainIO = input("passw\n:")
	f = open("test.FAT", "r")
	encryptedIO = hashlib.md5(y.encode())
	encryptedIO = str(encryptedIO.hexdigest())
	time = timeChunk()
	encryptedIO = encryptedIO + str(time)
		

	for line in f.readlines():
		if encryptedIO in line:
			print("Sucess")
			break
		else:
			continue
	print("Not a valid code")



def main():
	passw()
main()
