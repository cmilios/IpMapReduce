from mrjob.job import MRJob
import sys



class Count(MRJob):
    def mapper(self, key, line):
        
        line = line.strip()
        
        columns = line.split(',')
        ip = columns[0]
        date = columns[1]
        time = columns[2][:-3]
        #val = {'date': date, 'time': time}

        v = date+','+time
        #ss = {'Key': ip, 'Value': val}
        if(line[0] != 'i'):
            yield(ip, v)
        
            
    def reducer(self, ips, datetimes):


        list = []
        val = ''
        for i in datetimes:
            date,time = i.split(',')
            val = {'Date': date, 'Time': time}
            if(len(list)==0):
                list.append(val)
            else:
                for dates in list:
                    if(dates['Date']!= val['Date']):
                        list.append(val)
                    else:
                        if(dates['Time']!= val['Time']):
                            list.append(val)

        ss = Remove(list)
        yield(ips, len(ss))
        list=[]


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
       
if __name__ == '__main__':
    Count.run()