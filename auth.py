
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
    return auth
    

pwdb = {"dina":"hello", 
        "phil":"password"}

username, password = get_credentials()
authenticate(username, password, pwdb)

