def kelly_criterion():
    # Step 1: Ask user for available capital
    capital = float(input("How much money do you have? "))

    # Step 2: Ask user for win information
    win_chance = float(input("What is the chance of winning (in %)? ")) / 100
    win_gain = float(input("What percentage of gain can you potentially make (in %)? ")) / 100

    # Step 3: Ask user for loss information
    loss_chance = float(input("What is the chance of losing (in %)? ")) / 100
    loss_amount = float(input("What percentage of loss can you potentially face (in %)? ")) / 100


    # Step 4: Calculate Kelly Criterion
    kelly_fraction = (win_chance * win_gain - loss_chance * loss_amount) / (win_gain - loss_amount)


    # Step 5: Calculate position size
    position_size = capital * kelly_fraction
    print("                                               ")
    print("Your Kelly Criterion is = "+ str(kelly_fraction))
    print("                                               ")

    # Step 6: Return the recommended position size
    return position_size

# Example usage
recommended_size = kelly_criterion()
print("Recommended position size: "+ str(recommended_size) + " ($ or PLN)")


