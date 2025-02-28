import data

#part 1
def population_total(county_list):
    total_population = 0
    for county in county_list:
        total_population += county.population.get('2014 Population', 0)
    return total_population

#part 2
def filter_by_state(county_list, state_abbreviation):
    # Create a new list to store counties that match the state abbreviation
    filtered_counties = []

    # Iterate through the county list
    for county in county_list:
        # If the county's state matches the state abbreviation, add it to the filtered list
        if county.state == state_abbreviation:
            filtered_counties.append(county)

    # Return the filtered list of counties
    return filtered_counties

#part 3
def population_by_education(county_list, education_key):
    total_population = 0
    for county in county_list:
        if education_key in county.education:
            education_percentage = county.education[education_key]
            total_population += (education_percentage / 100) * county.population['2014 Population']
    return total_population

def population_by_ethnicity(county_list, ethnicity_key):
    total_population = 0
    for county in county_list:
        if ethnicity_key in county.ethnicities:
            ethnicity_percentage = county.ethnicities[ethnicity_key]
            total_population += (ethnicity_percentage / 100) * county.population['2014 Population']
    return total_population

def population_below_poverty_level(county_list):
    total_population = 0
    for county in county_list:
        poverty_percentage = county.income['Persons Below Poverty Level']
        total_population += (poverty_percentage / 100) * county.population['2014 Population']
    return total_population

#part 4
def percent_by_education(county_list, education_key):
    total_population = population_total(county_list)
    if total_population == 0:
        return 0  # To avoid division by zero
    sub_population = population_by_education(county_list, education_key)
    return (sub_population / total_population) * 100

def percent_by_ethnicity(county_list, ethnicity_key):
    total_population = population_total(county_list)
    if total_population == 0:
        return 0  # To avoid division by zero
    sub_population = population_by_ethnicity(county_list, ethnicity_key)
    return (sub_population / total_population) * 100

def percent_below_poverty_level(county_list):
    total_population = population_total(county_list)
    if total_population == 0:
        return 0  # To avoid division by zero
    sub_population = population_below_poverty_level(county_list)
    return (sub_population / total_population) * 100

#part 5
def education_greater_than(county_list, education_key, threshold):
    return [
        county for county in county_list
        if county[education_key] > threshold
    ]

def education_less_than(county_list, education_key, threshold):
    return [
        county for county in county_list
        if county[education_key] < threshold
    ]

def ethnicity_greater_than(county_list, ethnicity_key, threshold):
    return [
        county for county in county_list
        if county[ethnicity_key] > threshold
    ]

def ethnicity_less_than(county_list, ethnicity_key, threshold):
    return [
        county for county in county_list
        if county[ethnicity_key] < threshold
    ]

def below_poverty_level_greater_than(county_list, threshold):
    return [
        county for county in county_list
        if county['Persons Below Poverty Level'] > threshold
    ]

def below_poverty_level_less_than(county_list, threshold):
    return [
        county for county in county_list
        if county['Persons Below Poverty Level'] < threshold
    ]
