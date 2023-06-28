from rubicon.objc import objc_method, UIApplication, NSLog
from toga import App, Window, Label, Button, TextInput

class KellyCriterionApp(App):
    def startup(self):
        # Create main window
        main_box = Box()
        self.main_window = Window(title="Kelly Criterion", size=(400, 300))
        self.main_window.content = main_box

        # Step 1: Ask user for available capital
        capital_input = TextInput(placeholder="How much money do you have?")
        main_box.add(capital_input)

        # Step 2: Ask user for win information
        win_chance_input = TextInput(placeholder="What is the chance of winning (in %)?")
        main_box.add(win_chance_input)

        win_gain_input = TextInput(placeholder="What percentage of gain can you potentially make (in %)?")
        main_box.add(win_gain_input)

        # Step 3: Ask user for loss information
        loss_chance_input = TextInput(placeholder="What is the chance of losing (in %)?")
        main_box.add(loss_chance_input)

        loss_amount_input = TextInput(placeholder="What percentage of loss can you potentially face (in %)?")
        main_box.add(loss_amount_input)

        # Calculate button
        calculate_button = Button("Calculate", on_press=self.calculate)
        main_box.add(calculate_button)

        # Step 4: Calculate Kelly Criterion
        self.kelly_fraction_label = Label("")
        main_box.add(self.kelly_fraction_label)

        # Step 5: Calculate position size
        self.position_size_label = Label("")
        main_box.add(self.position_size_label)

        # Show the main window
        self.main_window.show()

    def calculate(self, widget):
        capital = float(capital_input.value)
        win_chance = float(win_chance_input.value) / 100
        win_gain = float(win_gain_input.value) / 100
        loss_chance = float(loss_chance_input.value) / 100
        loss_amount = float(loss_amount_input.value) / 100

        kelly_fraction = (win_chance * win_gain - loss_chance * loss_amount) / (win_gain - loss_amount)

        self.kelly_fraction_label.text = "Your Kelly Criterion is = " + str(kelly_fraction)
        position_size = capital * kelly_fraction
        self.position_size_label.text = "Recommended position size: " + str(position_size) + " ($ or PLN)"

if __name__ == '__main__':
    KellyCriterionApp().main_loop()
