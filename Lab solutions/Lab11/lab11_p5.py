# Pollution/Cancer Correlation Program

import math

def openFiles():
    '''
        Prompts the user for the file names to open, opens the files,
        and returns the file objects for each in a tuple of the form
        (pollution_datafile, cancer_datafile).

        Raises an OSError exception if the files are not successfully
        opened after four attempts of entering file names.
    '''

    # init
    pollution_datafile_opened = False
    cancer_datafile_opened = False
    num_attempts = 4
    
    # prompt for file names and attempt to open files
    while ((not pollution_datafile_opened) or \
           (not cancer_datafile_opened)) \
            and (num_attempts > 0):
        try:
            if not cancer_datafile_opened:
                file_name = input('Enter lung cancer data from filename: ')
                cancer_datafile = open(file_name, 'r')
                cancer_datafile_opened = True

            if not pollution_datafile_opened:
                file_name = input('Enter air pollution data from filename: ')
                pollution_datafile = open(file_name, 'r')
                pollution_datafile_opened = True
            
        except OSError:
            print('File not found:',file_name + '.','Please reenter\n')
            num_attempts = num_attempts - 1

    # if one or more files not opened, raise OSError exception
    if not pollution_datafile_opened or not cancer_datafile_opened:
        raise OSError('Too many attempts of reading input files')
    
    # return file objects if successfully opened
    else:
        return (pollution_datafile, cancer_datafile)


def readFiles(pollution_datafile, cancer_datafile):
    '''
        Reads the data from the provided file objects pollution_datafile
        and cancer_datafile. Returns a list of the data read from each
        in a tuple of the form (pollution_datafile, cancer_datafile).
    '''

    # init
    cancer_data = {}
    pollution_data = {}
    empty_str = ''

    # read past file headers
    pollution_datafile.readline()
    cancer_datafile.readline()

    for data in cancer_datafile:
        tmp_list = data.lower().strip().split(',')
        cancer_data[tmp_list[0]] = tmp_list[1]

    for data in pollution_datafile:
        tmp_list = data.lower().strip().split(',')
        if tmp_list[0] in cancer_data:
            pollution_data[tmp_list[0]] = tmp_list[1]

    # return list of data from each file
    return (pollution_data, cancer_data)

    # # init
    # pollution_data = []
    # cancer_data = []
    # empty_str = ''
    #
    # # read data files
    # eof = False
    #
    # while not eof:
    #
    #     # read line of data from each file
    #     s_line = pollution_datafile.readline()
    #     c_line = cancer_datafile.readline()
    #
    #     # check if at end-of-file of both files
    #     if s_line == empty_str and c_line == empty_str:
    #         eof = True
    #
    #     # check if end of pollution data file only
    #     elif s_line == empty_str:
    #         raise OSError('Unexpected end-of-file for pollution data file')
    #
    #     # check if at end of cancer data file only
    #     elif c_line == empty_str:
    #         raise OSError('Unexpected end-of-file for cancer data file')
    #
    #     # append line of data to each list
    #     else:
    #         pollution_data.append(s_line.strip().split(','))
    #         cancer_data.append(c_line.strip().split(','))
    #
    # # return list of data from each file
    # return (pollution_data, cancer_data)
        

def calculateCorrelation(pollution_data, cancer_data):
    '''
        Calculates and returns the correlation value for the data
        provided in lists pollution_data and cancer_data
    '''    

    # init
    sum_pollution_vals = sum_cancer_vals = 0
    sum_pollution_sqrd = sum_cancer_sqrd = 0
    sum_products = 0

    # calculate intermediate correlation values
    num_values = len(pollution_data)

    for key in pollution_data:
        sum_cancer_vals = sum_cancer_vals + float(cancer_data[key])
        sum_pollution_vals = sum_pollution_vals + float(pollution_data[key])

        sum_pollution_sqrd = sum_pollution_sqrd +  \
                              float(pollution_data[key]) ** 2
        sum_cancer_sqrd = sum_cancer_sqrd +  \
                              float(cancer_data[key]) ** 2

        sum_products = sum_products + float(pollution_data[key]) *  \
                       float(cancer_data[key])

    # calculate and display correlation value
    numer = (num_values * sum_products) - \
            (sum_pollution_vals * sum_cancer_vals)

    denom = math.sqrt(abs( \
        ((num_values * sum_pollution_sqrd) - (sum_pollution_vals ** 2)) * \
        ((num_values * sum_cancer_sqrd) - (sum_cancer_vals ** 2)) \
        ))

    return numer / denom

    # # calculate intermediate correlation values
    # num_values = len(pollution_data)
    #
    # for k in range(0,num_values):
    #
    #     sum_pollution_vals = sum_pollution_vals + float(pollution_data[k][1])
    #     sum_cancer_vals = sum_cancer_vals + float(cancer_data[k][1])
    #
    #     sum_pollution_sqrd = sum_pollution_sqrd +  \
    #                           float(pollution_data[k][1]) ** 2
    #     sum_cancer_sqrd = sum_cancer_sqrd +  \
    #                           float(cancer_data[k][1]) ** 2
    #
    #     sum_products = sum_products + float(pollution_data[k][1]) *  \
    #                    float(cancer_data[k][1])
    #
    # # calculate and display correlation value
    # numer = (num_values * sum_products) - \
    #         (sum_pollution_vals * sum_cancer_vals)
    #
    # denom = math.sqrt(abs( \
    #     ((num_values * sum_pollution_sqrd) - (sum_pollution_vals ** 2)) * \
    #     ((num_values * sum_cancer_sqrd) - (sum_cancer_vals ** 2)) \
    #     ))
    #
    # return numer / denom


# ---- main

# program greeting
print ('This program will determine the correlation (-1 to 1) between')
print ('data on air pollution and incidences of lung cancer\n')

try:
    # open data files
    pollution_datafile, cancer_datafile = openFiles()
    # # Test code
    # cancer_datafile = 'lab11_p5 output test\\CDC_Lung_Cancer_Data.csv'
    # pollution_datafile = 'Air_Pollution_Data.csv'
    # pollution_datafile = 'lab11_p5 output test\\CDC_Cigarette_Smoking_Data.csv'

    # read data
    pollution_data, cancer_data = readFiles(pollution_datafile, cancer_datafile)

    # Intensive file closing
    pollution_datafile.close()
    cancer_datafile.close()

    # calculate correlation value
    correlation = calculateCorrelation(pollution_data, cancer_data)

    # display correlation value
    print ('r_value = ', correlation)

except OSError as e:
    print(e)
    print('Program terminated ...')

