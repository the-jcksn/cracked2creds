# cracked2creds

Cracking NTDS files is great fun, working out which cracked hash corresponds to which user in the NTDS is not as much fun. This script will take your NTDS file, compare it against the cracked hashes in the potfile (or other specified file of cracked hashes) and output lines of username:password. Which in my opinion, is more useful than hashcats 'hash:password' format.

Point and shoot, 'python3 cracked2creds.py' , give it the destination of the NTDS file when prompted, and get it output to terminal and a text file. Job done.
