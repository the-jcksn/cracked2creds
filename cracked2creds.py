#cracked2creds
#python script for matching NTDS usernames with cracked hashcat hashes/passwords
#github.com/the-jcksn
#dont be naughty - only for use by law abiding citizens staying IN SCOPE!


ntds_file = input('Please enter the name of the ntds file: ')
cracked_file = input('Please enter the name of the file containing the cracked hashes (or press enter to use hashcat potfile): ')
print()
output_file = ntds_file + '_passwords.txt'
if cracked_file == '':
    cracked_file = '.local/share/hashcat/hashcat.potfile'
with open(cracked_file,'r') as cracked:
        for line in cracked:
            hash = line.split(':')[0]
            password = line.split(':')[1]
            if len(password) > 1:
                with open(ntds_file,'r') as ntds:
                    for line2 in ntds:
                        if hash in line2:
                            user = line2.split(':')[0]
                            print(user + ':' + password[:-1])
                            with open(output_file,'a') as output:
                                output.write(user + ':' + password)
print('\n\nAll done. Results written to ' + output_file + '.')
