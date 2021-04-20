import os
import filecmp
class password_screen():
    def check_one():
        w = input("input your name here")
        x = input("input your username here")
        y = input("input your pasword here")
        os.system("notepad checkone.txt")
        with open("checkone.txt", "w") as q:
            a = q.write(w)
            b = q.write(x)
            c = q.write(y)
            q.close()

    def check_two():
        l = filecmp.cmp('checkone.txt', 'passwords.txt')
        print(l)

        if l == False:
            print("access denied")
        else:
            print("access granted")

    

d = password_screen()
password_screen.check_one()
password_screen.check_two()
                
        
    
