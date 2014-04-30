import re
import nltk
from nltk.tokenize import RegexpTokenizer
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    FloatLayout:

        Label: 
            text: ' AUTOMATIC QUESTIION PAPER GENERATION'
            pos: 250, 300
            size_hint: 0.4, 0.3
        Button:
            pos: 10, 150
            size_hint: 0.2, 0.1
            text: 'SOFTWARE TESTING '
            on_press: root.manager.current = 'settings'
        
        Button:
            pos: 200, 150
            size_hint: 0.2, 0.1
            text: 'MEIPR'
            on_press: root.manager.current = 'settings1'
        Button:
            pos: 400, 150
            size_hint: 0.2, 0.1
            text: 'DESIGN'
            on_press: root.manager.current = 'settings2'
        Button:
            pos: 600, 150
            size_hint: 0.23, 0.1
            text: 'SOFTWARE ENGINEERING'
            on_press: root.manager.current = 'settings3'
       
<SettingsScreen>:
    FloatLayout:
        Label:
            pos:350, 500
            size_hint:0.1, 0.1
            text: 'SOFTWARE TESTING'
        Button:
            pos:300, 400
            size_hint: 0.22, 0.1 
            text: 'generate question paper'
	    on_press:	
        Label:
            pos:100, 300
            size_hint:0.1, 0.1
            text: 'ENTER QUESTION HERE :'
        Button:
            pos:350, 150
            size_hint: 0.1, 0.1 
            text: 'submit'
            on_press: with open("abc.txt", "a") as myfile: myfile.write(a1.text)
        TextInput:
            id: a1
            text: ''
            pos: 300, 300
            size_hint: 0.23, 0.1
       
            
<SettingsScreen1>:
    FloatLayout:
        Label:
            pos:350, 500
            size_hint:0.1, 0.1
            text: 'MEIPR'
        Button:
            pos:300, 400
            size_hint: 0.22, 0.1 
            text: 'generate question paper'
        Label:
            pos:100, 300
            size_hint:0.1, 0.1
            text: 'ENTER QUESTION HERE :'
        Button:
            pos:350, 150
            size_hint: 0.1, 0.1 
            text: 'submit'
            on_press: root.manager.current = 'menu'
        TextInput:
            text: ''
            pos: 300, 300
            size_hint: 0.23, 0.1
            
<SettingsScreen2>:
    FloatLayout:
        Label:
            pos:350, 500
            size_hint:0.1, 0.1
            text: 'DESIGN'
        Button:
            pos:300, 400
            size_hint: 0.22, 0.1 
            text: 'generate question paper'
        Label:
            pos:100, 300
            size_hint:0.1, 0.1
            text: 'ENETER QUESTION HERE :'
        Button:
            pos:350, 150
            size_hint: 0.1, 0.1 
            text: 'submit'
            on_press: root.manager.current = 'menu'
        TextInput:
            text: ''
            pos: 300, 300
            size_hint: 0.23, 0.1
            
<SettingsScreen3>:
    FloatLayout:
        Label:
            pos:350, 500
            size_hint:0.1, 0.1
            text: 'SOFTWARE ENGINEERING'
        Button:
            pos:300, 400
            size_hint: 0.22, 0.1 
            text: 'generate question paper'
        Label:
            pos:100, 300
            size_hint:0.1, 0.1
            text: 'ENETER QUESTION HERE :'
        Button:
            pos:350, 150
            size_hint: 0.1, 0.1 
            text: 'submit'
            on_press: root.manager.current = 'menu'
        TextInput:
            text: ''
            pos: 300, 300
            size_hint: 0.2, 0.1
            
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class SettingsScreen1(Screen):
    pass

class SettingsScreen2(Screen):
    pass

class SettingsScreen3(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(SettingsScreen1(name='settings1'))
sm.add_widget(SettingsScreen2(name='settings2'))
sm.add_widget(SettingsScreen3(name='settings3'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
