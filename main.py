import requests
from collections import Counter

URL = "https://eng.mipt.ru/why-mipt/"

def get_text(url):
    response = requests.get(url)
    return response.text

def main():
    words_file = "words.txt"
    
    text = get_text(URL)
    word_counts = Counter(text.split())
    
    frequencies = {}
    with open(words_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                frequencies[word] = word_counts.get(word, 0)
                
    print(frequencies)

if __name__ == "__main__":
    main()