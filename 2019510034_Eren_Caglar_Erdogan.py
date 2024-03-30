import requests
from bs4 import BeautifulSoup

print("if you want to count word frequencies of one book press 1 and enter" )
print ("if you want to compare two books word frequencies press 2 and enter")
a= int(input())
print("WARNING!! operations may take a while")
#stopwords list
stopwords = ['will','9','8','7','6','5','4','3','2',' ','0','1','a', 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came', 'can', 'cannot', "can't", 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', 'i', 'id', 'ie', 'if', "i'll", 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is', "isn't", 'it', 'itd', "it'll", 'its', 'itself', "i've", 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', "'ll", 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', "she'll", 'shes', 'should', "shouldn't", 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure', 't', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', "there'll", 'thereof', 'therere', 'theres', 'thereto', 'thereupon', "there've", 'these', 'they', 'theyd', "they'll", 'theyre', "they've", 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', "'ve", 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', "we'll", 'went', 'were', 'werent', "we've", 'what', 'whatever', "what'll", 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', "who'll", 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', 'wont', 'words', 'world', 'would', 'wouldnt', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', "you'll", 'your', 'youre', 'yours', 'yourself', 'yourselves', "you've", 'z', 'zero']

if a == 1:

    #you should pay attention to uppercase letters and punctuation when entering the names of books /sample input= Non-Programmer's Tutorial for Python 2.6
    #the name of the book must be the same as the name of the wikibooks address
    book1_name = input("please enter the name of your book = ")

    #in order to emulate the URL of the wikibooks site, I split the name of the book I received from the user and combine it with underscore
    name = book1_name.split()
    book1_url = "_".join(name)
    number = int(input("how many word do you want to see = "))

    #I take the site resource with the requests module and process it with the beautifulsoup module
    #There are 3 different print version url types so I compare the length of the source of all three links and take the longest one
    a1 = requests.get("https://en.wikibooks.org/wiki/" + book1_url + "/Print_version")
    a2 = requests.get("https://en.wikibooks.org/wiki/" + book1_url + "/print_version")
    a3 = requests.get("https://en.wikibooks.org/wiki/" + book1_url + "/Print_Version")

    if len(a1.content) > len(a2.content) and len(a1.content) > len(a3.content):
        r = a1
    elif len(a2.content) > len(a1.content) and len(a2.content) > len(a3.content):
        r = a2
    elif len(a3.content) > len(a1.content) and len(a3.content) > len(a2.content):
        r = a3
    soup = BeautifulSoup(r.content, "html.parser")

    #I find the part of the page source that I want to use according to its class and tag
    #I am using .text method for receive a string without any separators or tags
    book1_text = soup.find("div", attrs={"class": "mw-parser-output"})
    book1_text = book1_text.text
    #
    with open("book1.txt", "w", encoding="utf-8") as f:
        f.write(book1_text)

    #removing punctuation marks from text
    punc = '''!()-[]{};:'"\, ←<>./?@#$%^&*_~='''
    for ele in book1_text:
        if ele in punc:
            book1_text = book1_text.replace(ele, " ")

    #I tried to create meaningful variable names
    #list means list off all words that occurs in books
    #count is a dictionary that keeps word frequencies
    #word_rank is a list
    book1_text = book1_text.lower()
    word_list = []
    word_list = book1_text.split()
    word_count = {}
    word_rank = []


    #in this loop i am counting frequencies of the words in the book and keeping values in a dictionary
    #it also extracts stopwords
    for i in word_list:
        if i in word_count:
            word_count[i] = word_count[i] + 1
        elif i not in word_count and i not in stopwords:
            word_count[i] = 1

    #I added the words in the dictionary to a list
    for i in word_count:
        word_rank.append(i)

    #In this nested loop, I sort the words in the word_rank list according to their values ​​in the dictionary
    for i in range(0, len(word_rank)):
        for j in range(i + 1, len(word_rank)):
            if word_count[word_rank[i]] < word_count[word_rank[j]]:
                holder = ""
                holder = word_rank[i]
                word_rank[i] = word_rank[j]
                word_rank[j] = holder

    #sorted words in the word_rank list are printed on the screen using the format method
    print("\n\n",book1_name)
    print("NO WORD           FREQ_1")
    for i in range(0,number):
        print('{:>2} {:<13}\t{:>4}'.format(i+1,word_rank[i],word_count[word_rank[i]]))

if a == 2:
    book1_name = input("please enter the first books name = ")
    name1 = book1_name.split()
    book1_url = "_".join(name1)

    number = int(input("how many word do you want to see = "))
    a1 = requests.get("https://en.wikibooks.org/wiki/" + book1_url + "/Print_version")
    a2 = requests.get("https://en.wikibooks.org/wiki/" + book1_url + "/print_version")
    a3 = requests.get("https://en.wikibooks.org/wiki/" + book1_url + "/Print_Version")

    if len(a1.content) > len(a2.content) and len(a1.content) > len(a3.content):
        r1 = a1
    elif len(a2.content) > len(a1.content) and len(a2.content) > len(a3.content):
        r1 = a2
    elif len(a3.content) > len(a1.content) and len(a3.content) > len(a2.content):
        r1 = a3
    soup1 = BeautifulSoup(r1.content, "html.parser")



    book1_text = soup1.find("div", attrs={"class": "mw-parser-output"})
    book1_text = book1_text.text
    with open("book1.txt", "w", encoding="utf-8") as f:
        f.write(book1_text)
    #removing punctuation marks from text for book 1
    punc = '''!()-[]{};:'"\←, <>./?@#$%^&*_~='''
    for ele in book1_text:
        if ele in punc:
            book1_text = book1_text.replace(ele, " ")

    #creating variables for book 1
    book1_text = book1_text.lower()
    word1_list = []
    word1_list = book1_text.split()
    word1_rank = []
    word1_count = {}

    #counting word frequencies for Book 1
    for i in word1_list:
        if i in word1_count:
            word1_count[i] = word1_count[i] + 1
        elif i not in word1_count and i not in stopwords:
            word1_count[i] = 1

    #adding words in the dictionary to word1_rank
    for i in word1_count:
        word1_rank.append(i)
    #the name of the second book is requested from the user


    book2_name = input("please enter the second books name = ")
    name2 = book2_name.split()
    book2_url = "_".join(name2)

    b1 = requests.get("https://en.wikibooks.org/wiki/" + book2_url + "/Print_version")
    b2 = requests.get("https://en.wikibooks.org/wiki/" + book2_url + "/print_version")
    b3 = requests.get("https://en.wikibooks.org/wiki/" + book2_url + "/Print_Version")

    if len(b1.content) > len(b2.content) and len(b1.content) > len(b3.content):
        r2 = b1
    elif len(b2.content) > len(b1.content) and len(b2.content) > len(b3.content):
        r2 = b2
    elif len(b3.content) > len(b1.content) and len(b3.content) > len(b2.content):
        r2 = b3
    soup2 = BeautifulSoup(r2.content, "html.parser")

    book2_text = soup2.find("div", attrs={"class": "mw-parser-output"})
    book2_text = book2_text.text
    with open("book2.txt", "w", encoding="utf-8") as f:
        f.write(book2_text)
    # removing punctuation marks from text for book 2
    punc = '''!()-[]{};:←'"\, <>./?@#$%^&*_~='''
    for ele in book2_text:
        if ele in punc:
            book2_text = book2_text.replace(ele, " ")

    # creating variables for book 2
    book2_text = book2_text.lower()
    word2_list = []
    word2_list = book2_text.split()
    word2_rank = []
    word2_count = {}

    # counting word frequencies for Book 2
    for i in word2_list:
        if i in word2_count:
            word2_count[i] = word2_count[i] + 1
        elif i not in word2_count and i not in stopwords and i is not i.isdigit():
            word2_count[i] = 1

    # adding words in the dictionary to word2_rank
    for i in word2_count:
        word2_rank.append(i)
    #if a word is in the wordrank1 and wordrank2 lists, it is common word
    common_rank = []
    for i in word1_rank:
        if i in word2_rank:
            common_rank.append(i)
    #i am using a dictionary to hold common word frequencys
    common_count = {}
    for i in common_rank:
        common_count[i]=word1_count[i]+word2_count[i]
    #sorting common_rank list according to their vales from common_count
    for i in range(0, len(common_rank)):
        for j in range(i + 1, len(common_rank)):
            if common_count[common_rank[i]] < common_count[common_rank[j]]:
                holder = ""
                holder = common_rank[i]
                common_rank[i] = common_rank[j]
                common_rank[j] = holder

    distinct1_rank =word1_rank
    distinct2_rank = word2_rank

    #if we remove the common words we get discrete words
    for i in common_count:
        distinct1_rank.remove(i)
        distinct2_rank.remove(i)

    #we have to put distinct words in an order
    for i in range(0, len(distinct1_rank)):
        for j in range(i + 1, len(distinct1_rank)):
            if word1_count[distinct1_rank[i]] < word1_count[distinct1_rank[j]]:
                holder = ""
                holder = distinct1_rank[i]
                distinct1_rank[i] = distinct1_rank[j]
                distinct1_rank[j] = holder
    for i in range(0, len(distinct2_rank)):
        for j in range(i + 1, len(distinct2_rank)):
            if word2_count[distinct2_rank[i]] < word2_count[distinct2_rank[j]]:
                holder = ""
                holder = distinct2_rank[i]
                distinct2_rank[i] = distinct2_rank[j]
                distinct2_rank[j] = holder

    print("\n\n\nCOMMON WORDS")
    print("NO WORD\t    \tFREQ_1\tFREQ_2\tTOT FREQ")
    for i in range(0, number):
        print('{:>2} {:<13}{:>5}{:>6}{:>8}'.format(i+1,common_rank[i],word1_count[common_rank[i]],word2_count[common_rank[i]],common_count[common_rank[i]]))


    print("\n\n",book1_name)
    print("DİSTİNCT WORDS")
    print("NO WORD           FREQ_1")
    for i in range(0,number):
        print('{:>2} {:<13}\t{:>4}'.format(i+1,distinct1_rank[i],word1_count[distinct1_rank[i]]))


    print("\n\n",book2_name)
    print("DİSTİNCT WORDS")
    print("NO WORD           FREQ_1")
    for i in range(0,number):
        print('{:>2} {:<13}\t{:>4}'.format(i+1,distinct2_rank[i],word2_count[distinct2_rank[i]]))
