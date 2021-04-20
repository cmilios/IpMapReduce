#!/usr/bin/env python3
from operator import itemgetter
import sys
current_ip = None
current_count = 0
ip = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    ip, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
        except ValueError: # count was not a number, so silently ignore/discard this line
        continue
        # this IF-switch only works because Hadoop sorts map output by key (here: word) before it is passed
        #to the reducer
        if current_ip == ip:
            current_count += count
        else:
            if current_ip: # write result to STDOUT
                print('%s\t%s' % (current_ip, current_count))
                current_count = count
                current_ip = ip
            # do not forget to output the last word if needed!
            if current_ip == ip:
                print('%s\t%s' % (current_ip, current_count))