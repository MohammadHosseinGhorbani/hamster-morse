import pyautogui
from time import sleep
import sys

word = sys.argv[1]

code_trans = str.maketrans(
    {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }
)
code = ' '.join(word).upper().translate(code_trans)
print(code)
sleep(5)

for i in code.split():
    for j in i:
        match j:
            case '.':
                pyautogui.click()
                sleep(0.5)
            case '-':
                pyautogui.mouseDown()
                sleep(0.5)
                pyautogui.mouseUp()
                sleep(0.5)
    sleep(0.7)
