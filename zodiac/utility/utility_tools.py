import csv


def update_csv(filename, data_list, csv_columns):
    try:
        with open(filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for dic in data_list:
                writer.writerow(dic)
            csvfile.close()
    except IOError:
        print("I/O error")
    finally:
        if csvfile is not None:
            csvfile.close()
        if len(data_list) > 0:
            data_list.clear()
