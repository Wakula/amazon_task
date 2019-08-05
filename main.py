from selenium import webdriver
from bs4 import BeautifulSoup


def get_word(html, searched_word):
    soup = BeautifulSoup(html, 'lxml')
    elems = soup.find_all('div', class_='sg-col-inner')
    for elem in elems:
        text = elem.text.split()
        for word in text:
            if word == searched_word:
                return word
def get_phrase(driver):
    url_virtue = r'https://www.amazon.com/s?k=virtue&ref=nb_sb_noss_1'
    url_signaling = r'https://www.amazon.com/s?k=signalling&ref=nb_sb_noss_2'
    url_is = r'https://www.amazon.com/s?k=is&ref=nb_sb_noss_2'
    url_society = r'https://www.amazon.com/s?k=societys+child&crid=1PDOVTN3D3WRW&sprefix=societys%2Caps%2C232&ref=nb_sb_ss_i_1_8'
    url_version = r'https://www.amazon.com/s?k=version&ref=nb_sb_noss_2'
    url_of = r'https://www.amazon.com/s?k=state&ref=nb_sb_noss_2'
    url_proof = r'https://www.amazon.com/s?k=proof&ref=nb_sb_noss'
    url_of2 = r'https://www.amazon.com/s?k=state+of+the+heart&crid=1ZSI0T8K72R74&sprefix=state+of+%2Caps%2C257&ref=nb_sb_ss_i_1_9'
    url_stake = r'https://www.amazon.com/s?k=stake&ref=nb_sb_noss_2'
    urls = {
        url_virtue : 'Virtue',
        url_signaling : 'signalling',
        url_is : 'is', 
        url_society : "Society's",
        url_version : 'version',
        url_of : 'of',
        url_proof : 'Proof',
        url_of2: 'of',
        url_stake : 'Stake'}
    phrase = []
    for url, word in urls.items():
        driver.get(url)
        phrase.append(get_word(driver.page_source, word))
    return ' '.join(phrase)


def main():
    try:
        searched_phrase = "Virtue signalling is society's version of Proof of Stake"
        driver = webdriver.Chrome()
        result = get_phrase(driver)
        print(result)
        if searched_phrase == result:
            print('Possible')
        else:
            print('impossible')
    finally:
        driver.close()


if __name__ == '__main__':
    main()
