import urllib.request

unvisited_url = ['http://www.baidu.com/']
visited_url = []
working_url = ''
file_name = 'crawler_testing_file'
parent_path = '/Users/victor/Documents/'
while len(unvisited_url) > 0:
    working_url = unvisited_url.pop(0)
    visited_url.append(working_url)
    contents = urllib.request.urlopen(working_url).read()
    working_file = open(parent_path + file_name, 'wb')
    working_file.write(contents)
    '''
    if content is HTML
        parse out URLs from links
        foreach URL
           if it matches your rules
              and it's not already in either the visited or unvisited list
              add it to the unvisited list
    '''
working_file.close()
print("success!")


