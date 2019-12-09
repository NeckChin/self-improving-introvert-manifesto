import os
import subprocess
import time
import sys

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

time.sleep(1)
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.RED + 'Today’s fast moving society favors extroversion.' + color.END+"\r", flush=True)
os.linesep
time.sleep(1)
print(color.RED + 'For those with introverted tendencies to survive and thrive,' + color.END+"\r")
time.sleep(1)
print(color.RED + 'they must' + color.END+"\r")
time.sleep(1)
print(color.BOLD +color.RED + 'adopt' + color.END+"\r")
time.sleep(0.5)
print(color.BOLD +color.RED + 'and' + color.END+"\r")
time.sleep(0.5)
print(color.BOLD +color.RED + 'change,' + color.END+"\r")
time.sleep(1)
print(color.RED + 'becoming a self-improving introvert who '+color.BOLD+'fakes it until they make it. ' + color.END+"\r\n")
time.sleep(1)

sys.stdout.write(' loading.')
sys.stdout.flush()
time.sleep(.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(.5)
for i in range(50):
    time.sleep(0.02)
    printProgressBar(i + 1, 50, prefix = "\033[1;32;40m Phase1"+color.END, suffix = 'Compiled', length = 50)
print();

sys.stdout.write(' loading.')
sys.stdout.flush()
time.sleep(.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(.5)
for i in range(50):
    time.sleep(0.02)
    printProgressBar(i + 1, 50, prefix = "\033[1;32;40m Phase2"+color.END, suffix = 'Compiled', length = 50)
print(); 

sys.stdout.write(' loading.')
sys.stdout.flush()
time.sleep(.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(.5)
sys.stdout.write('.')
sys.stdout.flush()
time.sleep(.5)
for i in range(50):
    time.sleep(0.02)
    printProgressBar(i + 1, 50, prefix = "\033[1;32;40m Phase3"+color.END, suffix = 'Compiled', length = 50)
print();
time.sleep(3)

print("\033[1;32;40m \tPHASE 1: Fundamental beliefs that will allow change to happen\r"+color.END)
time.sleep(1.9)
print(' • In the scope of things, other peoples’ opinions are irrelevant\r')
time.sleep(1.8)
print(' • Nature, self, habits, viewpoints, can be changed\r')
time.sleep(1.7)
print(' • Seeking improvement is different from wanting to be perceived as different\r')
time.sleep(1.6)
print(' • As long as change is for yourself, and not for others, it’s ok\r')
time.sleep(1.5)
print(' • If you don’t like the way others see yourself and want to change because of that...\r')
time.sleep(2)
print('   that is ok too\r')
time.sleep(1.9)
print(' • “This is who I am, my position and self is unchangeable” is a damaging mentality; there is always room for improvement\r')
time.sleep(1.8)
print(' • Can be temporarily content, but never settle.\r')
time.sleep(1.7)
print(' • Loss of identity allows for a better you to be shaped\r')
time.sleep(1.6)
print(' • The fake will eventually become the real\r')
time.sleep(1.5)
print(' • Uncertainty means there is potential for progress\r\n')
time.sleep(3)

print("\033[1;32;40m \tPHASE 2: Carry out changes that have to happen\r"+color.END)
time.sleep(1.9)
print(' • You need to want to better yourself\r')
time.sleep(1.8)
print(' • Recognize your weaknesses\r')
time.sleep(1.7)
print(' • Recognize the parts of yourself that you don’t like\r')
time.sleep(1.6)
print(' • Address the parts of yourself that you don’t like\r')
time.sleep(1.5)
print(' • Be more cognizant when the parts of yourself that you don’t like surface\r')
time.sleep(1.4)
print(' • Enact change, and fake the change you want to become\r')
time.sleep(1.3)
print(' • Enforce the change, make it into a habit\r')
time.sleep(1.2)
print(' • Live the habit, absorb it into your lifestyle\r\n')
time.sleep(3)

print("\033[1;32;40m \tPHASE 3: Recognizing why one who BELIEVES should carry out CHANGE\r"+color.END)
time.sleep(1)
print(' • Trying something different outside of comfort zone helps you discover what is and what isn’t you\r')
time.sleep(1.2)
print(' • Wanting to become who you want to be is not a crime\r')
time.sleep(1.5)
print(' • Being open to change and keeping an open mind is important\r')
time.sleep(1.1)
print(' • There are '+color.UNDERLINE+color.BOLD+'infinite'+color.END+' branching paths forward, it’s up to you to '+color.BOLD+'choose steps that you won’t regret\r'+color.END)