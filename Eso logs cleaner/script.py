f = open("Encounter.log", "r")

OutFile = open("CleanEncounter.log", "w")


for line in f:
    a = 0

    try:
        a = int(line[0:7])
    except ValueError:
        a = a
    
    if (a < 3084697):
        if "INFO" in line:
            OutFile.write(line)
    else:
        OutFile.write(line)

    
