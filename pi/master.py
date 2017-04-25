from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout 
from random import randint
import os,time
import argparse
import base64
import json
import os


blue = (0, 0, 1, 1)
red = (1, 0, 0, 1)
white = (1,1,1,1)
green = [0,1,0,1]            
purple = [1,0,1,1]

######################################################################
# Menu
######################################################################
def load(x):
	xxx=0
def popup_message(msg):
        title="Message"
        popup = Popup(title=title, content=Label(text=msg), size=(435, 100), size_hint=(None, None))
        popup.bind(on_dismiss=load)
        popup.open()

def print1(x):
	print('trans')
	#os.system('scp pyramid.rtf root@192.168.1.25:/mnt/ramdisk/gcode.rtf;')
	os.system('sshpass -p "Just a bit off the block!" scp seshan.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf;')
	print('act')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')

def print2(x) :
	os.system('sshpass -p "Just a bit off the block!" scp rectangle.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')

def print3(x) :
	os.system('sshpass -p "Just a bit off the block!" scp maze.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print4(x) :
	os.system('sshpass -p "Just a bit off the block!" scp c3.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print5(x) :
	os.system('sshpass -p "Just a bit off the block!" scp maze2.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print6(x) :
	os.system('sshpass -p "Just a bit off the block!" scp lotus.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7(x) :
	os.system('sshpass -p "Just a bit off the block!" scp si.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7a(x) :
	os.system('sshpass -p "Just a bit off the block!" scp avg.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7b(x) :
	os.system('sshpass -p "Just a bit off the block!" scp legomfg.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7c(x) :
	os.system('sshpass -p "Just a bit off the block!" scp sman.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7d(x) :
	os.system('sshpass -p "Just a bit off the block!" scp pm.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7e(x) :
	os.system('sshpass -p "Just a bit off the block!" scp r2.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7f(x) :
	os.system('sshpass -p "Just a bit off the block!" scp maker.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')
def print7g(x) :
	os.system('sshpass -p "Just a bit off the block!" scp FIRST.rtf root@192.168.150.10:/mnt/ramdisk/prjs/master/gcode.rtf')
	os.system('sshpass -p "Just a bit off the block!" ssh root@192.168.150.10 "echo 1 > /mnt/ramdisk/prjs/master/run.rtf"')
	popup_message('printing')

def dropbear(self):
	os.system('~pi/cmds')

def wifi(self):
	os.system('ifdown wlan0;ifup wlan0')

def hotspot(self):
	os.system('~pi/hotspot')

def TTTrun(self):
    sm.current='TicTacToe'

def GVrun(self):
    sm.current='GV'

def exit(self):
    sm.current='menu'

def shutdown(self):
	os.system('poweroff')

MENUlayout = BoxLayout(orientation='vertical')
TTTlayout = BoxLayout(orientation='vertical')
GVlayout = BoxLayout(orientation='vertical')

# use a (r, g, b, a) tuple
#btn =  Button(text='Print "Seshan" [1]', background_color=blue, font_size=50)        
#btn.bind(on_press=print1)
#btn2 =  Button(text='Print 2 rectangles [5]', background_color=red, font_size=50)        
#btn2.bind(on_press=print2)
btn3 =  Button(text='Print a Maze (Circular) [2]', background_color=red, font_size=50)        
btn3.bind(on_press=print3)
#btn4 =  Button(text='Print a C3PO+R2D2 [1]', background_color=red, font_size=50)        
#btn4.bind(on_press=print4)
#btn5 =  Button(text='Print a Maze (Square) [2]', background_color=red, font_size=50)        
#btn5.bind(on_press=print5)
#btn6 =  Button(text='Print a Leaf [1]', background_color=blue, font_size=50)        
#btn6.bind(on_press=print6)
btn7 =  Button(text='Print Space Invaders (TM) [2]', background_color=blue, font_size=50)        
btn7.bind(on_press=print7)
#btn7g =  Button(text='Print FIRST(R) Logo [1]', background_color=blue, font_size=50)        
#btn7g.bind(on_press=print7g)
btn8 =  Button(text='More Prints', background_color=green, font_size=50)
btn8.bind(on_press=GVrun)
MENUlayout.add_widget(btn8)
MENUlayout.add_widget(btn3)
#MENUlayout.add_widget(btn6)
MENUlayout.add_widget(btn7)
#MENUlayout.add_widget(btn7g)



btn10 =  Button(text='Back', background_color=green, font_size=50)
btn10.bind(on_press=exit)
GVlayout.add_widget(btn10)
btn8 =  Button(text='Settings Panel', background_color=purple, font_size=50)
btn8.bind(on_press=TTTrun)
GVlayout.add_widget(btn8)




btn9 =  Button(text='Back', background_color=green, font_size=50)
btn9.bind(on_press=exit)
TTTlayout.add_widget(btn9)

btn9 =  Button(text='Run DROPBEAR on EV3', background_color=blue, font_size=50)
btn9.bind(on_press=dropbear)
TTTlayout.add_widget(btn9)

#btn9 =  Button(text='NOT RECCOMENDED: Connect to SESHAN WIFI', background_color=red, font_size=20)
#btn9.bind(on_press=wifi)
#TTTlayout.add_widget(btn9)

btn9 =  Button(text='Start Hotspot', background_color=red, font_size=50)
btn9.bind(on_press=hotspot)
TTTlayout.add_widget(btn9)

btn9 =  Button(text='Shutdown', background_color=blue, font_size=50)
btn9.bind(on_press=shutdown)
TTTlayout.add_widget(btn9)

#btn7a =  Button(text='Print an Avengers (TM) [2]', background_color=red, font_size=50)        
#btn7a.bind(on_press=print7a)
#GVlayout.add_widget(btn7a)

#btn7b =  Button(text='Print a LEGO (R) Minifigure [1]', background_color=blue, font_size=50)        
#btn7b.bind(on_press=print7b)
#GVlayout.add_widget(btn7b)

#btn7c =  Button(text='Print a SuperMan (C) [2]', background_color=blue, font_size=50)        
#btn7c.bind(on_press=print7c)
#GVlayout.add_widget(btn7c)

btn7d =  Button(text='Print a PacMan Ghost [2]', background_color=red, font_size=50)        
btn7d.bind(on_press=print7d)
GVlayout.add_widget(btn7d)

btn7e =  Button(text='Print a R2D2 (TM) [2]', background_color=blue, font_size=50)        
btn7e.bind(on_press=print7e)
GVlayout.add_widget(btn7e)

#btn7f =  Button(text='Print a MAKER FAIRE(TM) robot [2]', background_color=red, font_size=50)        
#btn7f.bind(on_press=print7f)
#GVlayout.add_widget(btn7f)


#MENUlayout.add_widget(btn)
#MENUlayout.add_widget(btn2)
#MENUlayout.add_widget(btn4)
#MENUlayout.add_widget(btn5)








# Declare both screens
class MenuScreen(Screen):
    pass

class TicTacToeScreen(Screen):
    pass

class DRJAVI3RScreen(Screen):
    pass

class GVScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sc1 = MenuScreen(name='menu')
sc2 = TicTacToeScreen(name='TicTacToe')
sc3 = DRJAVI3RScreen(name='DRJAVI3R')
sc4 = GVScreen(name='GV')

sc1.add_widget(MENUlayout)
sc2.add_widget(TTTlayout)
#sc3.add_widget(DRlayout)
sc4.add_widget(GVlayout)
sm.add_widget(sc1)
sm.add_widget(sc2)
#sm.add_widget(sc3)
sm.add_widget(sc4)




"""

MENUlayout = BoxLayout(orientation='vertical')
# use a (r, g, b, a) tuple
btn =  Button(text='Play TicTacToe', background_color=blue, font_size=50)
btn.bind(on_press=TTTrun)
btn3 =  Button(text='Ask Dr. JAVI3R', background_color=blue, font_size=50)
btn3.bind(on_press=DRrun)
MENUlayout.add_widget(btn)
MENUlayout.add_widget(btn3)

# Declare both screens
class MenuScreen(Screen):
    pass

class TicTacToeScreen(Screen):
    pass

class DRJAVI3RScreen(Screen):
    pass

class GVScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sc1 = MenuScreen(name='menu')
sc2 = TicTacToeScreen(name='TicTacToe')
sc3 = DRJAVI3RScreen(name='DRJAVI3R')
sc4 = GVScreen(name='GV')

sc1.add_widget(MENUlayout)
sc2.add_widget(TTTlayout)
sc3.add_widget(DRlayout)
sm.add_widget(sc1)
sm.add_widget(sc2)
sm.add_widget(sc3)
sm.add_widget(sc4)


"""


class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    
    TestApp().run()
