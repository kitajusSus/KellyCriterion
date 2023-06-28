def kelly_criterion():
    # Step 1: Ask user for available capital
    capital = float(input("How much money do you have? "))

    # Step 2: Ask user for win information
    win_chance = float(input("What is the chance of winning (in %)? ")) / 100

    ####################################
    loss_chance = abs(1 - win_chance)
    print("Percentage  of losing chance " + str(loss_chance * 100) + "%")
    ###################################

    win_gain = float(input("What percentage of gain can you potentially make (in %)? ")) / 100 + 1

    loss_amount = float(input("What percentage of loss can you potentially face (in %)? ")) / 100

    fraction = win_gain/loss_amount

    # Step 4: Calculate Kelly Criterion
    kelly_fraction = win_chance - ((1-win_chance)/fraction)


    # Step 5: Calculate position size
    position_size = capital * kelly_fraction
    print("                                               ")
    print("Your Kelly Criterion is = "+ str(abs(kelly_fraction)))
    print("                                               ")

    # Step 6: Return the recommended position size
    return position_size

# Example usage
recommended_size = kelly_criterion()
print("Recommended position size: "+ str(recommended_size) + " ($ or PLN)")


# Prompt to prevent immediate exit
input("Press Enter to exit...")
