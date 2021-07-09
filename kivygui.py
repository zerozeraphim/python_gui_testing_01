import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # init infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 2
        
        # create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(text="Name: "))

        # add input box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        # add widgets
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))

        # add input box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        # add widgets
        self.top_grid.add_widget(Label(text="Favorite Color: "))

        # add input box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)
        

        # create submit button
        self.submit = Button(text="Submit", font_size = 32 )
        # bind the button
        self.submit.bind(on_press=self.press)
        self.top_grid.add_widget(self.submit)

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


class MyApp(App):
    def build(self):
        #return Label(text="Hello World")
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
