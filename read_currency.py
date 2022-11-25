import csv

with open('currencyrates.csv','r') as currency_file:
    lines = csv.reader(currency_file)

    for line in lines:
        if 'Bangladeshi' in line[0]:
            print(line)