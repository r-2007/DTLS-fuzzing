import csv

with open('s0_2_plot_data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    hour = 0
    count = 1
    for row in csv_reader:
        if line_count == 0:            
            line_count += 1
        else:
            count += 1
            if (count % 435 == 0):                            
                print(f'\t{hour}, {row[7]}')
                hour += 1            
            line_count += 1  