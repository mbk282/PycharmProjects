text = open('event_links(no-dups)','rb')
textfile = text.read()

with open('event_links(no-dups)-for_sitemap', 'wb') as data:
    for link in textfile:
        data.write("'"+link+"',")

data.close()