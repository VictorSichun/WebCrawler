import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import ssl

unvisited_url = ['https://www.zhihu.com/question/38473122']
visited_url = []
working_url = ''
folder_name = 'crawler_testing_file'
parent_path = '/Users/victor/Desktop/'
current_directory = os.path.join(parent_path, folder_name)


# bypass verification
#context = ssl._create_unverified_context()
while len(unvisited_url) > 0:
    working_url = unvisited_url.pop(0)
    visited_url.append(working_url)
    opening_page = urllib.request.urlopen(working_url)
    page_content = BeautifulSoup(opening_page, "html.parser")
    fetched_content = page_content.findAll('img')

    for i in fetched_content:
        try:
            img_url = urljoin(working_url, i['data-actualsrc'])
            file_name = i['src'].split('/')[-1]
            # check if the directory exists; if not, create a new one
            if not os.path.exists(current_directory):
                os.makedirs(current_directory)

            file_path = os.path.join(current_directory, file_name)
            urllib.request.urlretrieve(img_url, file_path)
        except Exception as e:
            print(e)
            continue

    urllib.request.urlcleanup()
    '''
    if content is HTML
        parse out URLs from links
        foreach URL
           if it matches your rules
              and it's not already in either the visited or unvisited list
              add it to the unvisited list
    '''
print("success!")