import string
import re


def find_obrez():

    lookup = 'Подписывая экспедиторскую расписку'
    a = 0
    with open("GeoBase_test.svg", encoding="utf8") as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup  in line:
                print(line)
                return 0



if __name__ == "__main__":
    find_obrez()