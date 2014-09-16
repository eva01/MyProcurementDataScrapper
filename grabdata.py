from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib2  

gov_tender_url="http://myprocurement.treasury.gov.my/templates/theme427/keputusantender_arkib.php?sort=&by=&page="
delimiter = '|'
bordercoloroftable = '#000000'
output_file_name = 'Arkib_Keputusan_Tender.dat'

#open file
output_file = open(output_file_name, 'w')

for x in range(1, 1020):

        current_url_being_read = gov_tender_url + str(x)
        print '@@@@@' + str(x)
        print current_url_being_read

        try:
            gov_tender_html = urllib2.urlopen(current_url_being_read)
        except HTTPError, e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        except URLError, e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        else:
       
                soup = BeautifulSoup(gov_tender_html)
                html_output =soup.find('table', attrs={'bordercolor':bordercoloroftable})
                # grabs the top row

                rows = html_output.findAll('tr')

                #prints all rows with columns delimited by delimiter--only IF the first column of the row is a number (1., 2., 3.,.....10190.)
                for tr in rows:
                  cols = tr.findAll('td')
                  rowtext = ''
                  firstColumnData = cols[0].text.strip('.') #first column is usually a number followed by '.'

                  if firstColumnData.isdigit(): #check if it's a number
                        
                        for td in cols:
                                rowtext= rowtext+ td.text.strip() + delimiter
                        print rowtext
                        new_rowtext= rowtext.encode('utf-8')
                        new_rowtext= new_rowtext.replace('\n','').replace('\r','') + '\n'
                        output_file.write(new_rowtext)
                                        
                print '@@@@@' + str(x)

output_file.close()


