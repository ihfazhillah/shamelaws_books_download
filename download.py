import csv
import wget
import os

from parser import find_bok_link

def download_all_books(csv_file):
    with open(csv_file, 'r') as f:
        csvreader = csv.DictReader(f, delimiter=',')

    # mkdir sesuai nama file
        filename = os.path.split(csv_file)[-1]
        try:
            filedir = os.path.splitext(filename)[0]
            os.mkdir(filedir)
        except:
            pass

        for row in csvreader:
            print(row)
            link = find_bok_link(row['url'])
            print('downloading %s' %(row['3nwan']))
            wget.download(link, out=filedir)
try:
    download_all_books('mustawda.csv')
    download_all_books('jadied.csv')
    download_all_books('shamela_khosh.csv')
except IndexError:
    pass
