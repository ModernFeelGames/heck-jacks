# Made by modern_o on roblox. Thank me later.

import time
import ctypes
from num2words import num2words
import win32com.client as client
sendKey = client.Dispatch('WScript.Shell')

print("Heck Jacks Bot for Roblox! Made by modern_o <3")

# ----------------------- #

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Stolen from stackoverflow lmao, roblox is dumb and needs DirectInput

# ----------------------- #

jacks = input("How many heck jacks would you like to do?: ")
address = input("How would you like to address your supervisor? (E.g Sir.): ")
delay = input("How long would you like to delay between jumps in seconds? 2-3 is recommended: ")

jacks2 = int(jacks)
currentNums = 1
delay2 = int(delay)

def doHellJacks(amount):
    global delay2
    global currentNums
    lol = num2words(currentNums)+"*"
    counting = 1
    arrayOfJacks = list(lol)
    for f in arrayOfJacks:
        if f == "-":
            print("")
            # Just ingore -
        elif f == "*":
            PressKey(0x39)
            time.sleep(.2)
            ReleaseKey(0x39)
            time.sleep(delay2+1)
            textlmao = num2words(currentNums).upper()+", " + address.upper()
            sendKey.SendKeys('/')
            time.sleep(.2)
            sendKey.SendKeys(textlmao)
            time.sleep(.2)
            PressKey(0x1C)
            time.sleep(.2)
            ReleaseKey(0x1C)
        else:
            PressKey(0x39)
            time.sleep(.2)
            ReleaseKey(0x39)
            time.sleep(delay2)
            sendKey.SendKeys('/')
            time.sleep(.3)
            sendKey.SendKeys(f.upper())
            time.sleep(.2)
            PressKey(0x1C)
            time.sleep(.2)
            ReleaseKey(0x1C)
            

    if currentNums < jacks2:
        currentNums = float(currentNums) + float(1)
        time.sleep(delay2)
        doHellJacks(jacks2)

print("Click on roblox. You have 5 Seconds.")
time.sleep(1)
print("Click on roblox. You have 4 Seconds.")
time.sleep(1)
print("Click on roblox. You have 3 Seconds.")
time.sleep(1)
print("Click on roblox. You have 2 Seconds.")
time.sleep(1)
print("Click on roblox. You have 1 Seconds.")
time.sleep(1)
doHellJacks(jacks2)
print("Done!")
sendKey.SendKeys('/')
time.sleep(.2)
sendKey.SendKeys('DONE, ' + address)
time.sleep(.2)
PressKey(0x1C)
time.sleep(.2)
ReleaseKey(0x1C)
