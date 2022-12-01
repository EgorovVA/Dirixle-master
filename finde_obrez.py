import string
import re


def find_obrez():
    hight = 0
    width = 0
    lookup = '<rect'
    a = 0
    #line = ""
    with open("GeoBase_test.svg", encoding="utf8") as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup  in line:
                print(line)
                index = line.find("city")
                if line[index+25] != "\42":
                    #print(float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24]+line[index+25]))
                    hight = float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24]+line[index+25])
                    if line[index+53]!= "\42":
                        #print(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52] + line[index+53])
                        width = float(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52] + line[index+53])
                    else:
                        #print(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                        width = float(line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                else:
                   #print(float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24]))
                    hight = float(line[index+20]+line[index+21]+line[index+22]+line[index+23]+line[index+24])
                    if line[index+52] != "\42":
                       # print(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                        width = float(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51] + line[index+52])
                    else:
                       # print(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51])
                        width = float(line[index+47] + line[index+48] + line[index+49] + line[index+50] + line[index+51])
                return hight, width
                


if __name__ == "__main__":
    print(find_obrez())
    a = find_obrez()
    hight = a[0]
    width = a[1]