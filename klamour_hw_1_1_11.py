# -*- coding: utf-8 -*-
"""
Katherine Lamoureux
MET CS 521
9/8/2019
Homework 1.5
Description: Program to display the population for the next five years
"""

# This section holds variables
seconds_per_day = 60 * 60 * 24
days_per_year = 365
population = 312032486

# This section computes birth per year
birth = ( 1 / 7 ) * seconds_per_day * days_per_year

# This section computes death per year
death = ( -1 / 13 ) * seconds_per_day * days_per_year

# This section computes immigrant per year
immigrant = ( 1 / 45 ) * seconds_per_day * days_per_year

# This section displays the results of the next five years
print( 'The current population is', population)
print( 'The population will increase over the next five years as such:' )
print( 'Year 1: ', round(population + birth + death + immigrant) )
print( 'Year 2: ', round(population + birth*2 + death*2 + immigrant*2) )
print( 'Year 3: ', round(population + birth*3 + death*3 + immigrant*3) )
print( 'Year 4: ', round(population + birth*4 + death*4 + immigrant*4) )
print( 'Year 5: ', round(population + birth*5 + death*5 + immigrant*5) )