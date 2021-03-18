# Prints total number of paths discovered after each hour
import csv

with open('plot_data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    hour = 0
    count = 1
    fname = "plot_data"
    total_lines = 0
    line_value = 0
    with open(fname, 'r') as f:
        for line in f:
            total_lines += 1   
    line_value = total_lines//24.
    for row in csv_reader:
        if line_count == 0:            
            line_count += 1
        else:
            count += 1
            if (count % line_value == 0):                            
                print(f'\t{hour}, {row[3]}')
                hour += 1            
            line_count += 1    
