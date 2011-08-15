import pprint, pickle
import sys, os
from createchart import CreateConfChart
graph_data = {}

def getMean(numList):
    return sum(numList)/len(numList)
# read latency data from a pkl file 
# and update data_dict dictiory
def ReadPickleFile(pklfile):
    pkl_file = open(pklfile, 'rb')

    data1 = pickle.load(pkl_file)
    conf,nr_workers,latencies_by_url=data1
    #print conf,"\n",nr_workers,"\n"

    for url, latencies in latencies_by_url.items():
        #print url,"::",latencies
        for latency in latencies:
            # if the latency value is timeout
            # then we ignore it & take the mean 
            # for rest of the values
            if not (isinstance(latency,float) or isinstance(latency,int)):
                latencies.remove(latency)
        
        mean = getMean(latencies)
        #put the data into dictionary that will be 
        #later used for graph generation

        # if this is the first time data for this url 
        # is being added to the dict then we create a 
        # subdictionay object whose keys will be the different 
        # service cofigurations
        if not graph_data.has_key(url):
            graph_data[url] = {}
        # if this is the first time data for this service 
        # configuration is being added to the dict then we create
        # empty nr_worker_list & empty latency list
        if not graph_data[url].has_key(conf):
            graph_data[url][conf]=([],[])
        # add the nr_worker & latency data
        # we add the data in sorted order for better graph 
        # display
        graph_data[url][conf][0].append(int(nr_workers))
        print "Before::",graph_data[url][conf][0],
        graph_data[url][conf][0].sort()
        print "After::",graph_data[url][conf][0],"\n\n"
        index = graph_data[url][conf][0].index(int(nr_workers))
        graph_data[url][conf][1].insert(index, mean)
        
        #print url,",",conf,",",nr_workers,",",mean
    #print graph_data,"\n"        
    pkl_file.close()

log_dir = sys.argv[1]
for f in os.listdir(log_dir):
    #print f;
    ReadPickleFile(os.path.join(log_dir,f));

#print the dict
for url in graph_data.keys():
    chart_data = []
    for conf in graph_data[url].keys():
        #print url,",",conf,",",graph_data[url][conf][0],"::",graph_data[url][conf][1]
        t = (conf,graph_data[url][conf][0],graph_data[url][conf][1])
        chart_data.append(t);
        #print t
    #print "\n"
        
    print url,"::",chart_data
    # striping http:// as this parametere will be used in filename
    # and filename cannot have such chars
    CreateConfChart(url.strip('http://'),chart_data)
