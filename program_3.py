# Program #3: US_Population

def sum_population_for_year(all_entered_values, year_to_sum):
    return  sum(all_entered_values[2] for all_entered_values in all_entered_values if all_entered_values[0] == year_to_sum)
    

def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    rows = int(input('How many states are you using data from? '))

    for r in range(rows):
        year = int(input('what year '))
        state = str(input('what state '))
        pop = int(input('states population '))
        cols = [year,state,pop]
        all_entered_values.append(cols)
    print(all_entered_values)
    # Now have the user enter a year.
    year_to_sum = int(input('What year do you want added together? '))
    print(sum_population_for_year(all_entered_values,year_to_sum))



    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year


#def sum_population_for_year(all_entered_values, year_to_sum):
 #   total_population = sum(all_entered_values[2] for all_entered_values in data if all_entered_values[0] == year_to_sum)

# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they enterd 2011 for the year to sum.

# print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
