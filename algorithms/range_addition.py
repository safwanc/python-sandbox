MAX_YEAR = 2018

def find_max_population(years_alive):
    max_population_year, max_population = 0, 0
    timeline = [0] * (MAX_YEAR + 1)

    for birth_year, death_year in years_alive:
        timeline[birth_year] += 1
        timeline[death_year] -= 1

    for year in range(1, MAX_YEAR + 1):
        timeline[year] += timeline[year - 1]
        if timeline[year] >= max_population:
            max_population, max_population_year = timeline[year], year
    
    return max_population_year

print(find_max_population([[1987, 2018], [1990, 2017]]))