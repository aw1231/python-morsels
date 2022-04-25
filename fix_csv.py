import sys

if len(sys.argv) == 3:
    input = sys.argv[1]
    output = sys.argv[2]
else:
    exit

with open(input) as infile:
    with open(output, mode="w") as outfile:
        inputlist = infile.read().splitlines()
        outputlist = []
        for line in inputlist:
            linelist = line.split("|")
            outputline = ""
            for entry in linelist:
                if "," in entry and outputline != "":
                    outputline = outputline + ',"' + entry + '"'
                elif outputline != "":
                    outputline = outputline + "," + entry
                else:
                    outputline = entry
            outputline = outputline + "\n"
            outfile.write(outputline)
