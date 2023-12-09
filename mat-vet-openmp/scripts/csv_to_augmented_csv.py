#!/usr/bin/env python3

import csv
import sys

if len(sys.argv) != 3:
    print("Usage: python csv_to_augmented_csv.py <input_csv_path> <output_csv_path>")
    sys.exit(1)

input_csv = sys.argv[1]
output_csv = sys.argv[2]

# Read the input CSV and create the output CSV
with open(input_csv, 'r') as csvfile, open(output_csv, 'w', newline='') as outputfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outputfile)
    
    # Read the rows and calculate and add the values for "speed_up," "efficiency," and "total_overhead"
    max_time_0 = None
    for row in reader:
        nthreads = int(row[0])
        time = float(row[1])

        if max_time_0 is None:
            max_time_0 = time

        speed_up = max_time_0 / (time if time != 0 else 1)
        efficiency = speed_up / nthreads
        total_overhead = nthreads * time - max_time_0

        row += [speed_up, efficiency, total_overhead]
        writer.writerow(row)

print(f"Modified CSV has been saved to {output_csv}")
