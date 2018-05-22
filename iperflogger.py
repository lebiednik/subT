import os, sys
import time

#Logging program for Iperf


def main(argv):
    iplist = {"10.52.202.42", "10.52.202.43"}
    if (len(argv) == 2):
        sleeptime = argv[1]
    else:
        sleeptime = 300
        for ipaddr in iplist:
            try:
                print("Running iperf on " + ipaddr)
                os.system("/usr/bin/iperf -c "+ ipaddr + " -i 1 -y c -d -t 10 >>output.csv")
            except:
                print("Something went wrong")
    print("Sleeping for " + str(sleeptime) + " seconds")
    time.sleep(sleeptime) 


if __name__ == "__main__":
    main(sys.argv)
