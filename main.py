#Kivy Calc w/o kv file

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
 
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
#set app size
#Window.size = (500, 700)

Builder.load_string("""
                    
<MyLayout>
	BoxLayout:
		orientation:"vertical"
		size:root.width, root.height
		
		TextInput:
			id:calc_input
			text:"0"
			halign:"right"
			font_size:65
			size_hint:(1, 0.15)
			
		GridLayout:
			cols:4
			rows:5	
			#Row
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "%"
				on_press:root.add_symbol("%")
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "<-"
				on_press:root.go_back()
			Button:
				id: calc_clear
				size_hint:(.2, .2)
				font_size:32
				text: "C"
				on_press: root.clear()
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "/"
				on_press:root.add_symbol("/")
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "7"
				on_press: root.button_press(7)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "8"
				on_press: root.button_press(8)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "9"
				on_press: root.button_press(9)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "X"
				on_press:root.add_symbol("*")
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "4"
				on_press: root.button_press(4)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "5"
				on_press: root.button_press(5)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "6"
				on_press: root.button_press(6)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "-"
				on_press:root.add_symbol("-")
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "1"
				on_press: root.button_press(1)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "2"
				on_press: root.button_press(2)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "3"
				on_press: root.button_press(3)
			Button:
				size_hint: (.2, .2)
				font_size:32
				text: "+"
				on_press:root.add_symbol("+")
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "+/-"
				on_press:root.posneg()
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "0"
				on_press: root.button_press(3)
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "."
				on_press:root.add_symbol(".")
			Button:
				size_hint:(.2, .2)
				font_size:32
				text: "="
				on_press:root.evaluate()
			
			
""")

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"
    
    def button_press(self, num):
        prior = self.ids.calc_input.text
        if prior == 'Error':
            self.ids.calc_input.text = f'{num}'
        elif prior == '0':
            self.ids.calc_input.text = f'{num}'
        else:
            self.ids.calc_input.text = f'{prior}{num}'
            
    def add_symbol(self, sym):
        oper = set("*/-+%")
        prior = self.ids.calc_input.text
        
        if prior[-1] in oper:
            if sym == prior[-1]:
                return
            else:
                self.ids.calc_input.text = f'{prior[:-1]}{sym}'
                return
        if sym == ".":
            if prior[-1].isnumeric():
                
                temp = prior.replace('+',',').replace('-',',').replace('*',',').replace('%',',').replace('/',',').split(',')
                
                last_num = temp[-1]
                
                if sym not in last_num:
                    self.ids.calc_input.text = f'{prior}{sym}'
            else:
                pass
        else:
            self.ids.calc_input.text = f'{prior}{sym}'
        
    def evaluate(self):
        equation = self.ids.calc_input.text
        try:
            code = compile(equation, "<string>", "eval")
            result = float(eval(code))
            self.ids.calc_input.text = f'{result}'
        except:
            self.ids.calc_input.text = 'Error'
        
        
    def posneg(self):
        prior = self.ids.calc_input.text
        num = float(prior)
        num *= -1
        self.ids.calc_input.text = f'{num}'
        
    def go_back(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]
        
class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    CalculatorApp().run()
    