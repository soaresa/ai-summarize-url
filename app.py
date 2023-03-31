import requests
from bs4 import BeautifulSoup

from Services.chat_completion import chat_completion

def scrape_medium_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').text
    paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    text = ' '.join([para.text for para in paragraphs])
    return title, text

def summarize_text(text):
    response = chat_completion("Please summarize the following article in 2 paragraphs: " + text)
    summary = response.content
    return summary

title, text = scrape_medium_article("https://medium.com/@avi-loeb/will-future-ai-systems-be-legally-liable-8ac4339da547")
sum = summarize_text(text)
print('>>> Summary: \n\n' + title + '\n\n' + sum)
