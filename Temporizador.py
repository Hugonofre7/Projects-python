import time

def temporizador(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  
        time.sleep(1)
        t -= 1

    print("Comenzar Temporizador!!")

t = input("Introduzca el tiempo: ")

temporizador(int(t))
