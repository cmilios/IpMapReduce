#!/usr/bin/env python3
import sys
# input comes from STDIN (standard input)
list = []

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    columns = line.split(',')
    columns = columns[0:2]
    ip = columns[0]
    date = columns[1]
    time = columns[2][:-3]
    x = {'Key': ip, "Value": {'Date': date, 'Time': time}}
    for y in list:
        if(y['Key'] == x['Key']):
            if(y['Value']['Date'] == x['Value']['Date']):
                if(y["Value"]["Time"] == x['Value']['Time']):
                    pass
                else:
                    list.append(x)
                    print(ip, 1)
            else:
                list.append(x)
                print(ip, 1)
        else:
            list.append(x)
            print(ip, 1)

    

