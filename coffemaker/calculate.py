def make_coffee(user_choice, ingredient):
    if user_choice == 'espresso':
        if ingredient['water'] >= 200 and ingredient['coffee'] >= 24:
            quarters_amount = float(input('How many quarters: '))
            dimes_amount = float(input('How many dimes: '))
            nickles_amount = float(input('How many nickles: '))
            pennies_amount = float(input('How many pennies: '))

            total_coin_amount = (quarters_amount * 0.25 ) + (dimes_amount * 0.10) + (nickles_amount * 0.05) + (pennies_amount * 0.01)

            if total_coin_amount >= espresso_cost:
                water_res -= 50
                coffee_res -= 18
                change_amount = total_coin_amount - espresso_cost
                profit += espresso_cost
                report['Water'] = water_res
                report['Milk'] = milk_res
                report['Coffee'] = coffee_res
                report['Money'] = profit

                if change_amount > 0:
                    print(f'Here is $ {change_amount} dollars in Change.')
                print(f'Here is your {user_prompt}, Enjoy')
        print(report)