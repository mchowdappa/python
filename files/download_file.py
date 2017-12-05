#from urllib import request  ## This works in Python 3.x

import urllib

data_url = r'https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportCompleteSample.csv'


def download_stock_data(csv_url):
    response = urllib.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'ibm.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line+"\n")
    fx.close()
download_stock_data(data_url)
