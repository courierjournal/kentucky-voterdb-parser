# Script to convert Kentucky Voter Registration database from fixed width to
# CSV with the proper fields
# All information in this script current as of 2017
# By: Jesse Hazel for The Courier-Journal
# To run: python convert.py {FILENAME}.txt


from sys import argv
import csv
import codecs
script, filename = argv

# These are the field widths (start,end) as described in the documentation the
# from State Board of Elections
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
	(222,241),
	(222,223),
	(224,224),
	(225,225),
	(226,227),
	(228,228),
	(229,229),
	(230,231),
	(232,232),
	(233,233),
	(234,235),
	(236,236),
	(237,237),
	(238,239),
	(240,240),
	(241,241)
	)

fieldNames = (
	"COUNTY_CODE",
	"PRECINCT_CODE",
	"CITY_CODE",
	"LAST_NAME",
	"FIRST_NAME",
	"MIDDLE_NAME",
	"GENDER",
	"PARTY",
	"OTHER_CODE",
	"ADDRESS_RESIDENCE",
	"CITY_RESIDENCE",
	"STATE_RESIDENCE",
	"ZIP_RESIDENCE",
	"ADDRESS_MAILING",
	"CITY_MAILING",
	"STATE_MAILING",
	"ZIP_MAILING",
	"DOB",
	"REGISTRATION_DATE",
	"HISTORY_RAW",
	"H_YR1_LABEL",
	"H_YR1_PRIMARY",
	"H_YR1_GENERAL",
	"H_YR2_LABEL",
	"H_YR2_PRIMARY",
	"H_YR2_GENERAL",
	"H_YR3_LABEL",
	"H_YR3_PRIMARY",
	"H_YR3_GENERAL",
	"H_YR4_LABEL",
	"H_YR4_PRIMARY",
	"H_YR4_GENERAL",
	"H_YR5_LABEL",
	"H_YR5_PRIMARY",
	"H_YR5_GENERAL",
	)

#String formatter to clean up some of the fields
def formatString(label, line):
  if label == "ZIP_RESIDENCE" or label == "ZIP_MAILING" and line != "":
    return line[0:5]
  elif label == "DOB" or label == "REGISTRATION_DATE" and line != "":
  	#XXX: dates are sometimes (likely incorrectly) <1900 which causes datetime to choke
  	#for now we'll just statically format dates, deal with them as outliers in the model
  	day = line[2:4]
  	month = line[0:2]
  	year = line[4:8]
  	return year + "-" + month + "-" + day
    #return datetime.strptime(line, '%m%d%Y').strftime('%Y-%m-%d')
  else:
    return line


#Open output and write the header
outputFile = open('output.csv', 'w')
writer = csv.writer(outputFile, dialect = 'excel')
writer.writerow(fieldNames)

#Loop through the file and parse each line
i=0
with codecs.open(filename, 'r', 'utf-8') as f:
  for line in f:
    lineOut = []
    for index, field in enumerate(fieldWidths):
      newField = line[field[0]-1:field[1]].encode('utf-8').strip()
      lineOut.append(formatString(fieldNames[index], newField))
    writer.writerow(lineOut)
    i+=1
    print "*Wrote line {}\r".format(i),
    

print "Done. Wrote {} lines to output.csv".format(i)
