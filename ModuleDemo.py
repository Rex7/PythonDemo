user = "regis"
pass_word = 9821572187


def usercheck(name, password):
    if name == user and pass_word == password:
        print("Welcome master rex")
        default_argument(password, name)
    else:
        print("Sorry your not authorized user")
    return


def default_argument(password, name="admin"):
    print("Name :{0} \n Password:{1}".format(name, password))