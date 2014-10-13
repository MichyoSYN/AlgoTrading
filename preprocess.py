__author__ = 'Michyo'

'''
For this .py to run, you must name one folder as 'data_folder'
put all .csv related to 'current_product' in a sub-folder in it named as 'current_product'
'''

import csv
import os

# Global parameters.
separate_symbol = os.sep
data_folder = "data"
current_product = "HSIH4"

# Process for one file in a data sub-folder.
def process_raw_data(file_name, uni_count, product_code, write_in_file):
    count = 0 # test print
    with open(write_in_file, "ab+") as f:
        writer = csv.writer(f)
        for line in open(file_name):
            data_line = line.split(",")
            if data_line[1] == product_code and data_line[2] != "999999":
                writer.writerow(data_line)
                count += 1
        writer.writerow([current_product, uni_count, count])
    print("file = " + file_name + ", count = " + str(count)) # test print
    f.close()

# Clean up file content.
def clean_file(file_name):
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerow("")

# Process for whole files in one folder.
def process_folder(product_code):
    uni_count = 0
    folder = data_folder + separate_symbol + product_code
    print("folder = " + folder) # test print
    for f in os.listdir(folder):
        file_name = os.path.join(folder, f)
        file_full_text = os.path.splitext(file_name)
        if file_full_text[1] == ".csv":
            print("filename = " + file_name) # test
            process_raw_data(file_name, uni_count, product_code, "processed_data.csv")
            process_raw_data(file_name, uni_count, product_code, "processed_data_" + current_product + ".csv")
            uni_count += 1

print("Processing " + current_product) # test print
# clean_file("processed_data.csv")
# clean_file("processed_data_" + current_product + ".csv")
# process_folder(current_product)