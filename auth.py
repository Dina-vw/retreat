import json
def get_credentials():
	username = input('Type username: ')
	password = input('Type password: ') 
	return username, password

def authenticate(username, password, pwdb):
    auth = False
    if username in pwdb: 
        if password == pwdb[username]:
            print('Authentication successful')
            auth = True
        else: 
            print('Wrong password!')
    else: 
        print('User not known')
        add_user(username, password, pwdb)
    return auth
    



def write_pwdb(pwdb):
    with open('pwdb.json', 'wt') as pwdb_file:  
        json.dump(pwdb, pwdb_file)
    print('pwdb written!')
   
def read_pwdb():
    with open('pwdb.json', 'rt') as pwdb_file:
        pwdb = json.load(pwdb_file)
    return pwdb
def add_user(username, password, pwdb):
    response = input('Do you want to create a new user name? [y/n]')
    if response == 'y':
        pwdb[username] = password
        write_pwdb(pwdb)
    else: 
        print('User not added')
username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)
