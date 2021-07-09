import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGridLayout(Widget):
    # init infinite keywords
    

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f"Hello {name}, you like {pizza}, and your favorite color is {color}!")
        # print it to the screen
        self.add_widget(Label(text=f"Hello {name}, you like {pizza}, and your favorite color is {color}!"))

        #clear the input boxes
        self.name.text=""
        self.pizza.text=""
        self.color.text=""


class gui2(App):
    def build(self):
        #return Label(text="Hello World")
        return MyGridLayout()

if __name__ == '__main__':
    gui2.run()
