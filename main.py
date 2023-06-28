from toga import App, Box, Button, Label, TextInput
import toga

class KellyCriterionApp(App):
    def startup(self):
        # Step 1: Ask user for available capital
        capital_input = TextInput(placeholder="How much money do you have?")
        win_chance_input = TextInput(placeholder="What is the chance of winning (in %)?")
        win_gain_input = TextInput(placeholder="What percentage of gain can you potentially make (in %)?")
        loss_chance_input = TextInput(placeholder="What is the chance of losing (in %)?")
        loss_amount_input = TextInput(placeholder="What percentage of loss can you potentially face (in %)?")

        # Step 4: Calculate Kelly Criterion
        kelly_fraction_label = Label("Your Kelly Criterion is = ")
        self.position_size_label = Label("")

        # Calculate button
        calculate_button = Button("Calculate", on_press=self.calculate)

        # Create main box layout
        main_box = Box(
            children=[
                capital_input,
                win_chance_input,
                win_gain_input,
                loss_chance_input,
                loss_amount_input,
                calculate_button,
                kelly_fraction_label,
                self.position_size_label
            ],
            style=Pack(direction="column")
        )

        # Create main window
        self.main_window = toga.MainWindow(title="Kelly Criterion", size=(400, 300))
        self.main_window.content = main_box
        self.main_window.show()

    def calculate(self, widget):
        capital = float(self.main_window.children[0].children[0].value)
        win_chance = float(self.main_window.children[0].children[1].value) / 100
        win_gain = float(self.main_window.children[0].children[2].value) / 100
        loss_chance = float(self.main_window.children[0].children[3].value) / 100
        loss_amount = float(self.main_window.children[0].children[4].value) / 100

        kelly_fraction = (win_chance * win_gain - loss_chance * loss_amount) / (win_gain - loss_amount)
        self.main_window.children[0].children[5].text = "Your Kelly Criterion is = " + str(kelly_fraction)
        position_size = capital * kelly_fraction
        self.position_size_label.text = "Recommended position size: " + str(position_size) + " ($ or PLN)"

if __name__ == '__main__':
    KellyCriterionApp().main_loop()

