import re
def validate():
    while True:

        password=input()
        if re.search('[0-9]',password) is None:
            print('again')
        elif re.search('[A-Z]',password) is None:
            print('again')
        elif re.search('[a-z]',password) is None:
            print('gain')
        elif re.search('[~!@#$%^&*]',password) is None:
            print('again')
        elif len(password)<8:
            print('again')
        else:
            break
validate()