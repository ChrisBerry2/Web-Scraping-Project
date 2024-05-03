from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from plotly.graph_objs import bar
from plotly import offline
#use this code to remove the error
import ssl
context = ssl._create_unverified_context()


'''
Author Statistics:

Count the number of quotes by each author.
Find the author with the most and least quotes.
Quote Analysis:

Determine the average length of quotes.
Identify the longest and shortest quotes.
Tag Analysis:

If there are tags associated with each quote, analyze the distribution of tags.
What is the most popular tag?
How many total tags were used across all quotes?
'''
quote_dict = {}
quote_len = {}
quote_num = {}
tags = []

for page in range(1,11):
    url = 'https://quotes.toscrape.com/page/' + str(page) + '/'
    url = 'https://quotes.toscrape.com/page/1/' 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url,headers = headers)
    #this line is also required to remove the error
    webpage = urlopen(req,context=context).read()
    soup = BeautifulSoup(webpage,'html.parser')

    i = 0
    for quote in soup.findAll('div', class_='quote'):
        span = soup.find('span', attrs={'class':'text'})
        #print(span)
        #input()
        span_text = span.text
        clean_span = attrs=({'class':'text'})

        get_author = soup.findAll('small',attrs={'class':'author'})
        author = get_author.text

        get_tag = soup.findAll('a',attrs={'class':'tag'})
        tag = get_tag.text
        clean_tag = tag.replace('Tags:','')
        tags.extend(clean_tag.split())

        quote_len[span_text] = [len(span_text)]
        i += 1

        if author not in quote_dict:
            quote_dict[author] = [clean_span]
        else: 
            quote_dict[author].append(clean_span)
    
    for tag in tags: 
        if tag not in quote_num:
            quote_num[tag] = 1
        else:
            quote_num[tag] += 1

    max_count = max(quote_num.values())

    pop_tag = [word for word, count in quote_num.items() if count == max_count]
    quote_count = {x: len(quotes) for x, quotes in quote_dict.items()}

    max_quote = max(quote_count.values())
    min_quote = min(quote_count.values())

    max_author = [author for author, count in quote_count.items() if count == max_quote]
    min_author = [author for author, count in quote_count.items() if count == min_quote]

    quote_total = sum(length[0] for length in quote_len.values())
    num_quotes = len(quote_len)

    avg_len = quote_total / num_quotes
    long_quote = max(quote_len, key = lambda quote: quote_len[quote][0])
    short_quote = min(quote_len, key = lambda quote: quote_len[quote][0])

    print('List of each author and their number of quotes:')
    for x, y in quote_count.items():
        print('\nAuthor', x)
        print('Number of quotes:', y)

    print(max_author[0], 'has the most quotes\n') 
    print('Authors with the least amount of quotes:')
    for author in min_author:
        print(author)
    
    print('The average quote length:', avg_len)
    print('\nthe longest quote:\n', long_quote)
    print('The shortest quote:\n', short_quote)

    print('The most popular tag is', pop_tag[0])
    print('The total number of tags are', len(tags))

    input()
    top_author = sorted(quote_count.items(), key = lambda x:x[1], reverse=True)[:10]
    author_names, author_quotes = zip(*top_author)

    author_data = [
        {
            'type':'bar',
            'x':author_names,
            'y':author_quotes,
        }
    ]

    author_format = {
        'title':'Top 10 Authors based on No. Quotes',
        'xaxis':{'title':'Author'},
        'yaxis':{'title':'No of Quotes'}
    }

    chart1 = {'data':author_data,"layout":author_format}
    offline.plot(chart1, filename='author_quotes.html')

    top_tags = sorted(quote_count.items(), key=lambda x:x[1],reverse=True)[:10]
    tag_name, tag_count = zip(*top_tags)

    tag_data = [
        {
            'type':'bar',
            'x':tag_name,
            'y':tag_count,
        }
    ]

    tag_format = {
        'title':'Top 10 Tags',
        'xaxis':{'title':'Tag'},
        'yaxis':{'title':'No. of Tags'}
    }

    offline.plot({'data': tag_data, 'layout': tag_format}, filename='top_tags.html', auto_open=False)
    #hart2 = {'data': tag_data, 'layout':tag_format}
    #offline.plot(chart2, filename= 'top_tags.html')
    