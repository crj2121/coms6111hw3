def main():
    # Read in file and get a generator using itertools
    csvFile = iterateCSV(sys.argv[1])
    minSupp = float(sys.argv[2])
    minConf = float(sys.argv[3])

    