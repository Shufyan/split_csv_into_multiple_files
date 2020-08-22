# import required libraries
import os

# A generic function to split the input .csv file into multiple output .csv files
"""
You can pass some other parameters while calling the function for e.g.:
    filehandler = open('test.csv', 'r')              ---- the filehandler parameter
    delimiter = ','                                  ---- the delimiter to be used
    row_limit = '100'                                ---- the row limit for splitting the files
    output_name_template = 'output_%s.csv'           ---- the output file name '%s' will be replaced by 1,2,3
    output_path = 'E:/ABC/XYZ/'                      ---- for same folder pass '.'
    keep_headers = True/False                        ---- if you want to keep the header in each file or not 
"""
def split_csv(filehandler, delimiter=',', row_limit=10000,
          output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    import csv
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:            
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)

# Calling the split_csv() function, you may call the similar way from external script
if __name__ == '__main__':
    split_csv(open('test.csv', 'r'));