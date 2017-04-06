# your Python code to implement the features could be placed here
# note that you may use any language, there is no preference towards Python
import collections
import pandas as pd

#Feature 1                                                                      
#cat log.txt | awk '{print $1}' | sort -n| uniq -c | sort -nr | head -10 > hosts.txt

#Feature 2                                                                      
logfile = open("log.txt", "r")
clean_log=[]
#create list with url and size                                                  
for line in logfile:
    try:
        if (line[line.index("GET")+4:line.index("HTTP")]!='/ '):
            clean_log.append((line[line.index("GET")+4:line.index("HTTP")],line.split()[9]))
    except:
        pass

counter = collections.Counter(clean_log)
dict = {}

# use Counter to find most common url                                           
for count in counter.most_common():                        
    try:
        #dict key: url, value: frequency * size                                 
        dict.update({count[0]:(int(count[1])*int(count[0][1]),count[1])})
    except:
        pass
      
#sort by bandwidth                                                              
sortedList = sorted( ((v,k) for k,v in dict.iteritems()),reverse=True)                                                               

#write output of top 10 resources to file                                       
outputfile = open('resources.txt','w')
for k,v in sortedList[:10]:
    print(v[0])
    outputfile.write("%s\n" % v[0])
logfile.close()

