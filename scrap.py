# coding: utf-8
import urllib
from bs4 import BeautifulSoup
import requests

fa = open('futuribles_articles.csv', 'w')
ga = open('futuribles_general.csv', 'w')
ha = open('futuribles_author.csv', 'w')

author_list = []
index_author = []
i = 1
h = 1
author_dict = {}

for n in range (1, 426):
    #On récupère l'URL des pages des archives de revues de 1 à 426
    url = "https://www.futuribles.com/fr/revue/" + str(n)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    #On récupère le premier noeud où sont contenues les métadonnées des articles
    article = soup.find_all('div', class_="toc-article")
    for child in article:
        article_name = child.meta
        article_name = article_name.find_next_sibling('meta')
        article_out = article_name['content']
        fa.write(str(i) + ";" + article_out + "\n")

        try:
            author = child.find('p', class_="author")
            author = author.span
            author_out = author.find_all('span', itemprop='name')
            for element in author_out:
                for author_name in element:
                    author_dict[h] = (author_name, i)
                    h += 1
        except AttributeError:
            author_name = "NULL"
            author_dict[h] = (author_name, "NULL")
            h += 1

        i += 1

for name, art in author_dict.values():
    index_author.append(art)
    author_list.append(name)

author_general_list = []

for name in author_list:
    if name not in author_general_list:
        author_general_list.append(name)
y = 1
while y < len(author_general_list):
    ha.write(str(y) + ";" + str(author_general_list[y - 1]) + "\n")
    y += 1

z = 1
while z < len(author_dict) + 1:
    index_general = author_general_list.index(author_list[z - 1])
    ga.write(str(z) + ";" + str(author_list[z - 1]) + ";" + str(index_general + 1) + ";" + str(index_author[z - 1]) + "\n")
    z += 1

fa.close()
ga.close()
ha.close()
