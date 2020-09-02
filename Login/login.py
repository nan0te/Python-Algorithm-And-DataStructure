class Login:

    def SignUp(user,passwd):
        if user == user.file:
            print('usuario exist')
        elif passwd.isalnum() == true:
            print('the password must contain one capital letter, a number and a special character')
        else:
            print('account created succesfully')

    def SignIn(user,passwd):
        if user == user.file and passwd == user.file:
            print('Welcome!')
        elif user == user.file and passwd != user.file:
            print('password incorrect')
        else:
            print('account does not exist')

