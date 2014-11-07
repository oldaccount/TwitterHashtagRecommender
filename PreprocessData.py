# se diversi tweet sono identici --> eliminarli (SPAM)
#rimuovere hashtag, punteggiatura, simboli strani, etc.
#se il tweet  vuoto dopo aver rimosso lo schifo, eliminare riga
#lasciare solo nomi, verbi, avverbi e aggettivi
#tradurre slang: vedere come fare
#togliere le immaginette
#rimuovere soli hashtag FATTO
from os.path import expanduser
import csv
import string


def read_file():
    home = expanduser("~")
    path_to_file = "/Desktop/NLP Project/"
    file_name = "tweets.csv"
    with open(home + path_to_file + file_name, 'rb') as f:
        for row in csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL):
            tweets_read.append(row[0])
            hashtags_read.append(row[1])


def write_file(tweets, hashtags):
    home = expanduser("~")
    path_to_file = "/Desktop/NLP Project/"
    file_name = "training.csv"
    rows = [[tweets[i], hashtags[i]] for i in range(0, len(tweets))]
    with open(home + path_to_file + file_name, 'wb') as f:
        csv.writer(f, quoting=csv.QUOTE_ALL).writerows(rows)


def remove_hashtags(tweets):
    processed_tweets = []
    for tweet in tweets:
        string_list = tweet.split(' ')
        new_list = []
        for element in string_list:
                if not element.startswith('#'):
                        new_list.append(element)
        processed_tweets.append(' '.join(new_list))
    return processed_tweets

#toglie parole come &34 etc
def remove_HTML_character(tweets):
    processed_tweets = []
    for tweet in tweets:
        string_list = tweet.split(' ')
        new_list = []
        for element in string_list:
                if not element.startswith('&'):
                        new_list.append(element)
        processed_tweets.append(' '.join(new_list))
    return processed_tweets

#rimuove tag di altre persone @esempio
def remove_user_tags(tweets):
    processed_tweets = []
    for tweet in tweets:
        string_list = tweet.split(' ')
        new_list = []
        for element in string_list:
                if not element.startswith('@'):
                        new_list.append(element)
        processed_tweets.append(' '.join(new_list))
    return processed_tweets

def only_ascii(c):
    if (ord(c)>= 65 and ord(c) <= 90) or (ord(c)>= 97 and ord(c) <= 122) or c == ' ':
        return c
    else:
        return ''

#rimangono le faccine
def remove_punctuation_shallow(tweets):
    processed_tweets = []
    for tweet in tweets:
            processed_tweets.append(tweet.translate(string.maketrans("",""), string.punctuation))
    return processed_tweets

#rimuove tutto cio che non e uno spazio o una lettera dell alfabeto
def remove_punctuation_deep(tweets):
    processed_tweets = []
    for tweet in tweets:
            processed_tweets.append(filter(only_ascii, tweet))
    return processed_tweets

def process(tweets): #passare l'intera lista
    tweets = remove_hashtags(tweets)
    tweets = remove_HTML_character(tweets)
    tweets = remove_user_tags(tweets)
    #togliere eventuali spazi ripetuti
    tweets = remove_punctuation_deep(tweets)
    return tweets

if __name__ == '__main__':
    tweets_read = []
    hashtags_read = []
    read_file()
    tweets_processed = process(tweets_read)
    write_file(tweets_processed, hashtags_read)