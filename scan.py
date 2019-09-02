from gpiozero import LED
import subprocess
import time

led = LED(17)

def main():
    a = False
    while True:
        time.sleep(1)
        l = subprocess.check_output(['iwlist', 'scanning']).splitlines()
        for line in l:
            if 'Test123' in line:
                print('alarming')
                a = True
                break
        else:
            a = False
        if a:
            led.on()
        else:
            led.off()

if __name__ == '__main__':
    main()
