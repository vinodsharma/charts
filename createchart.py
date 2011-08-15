import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import deque
import sys

# site argument will be used in the title & also in the name of the chart
# chartdata must be a list in which each item is a tuple which
# contains 3 items: confname,num_worker_list,latencies_list
# ex: chartdata=[
#            (conf1,num_workers_list,conf1_latencies),
#            (conf2,num_workers_list,conf2_latencies), 
#            (conf3,num_workers_list,conf3_latencies)
#           ]
#   where conf1 = "1 Server, 10 container"
#   num_workers_list = [3,6,9,12,15,18,21]
#   conf1_latencies = [10,15,12,13,11,17,15]
#   Note: chartdata can create chart with atmost 8 configuration
#         as we have only 8 colour to distinguish between 
#         different configuration

def CreateConfChart(site,chartdata):
    colours= deque(['b','g','r','c','m','y','k','w'])
    # change the size of chart using figsize parameter
    fig1 =plt.figure(figsize=(10,5))
    plt.xlabel('number of workers')
    plt.ylabel('latency(s)')
    plt.title('latencies for ' + site)
    max_x = None
    max_y = None
    max_xn = None
    max_yn = None
    line_list = []
    confname_list = []

    for data in chartdata:
        confname, num_workers1,latencies= data;
        if len(colours) == 0:
            print >> sys.stderr, "not enough colour for seperation of line"
            return False
        max_x = max(num_workers1)
        max_y = max(latencies)
        max_xn = len(num_workers1)
        max_yn = len(latencies)
        fmt = colours.popleft()+'-o'
        line, = plt.plot(num_workers1,latencies, fmt)
        line_list.append(line)
        confname_list.append(confname)
    #set properites for legend
    fp =  matplotlib.font_manager.FontProperties(size='xx-small')
    plt.legend( tuple(line_list),tuple(confname_list), loc='best', prop=fp)
    #plt.legend( tuple(line_list),tuple(confname_list),bbox_to_anchor=(0., 1.02, 1., .102), ncol=2,loc=3,mode="expand", borderaxespad=0.)
    #plt.legend( tuple(line_list),tuple(confname_list), prop =fp, loc=3, bbox_to_anchor=(-0.2,0),borderaxespad=0.)
    #plt.xticks((np.arange(0,max_x+10-(max_x%10)+2*((max_x+10-(max_x%10))/max_xn),(max_x+10-(max_x%10))/max_xn)))
    #plt.yticks((np.arange(0,max_y+10-(max_y%10)+2*((max_y+10-(max_y%10))/max_yn),(max_y+10-(max_y%10))/max_yn)))
    plt.savefig(site, format='png') 
    plt.close()
    return True







#usage of CreateChart function
conf1_latencies = [10.53232323543,15,12,13,11,17,15]
conf2_latencies = [8.242342354,10,6,8,10,14,17]
conf3_latencies = [9,11,10,12,11,13,9]
conf4_latencies = [7,6,8,9,4,12,17]
conf5_latencies = [1,2,4,6,7,5,8]
conf6_latencies = [3,4,8,6,9,11,10]
conf7_latencies = [5,7,9,8,10,9,1]
conf1 = "1 Server, 10 container"
conf2 = "2 Server, 5 container"
conf3 = "3 Server, 10 container"
conf4 = "4 Server, 5 container"
conf5 = "5 Server, 10 container"
conf6 = "6 Server, 5 container"
conf7 = "7 Server, 10 container"
num_workers_list = [10,30,50,70,90,110,150]
conf_list=[]
t1 = (conf1,num_workers_list,conf1_latencies)
conf_list.append(t1)
t2 = (conf2,num_workers_list,conf2_latencies)
conf_list.append(t2)
CreateConfChart("www.google.com",conf_list)
