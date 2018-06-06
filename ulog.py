#Program that logs link status from HSMM
#Written by Stephen Hamilton
#Last Modified 4 June 2018

import sys
from BeautifulSoup import BeautifulSoup
import urllib2
import time

def gethtml(ipaddr):
    #Try to get the status:
    try:
        r = urllib2.urlopen("http://"+ ipaddr+ ":8080/cgi-bin/mesh/")
        return r.read()
    except:
        print("Failed to reach site: " + ipaddr)
        return "-1"  

def parsehtml(html):
    newnodes = True
    td = 11
    nodelist = []
    nodenum = 0

    print("New nodes: " + str(newnodes))
    while (newnodes):
        soup = BeautifulSoup(''.join(html))
        node = soup('td')[td].contents[0]
        #import pdb;pdb.set_trace()
        lq = soup('td')[td+2].contents[0]
        if (str(lq)[-1] == "%"):
            node = str(node).split('/')[2] #Just get the hostname
            #Found a link quality, so add it to the list
            nodelist.append([node, lq])    
            #print("added " + str(node))   
        else:
            #print("stop" + str(lq)[-1]) 
            return nodelist
        td = td + 5
    #except:
        #print("No nodes found")
    #return nodelist

def main(argv):
    while(1):
        ips = ["10.33.86.81"]
        filename = "out.csv"
        for ipaddr in ips:
            html = gethtml(ipaddr)      
            nodelist = parsehtml(html)
        f = open(filename, "a")
        if (nodelist):
            for node in nodelist:
                print("Node: " + str(node[0]))
                print("Quality: " + str(node[1]))
                f.write(str(time.ctime()) + ",")
                f.write(str(node[0]) + ",")
                f.write(str(node[1]) + "\n")
        f.close()
        #Wait and do again in 5 minutes
        time.sleep(10)
if __name__ == "__main__":
    main(sys.argv)
