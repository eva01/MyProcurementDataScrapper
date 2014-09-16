MyProcurementDataScrapper
=========================

Data Scrapper in Python to grab data from MyProcurement website

This is a (very) simple Python script to grab data from the Malaysian Government's myProcurement website.

Currently the output is a single delimited file, and by default the delimiter is set to '|' because commas and colons appear in the data. This can be changed by changed the delimiter variable in the code.
The code was built on Python 2 (27 to be exact), and requires BeautifulSoup to run.

Future enhancements planned:
-Fix For loop, to loop until no data, rather than the fixed 1020 times now
-Retrieve header data
-Ability to store carriage returns in output file (that are not the end of the lines)
-Improve data quality of the output
  -standardize sdn. bhd., sdn bhd, SDN BHD to SDN. BHD.
  -remove all '-X' from the ROC registration (not required)
