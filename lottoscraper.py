from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv

urls = ["https://www.lottopcso.com/6-45-lotto-result-history-and-summary/", "https://www.lottopcso.com/6-55-lotto-result-history-and-summary/", "https://www.lottopcso.com/6-58-lotto-result-history-and-summary/"]

def extract(url, filename): 
    client = urlopen(url)                                               #opening up connection, grabbing page
    page_html = client.read()
    client.close()

    page_soup = soup(page_html, "html.parser")                          #parsing html

    results_dict = {}                                                   #for tally of results

    with open(filename, "w+") as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        results = page_soup.findAll("tr")
        results_dict = {}                                               #for the tally of the results
        for i in range(len(results)):
            if i == 0:                                                  #this is for the header/column labels of the csv file
                col_labels = results[i].findAll("th")
                row = []
                for j in range(len(col_labels)):
                    col_label = col_labels[j].text.strip()
                    row.append(col_label)
                    #print(col_label)
                file_writer.writerow(row)

            else:                                        
                entries = (results[i].findAll("td"))                    #for the entries in each row of the csv
                row = []
                for j in range(len(entries)):
                    entry = entries[j].text.strip()
                    row.append(entry)
                    #print(entry)
                    if j == 1:
                        nums = entry.split("-")
                        #print(nums)
                        for num in nums:
                            if num not in results_dict:
                                results_dict[num] = 1
                            else:
                                results_dict[num] += 1
                #file_writer.writerow(row + nums)
                file_writer.writerow(row)
    return results_dict


def visualize(dict_results, filename):
    a_file = open(filename, "w+")
    writer = csv.writer(a_file)
    
    for key, value in dict_results.items():
        writer.writerow([key, value])
    
    a_file.close()

    print("File ready")
    return None


results_645 = extract(urls[0], "results_645.csv")
print(urls[0], results_645)
visualize(results_645, "results_645_KVpairs.csv")

results_655 = extract(urls[1], "results_655.csv")
print(urls[1], results_655)
visualize(results_645, "results_655_KVpairs.csv")

results_658 = extract(urls[2], "results_658.csv")
print(urls[2], results_658)
visualize(results_645, "results_658_KVpairs.csv")



