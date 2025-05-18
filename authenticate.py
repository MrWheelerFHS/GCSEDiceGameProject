def authenticate(username, password):

    # Opens the file containing usernames
    users=open("usernames.txt","r")
    # puts each line of the file into an array
    userList=(users.readlines())
    # Closes the usernames file
    users.close()

    # Opens the file containing passwords
    passwords=open("passwords.txt","r")
    # puts each line of the file into an array
    passwordList=(passwords.readlines())
    # Closes the usernamespassword file file
    passwords.close()

    userFound=False

    while userFound==False:
        for i in range(0,len(userList),1):
                        
            if username==userList[i].strip():
                
                if password==passwordList[i].strip():
                    userFound=True
                    #print("Welcome", userList[i].strip()) 
                    return userList[i].strip()
                else:
                    userFound=True    
    return False

user1=authenticate("paulwhqeeler","pqw1")
if user1!= False:
    print("Welcome ",user1)
else:
    print("Username and or password not recognised")
