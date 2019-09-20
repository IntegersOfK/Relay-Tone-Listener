from gpiozero import LED
import subprocess
import time

led = LED(17)

def main():
    a = False
    while True:
        time.sleep(1)
        ps = subprocess.Popen(['sudo', 'iw', 'wlan0','scan', 'flush'], shell=False, stdout=subprocess.PIPE)
        grep = subprocess.Popen(['grep', 'SSID'], shell=False, stdin=ps.stdout, stdout=subprocess.PIPE)
        grep_output,_ = grep.communicate()

        for line in grep_output.split():
            print (line)
            if ('OnePlus' in line):
               print('-----> alarming <------')
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
