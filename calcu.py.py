import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# set size of calculator app
Window.size = (400, 600)

# file python will be reading from
Builder.load_file('design.kv')

class MyLayout(Widget):
    def clear(self):
        """
        clear input box and display "0" when "C" is pressed
        :return: None
        """
        self.ids.calcu_input.text = "0"

    def pressed_number(self, button):
        """
        displays the pressed button on to the input screen
        :param button:
        :return: None
        """
        previous_input = self.ids.calcu_input.text
        if "Invalid" in previous_input:
            previous_input = ""
        # if number in input box is '0' it replaces it with the pressed button's value
        if previous_input == "0":
            self.ids.calcu_input.text = ""
            self.ids.calcu_input.text = f'{button}'
        # if input box is not '0' it appends the new input to existing input
        else:
            self.ids.calcu_input.text = ''
            self.ids.calcu_input.text = f'{previous_input}{button}'

    def operation_sign(self):
        """
        returns the operation sign in the input box
        :return: "+", "-", "x", or "/"
        """
        if "+" in self.ids.calcu_input.text:
            return "+"
        elif "-" in self.ids.calcu_input.text:
            return "-"
        elif "x" in self.ids.calcu_input.text:
            return "x"
        elif "/" in self.ids.calcu_input.text:
            return "/"

    def decimal_sign(self):
        """

        :return: None
        """
        previous_input = self.ids.calcu_input.text
        # splits the input on the operating sign returned by operation_sign method
        num_list = previous_input.split(self.operation_sign())

        # adds a "." to input if one is not present already after operating sign(second number)
        if "+" in previous_input or "-" in previous_input or "x" in previous_input or "/" in previous_input:
            if "." not in num_list[-1]:
                updated_input = f'{previous_input}.'
                self.ids.calcu_input.text = updated_input
        elif "." in previous_input:
            pass
        # adds a "." if one is not present already
        else:
            updated_input = f'{previous_input}.'
            self.ids.calcu_input.text = updated_input

    def delete_input(self):
        """
        take off last item in input screen

        :return: None
        """
        previous_input = self.ids.calcu_input.text
        # updates input to not include last item
        updated_input = previous_input[:-1]
        # displays updated input number
        self.ids.calcu_input.text = updated_input

    def make_positive_or_negative(self):
        """
        adds a "-" to an input value if it doesn't have one already(to make negative)
        :return: None
        """
        previous_input = self.ids.calcu_input.text
        # if "-" change to positive
        if "-" in previous_input:
            updated_input = previous_input.replace("-", "")
            self.ids.calcu_input.text = f'{updated_input}'
        # if positive add "-"
        else:
            self.ids.calcu_input.text = f'-{previous_input}'


    def arithmetic(self, operation):
        """
        displays pressed arithmetic operation((+,-,*,%)) to input screen
        :param operation:
        :return: None
        """
        previous_number = self.ids.calcu_input.text
        input_list = list(previous_number)
        # can't have two operating signs back to back
        if input_list[-1] == "+" or input_list[-1] == "-" or input_list[-1] == "x" or input_list[-1] == "/":
            pass
        elif "+" in previous_number or "-" in previous_number or "x" in previous_number or "/" in previous_number:
            pass
        # adds operating sign pressed to input
        else:
            self.ids.calcu_input.text = f'{previous_number}{operation}'

    def equals(self):
        """
        computes values for inputs entered
        :return: None
        """
        # get previous input from input box
        previous_input = self.ids.calcu_input.text
        # if operating sign is "+", add input values
        if "+" in previous_input:
            # split inputs on "+" sign and make a list
            add_list = previous_input.split("+")

            total = float(0)
            for number in add_list:
                total += float(number)
            # display value as a string
            self.ids.calcu_input.text = str(total)
        # if operating sign is "-", subtract input values
        elif "-" in previous_input:
            sub_list = previous_input.split("-")
            total = float(sub_list[0])
            for number in sub_list[1:]:
                total -= float(number)
            # display total value as a string
            self.ids.calcu_input.text = str(total)
        # if operating sign is "x", add input values
        elif "x" in previous_input:
            multiply_list = previous_input.split("x")
            total = float(multiply_list[0])
            for number in multiply_list[1:]:
                total *= float(number)
            # return total value as a string
            self.ids.calcu_input.text = str(total)
        # if operating sign is "/", add input values
        elif "/" in previous_input:
            divide_list = previous_input.split("/")
            total = float(divide_list[0])

            try:
                # check if inputed values are divisible
                for number in divide_list[1:]:
                    total /= float(number)
                answer = round(total, 7)
                self.ids.calcu_input.text = str(answer)
            except:
                # if not divisible catch error and print invalid on input screen
                self.ids.calcu_input.text = "Invalid"
        # if operating sign is "%", find percentage of input values
        elif "%" in previous_input:
            percent_list = previous_input.split("%")
            first_number = float(percent_list[0])
            total = first_number * 100
            percentage = total / float(percent_list[1])
            # display result with a percentage sign
            self.ids.calcu_input.text = f'{str(percentage)}%'

class CalculatorApp(App):
    """
    main class to use/import kivy properties
    calls the MyLayout class for use
    """
    def build(self):
        return MyLayout()

if __name__=="__main__":
    CalculatorApp().run()

