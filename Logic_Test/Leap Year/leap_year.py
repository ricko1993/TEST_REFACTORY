# Python code to finding number of
# leap years in list of years.

# Input list initialization
Input = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956,
        1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

# Find whether it is leap year or not


def checkYear(year):
    return (((year % 4 == 0) and
            (year % 100 != 0)) or
            (year % 400 == 0))


# Answer Initialization
Answer = 0

for elem in Input:
    if checkYear(elem):
        Answer = Answer + 1

# Printing
print("No of leap years are:", Answer)
