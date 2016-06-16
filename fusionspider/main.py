#!/usr/bin/env python
#-.- coding:utf-8 -.-


import sys
import getopt
import dospider


def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hi:c:dm", ["help","ip","cdn","map"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        dospider.usage()
        sys.exit(2)

    if len(sys.argv) == 1:
        dospider.usage()
        sys.exit(2)

    for o, a in options:
        if o in ("-h","--help"):
            dospider.usage()
        elif o in ("-i", "--ip"):
            dospider.checkip(a)
        elif o in ("-c", "--cdn"):
            dospider.checkcdnip(a)
        elif o in ("-m", "--map"):
            dospider.getRegionByDomian(a)
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()