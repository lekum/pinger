from __future__ import print_function
from subprocess import check_output
from time import localtime, strftime, sleep

def get_ping_time(host):
    ping_output = check_output(["ping", host, "-c", "1"]).decode()
    ping_time, unit = ping_output.split("time=")[1].split("\n")[0].split()
    return ping_time, unit

def get_timestamp():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("interval", type=int)
    parser.add_argument("-o", "--outfile")
    args = parser.parse_args()

    print("Starting ping logging to host", args.host)

    if args.outfile:
        outfile = open(args.outfile, "w")
        print("Logging to", args.outfile)


    while True:
        ping_time, unit = get_ping_time(args.host)
        ping_time_with_comma = ping_time.replace(".",",")
        log_line = ";".join((get_timestamp(), ping_time_with_comma, unit))
        print(log_line)
        if args.outfile:
            print(log_line, file=outfile)
            outfile.flush()
        sleep(args.interval)
