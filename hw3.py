import data

#part 1
def population_total(county_list):
    total_population = 0
    for county in county_list:
        total_population += county.population.get('2014 Population', 0)
    return total_population
