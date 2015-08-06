# Script to convert Kentucky Voter Registration database from fixed width to CSV with the proper fields
# All information in this script current as of 2015
# By: Jesse Hazel for The Courier-Journal
# To run: python convert.py {FILENAME}.txt


from sys import argv
import csv
script, filename = argv

#These are the field widths (start,end) as described in the documentation the from State Board of Elections
fieldWidths = (
	(1,3),
	(4,7),
	(8,8),
	(9,33),
	(34,48),
	(49,58),
	(59,59),
	(60,60),
	(61,63),
	(64,103),
	(104,123),
	(124,125),
	(126,134),
	(135,174),
	(175,194),
	(195,196),
	(197,205),
	(206,213),
	(214,221),
	(222,241)
	)

fieldNames = (
	"County Code",
	"Precinct Code",
	"City Code",
	"Last Name",
	"First Name",
	"Middle Name",
	"Sex",
	"Party",
	"Other Code",
	"Residence Street Address",
	"Residence City Address",
	"Residence State",
	"Residence Zip",
	"Mailing Street Address",
	"Mailing City Address",
	"Mailing State",
	"Mailing Zip",
	"Date of Birth",
	"Date of Registration",
	"Voting History"
	)


#Open output and write the header
outputFile = open('output.csv', 'w')
writer = csv.writer(outputFile, dialect = 'excel')
writer.writerow(fieldNames);

i=0;
with open(filename) as f:
    for line in f:
    	lineOut = []
        for field in fieldWidths:
        	lineOut.append(line[field[0]-1:field[1]])
        writer.writerow(lineOut)
        i+=1

print "Done. Wrote {} lines to output.csv".format(i)
