from mrjob.job import MRJob
import sys



class Count(MRJob):
    def mapper(self, key, line):
        
        line = line.strip()
        columns = line.split(',')
        ip = columns[0]
        date = columns[1]
        time = columns[2][:-3]
        v = date+','+time
        if(line[0] != 'i'):
            yield(ip, v)
        
            
    def reducer(self, ips, datetimes):
        lista = set()
        for i in datetimes:
            lista.add(i)
        yield(ips, len(lista))


       
if __name__ == '__main__':
    Count.run()