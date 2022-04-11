# SSHBrutePlant
SSH brute force script written in Python 3.

# Usage
```python3 sshBrutePlant.py 127.0.0.1 username password_list```

```
python3 sshBrutePlant.py                       
sshBrutePlant.py usage: python3 sshBrutePlant.py host username password_list
[*] Example: python3 sshBrutePlant.py 127.0.0.1 root /usr/share/wordlists/rockyou.txt
[*] A single user name or a wordlist of user names may be supplied.
[*] Password_list must be a wordlist.
```
The script was tested against the author's own virtual machine, kali linux, 127.0.0.1.
For examples below, a credential `hamster:hAmst428PASS@#$` was used.

user.txt had three entries.
```
chinchilla
guinea_pig
hamster
```

pass.txt had four entries.
```
1
2
hAmst428PASS@#$
2
```
## Using a user name
```
python3 sshBrute2.py 127.0.0.1 hamster pass.txt
[-] The supplied wordlist hamster does not exist.
[+] The supplied user name hamster will be used as a user name.
[+] The supplied password wordlist pass.txt will be used.
Current Setup
Host: 127.0.0.1
User name or wordlist: hamster
Password wordlist: pass.txt
Proceed? (y/n): y
[*] [1] Attempting password: 1...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [2] Attempting password: 2...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [3] Attempting password: hAmst428PASS@#$...
[+] Connecting to 127.0.0.1 on port 22: Done
[*] hamster@127.0.0.1:
    Distro    Kali 2022.1
    OS:       linux
    Arch:     amd64
    Version:  5.15.0
    ASLR:     Enabled
[+] Valid credential found: hamster:hAmst428PASS@#$.
[*] Closed connection to '127.0.0.1'
```

## Using a wordlist for user names
```
python3 sshBrute2.py 127.0.0.1 user.txt pass.txt 
[+] The supplied wordlist of user user.txt will be used.
[+] The supplied password wordlist pass.txt will be used.
Current Setup
Host: 127.0.0.1
User name or wordlist: <_io.TextIOWrapper name='user.txt' mode='r' encoding='UTF-8'>
Password wordlist: pass.txt
Proceed? (y/n): y
[*] Using chinchilla as the user name...
[*] [1] Attempting password: 1...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [2] Attempting password: 2...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [3] Attempting password: hAmst428PASS@#$...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [4] Attempting password: 2...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] Using guinea_pig as the user name...
[*] [1] Attempting password: 1...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [2] Attempting password: 2...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [3] Attempting password: hAmst428PASS@#$...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [4] Attempting password: 2...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] Using hamster as the user name...
[*] [1] Attempting password: 1...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [2] Attempting password: 2...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [3] Attempting password: hAmst428PASS@#$...
[+] Connecting to 127.0.0.1 on port 22: Done
[*] hamster@127.0.0.1:
    Distro    Kali 2022.1
    OS:       linux
    Arch:     amd64
    Version:  5.15.0
    ASLR:     Enabled
[+] Valid credential found: hamster:hAmst428PASS@#$.
[*] Closed connection to '127.0.0.1'
```

While testing the script, I noticed that the paramiko library throws FileNotFoundError if the user does not have a home directory, in which case the script suggests manual logging in with a valid credential.
```
python3 sshBrute2.py 127.0.0.1 hamster pass.txt
[-] The supplied wordlist hamster does not exist.
[+] The supplied user name hamster will be used as a user name.
[+] The supplied password wordlist pass.txt will be used.
Current Setup
Host: 127.0.0.1
User name or wordlist: hamster
Password wordlist: pass.txt
Proceed? (y/n): y
[*] [1] Attempting password: 1...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [2] Attempting password: 2...
[-] Connecting to 127.0.0.1 on port 22: Failed
[-] Invalid password
[*] [3] Attempting password: hAmst428PASS@#$...
[+] Connecting to 127.0.0.1 on port 22: Done
[+] The credential seems valid, but the user has no home directory.
[+] Try logging into the target manually with hamster:hAmst428PASS@#$
```

# Disclaimer
The script was written to better understand Python and for educational purposes. The author will not be held responsible for any damage and harm caused due to misuse of it. Please respect the local laws of your area.
