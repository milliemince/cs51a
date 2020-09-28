#millie mince
#cs51A
#december 11 2019
#assignment 12!

from stack_queue import *
import urllib
from urllib.request import *
import ssl
import time

def is_pomona_url(url):
    """returns a bool whether the input url is a 
    pomona url or not"""
    return "pomona.edu" in url

def is_full_url(url):
    """returns a bool whether the input url is a full
    url or not"""
    return url[0:4] == "http"

def get_all_urls(url):
    """opens the input url, converts its contents to
    text, searches for hyperlinked url's and 
    returns a list of all these urls"""
    context = ssl._create_unverified_context()    
    try: 
        reader = urlopen(url, context=context)
    except urllib.error.URLError:
        print("Ignoring: " + url)
        return []
    except urllib.error.HTTPError:
        print("Ignoring: " + url)
        return []  
    urls = []
    search_line = '<a href="'
    for line in reader: 
        line = line.decode('ISO-8859-1').strip()
        if search_line in line:
            begin_index = line.find(search_line)
            while begin_index != -1:
                end_index = line.find('"', begin_index+len(search_line))
                some_url = line[begin_index + len(search_line): end_index]
                if is_full_url(some_url):
                    urls.append(some_url)
                begin_index = line.find(search_line, end_index)
            end_index = line.find('"', begin_index+len(search_line))
            some_url = line[begin_index+len(search_line):end_index] 
            if is_full_url(some_url):
                urls.append(some_url)
    reader.close()
    return urls

def filter_pomona_urls(l_urls):
    """takes as input a list of urls and returns another
    list containing only the pomona urls in that list"""
    filtered_urls = []
    for url in l_urls:
        if is_pomona_url(url):
            filtered_urls.append(url)
    return filtered_urls

def crawl_pomona(url, search_algorithm, max_urls):
    """starting at the original input url, crawl_pomona
    returns a list of all the pomona url's it can visit
    if it cannot visit more than the input max_urls.
    The order in which the crawler visits urls is 
    determined by the input search algorithm, either
    a Stack or a Queue."""
    to_visit = search_algorithm
    already_visited = set()
    to_visit.add(url)
    urls_visited = 0
    websites = [url]
    while not to_visit.is_empty() and urls_visited < max_urls:
        next_url = to_visit.remove()
        time.sleep(0.1)
        already_visited.add(next_url)
        print("Crawling: " + str(next_url))
        urls_visited += 1
        next_urls = get_all_urls(next_url)
        for url in next_urls:
            if not url in already_visited:
                to_visit.add(url)
                websites.append(url)
    return websites

def write_list_to_file(somelist, filename):
    """takes an input list and returns an output file
    in which each line is an element of the input list"""
    out = open(filename, "w")
    for elt in somelist:
        out.write(elt + "\n")
    out.close()
        
def write_pomona_urls(url, to_visit, max_urls, outfile):
    """takes an input url, crawls the url without visiting
    more than the input max_urls. returns a file 
    containing all the pomona links that were 
    visited during the crawl"""
    urls = crawl_pomona(url, to_visit, max_urls)
    write_list_to_file(urls, outfile)
    
"""If we were only going to select 100 URL's, the 
Queue implementation would be better. Since we're
starting at Pomona's main webpage, the Queue
implementation allows us to visit a greater breadth 
of Pomona's website than the Stack implementation
does. For example, when using a Queue, our web
crawler visits the academic calendar, the news, 
the admissions page, the academics page, the map,
and athletic pages. With the stack implementation, 
we do not see most of these pages in the first
100 urls the crawler visits."""