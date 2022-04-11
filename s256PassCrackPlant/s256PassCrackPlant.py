from pwn import *
import sys
import re

'''
Sha256 password cracker using rockyou.txt.
It uses regex to validate if the input is a valid sha256 hash.
'''

# Checks if the input only has a-f, A-F, and numeric characters, and is 64 characters.
def validateSha256(inputHash):
	# ^[A-Fa-f0-9]{64}$
	regex = re.compile('^[A-Fa-f0-9]{64}$')
	match = regex.match(str(inputHash))
	return bool(match)

# Cracks the input based on rockyou.txt.
def crackHash(inputHash):
	password_list = open("/usr/share/wordlists/rockyou.txt", "r", encoding='latin-1')
	attempts = 1

	try:
		with log.progress(f"Attempting to crack: {input_hash}") as p:
			for password in password_list:
				password = password.strip("\n").encode('latin-1')
				password_hash = sha256sumhex(password)
				p.status(f"{attempts} {password.decode('latin-1')} == {password_hash}")
				if input_hash == password_hash:
					p.success(f"Password hash found after {attempts} attempts! {password.decode('latin-1')} hashes to {password_hash}!")
					exit()
				attempts += 1
			p.failure("Password hash not found.")
	except KeyboardInterrupt:
		print("Quitting due to the user input Ctrl^C.")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Invalid arguments!")
		print(f"{sys.argv[0]} <sha256sum>")
		exit()

	# Check if the input is a valid sha256 hash.
	if not validateSha256(sys.argv[1]):
		print("The input is not a valid sha256 hash.")
		exit()
	else:
		print("The input is a valid sha256 hash.")

	# Assignments
	input_hash = sys.argv[1]

	crackHash(input_hash)