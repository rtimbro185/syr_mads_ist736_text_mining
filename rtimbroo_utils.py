# -*- coding: utf-8 -*-
# RTIMBROO UTIL FUNCTIONS

'''

'''
def getFileLogger(logDir, logFileName, name='file_logger', level=20):
    import logging
    #print(level)
    loglevel = None
    if level == 10: # DEBUG
        loglevel = logging.DEBUG;
    elif level == 20: # INFO
        loglevel = logging.INFO;
    elif level == 30: # WARNING
        loglevel = logging.WARNING;
    elif level == 40: # ERROR
        loglevel = logging.ERROR;
    elif level == 50: # CRITICAL
        loglevel = logging.CRITICAL;
    else:
        loglevel = logging.DEBUG;
        
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(level)
        
        # logging file handler
        fh = logging.FileHandler(f'{logDir}{logFileName}.log')
        fh.setLevel(logging.DEBUG)
        
        # create console handler with higher level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # create formatter and add it to the handlers
        file_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        console_formatter = logging.Formatter('%(message)s')
        
        fh.setFormatter(file_formatter)
        ch.setFormatter(console_formatter)
        
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        
        # add the handler to the root logger
        #logging.getLogger('').addHandler(ch)
        
        logger.handler_set = True
    return logger

#--------------------------------------------------------------------#

'''

'''
##------------------------------------------------------------------------
# Generate Feature Vector
# Steps:
#    1: skip header
#    2: replace all chars that are not [a-zA-Z] with whitespace
#    3: lowercase all remaining chars
#    4: break text into token by whitespace, each token becomes a feature
#    5: calculate value of a feature; which is the number of occurrences of the token in input_file
# return tuple (instanceName targetLabel featureVector)
##------------------------------------------------------------------------
def generateFeatureVector(input_ex, classLabel):
    import re
    from collections import Counter, OrderedDict
    
    outFeatureVector = Counter()
    instanceName = input_ex.split("/")[-1]
    targetLabel = classLabel
    
    
    #open and readin input file
    with open(input_ex,'rb') as in_f:
        inputExLines = in_f.readlines()
    if isTest: print("Instance Name:[{0}], TargetLabel:[{1}] Total lines in inputExLines file:[{2}]".format(instanceName,classLabel,len(inputExLines)))
    
    #get index, skip header
    lineIndex = 0
    for line in inputExLines:
        if not line == b'\n':
            lineIndex += 1
            continue
        else:
            break
        
    lines = inputExLines[lineIndex+1:] #skip header
    if isTest: print("non-header lines count:[{0}]".format(len(lines)))
    
    #replace all characters that are not [a-zA-Z] with whitespace
    lines = [ re.sub(b'[^a-zA-Z]',b' ',l) for l in lines]
    #lowercase all remaining char
    lines = [l.lower() for l in lines]
    #break text into token by whitespace - each token is a feature
    tokLines = [ re.split(b'\\s+',l) for l in lines]
    for t in tokLines:
        tokens = [e.decode() for e in t]
        while True:
            if '' in tokens:
                tokens.remove('')
            else:
                break
            
        #calculate feature value - frequency of occurances
        outFeatureVector.update(Counter(tokens))
        
    fv = OrderedDict(sorted(outFeatureVector.items()))
    
    return instanceName, targetLabel, fv

##------------------------------------------------------------------------
# Generate a WordCloud Visualization
# Steps:
#    1: 
# return ...
##------------------------------------------------------------------------
def wordcloud_draw(data, color='black', width=1000, height=750, max_font_size=50, max_words=100):
    import matplotlib.pyplot as plt #2D plotting
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    
    words = ' '.join([word for word in data])
    #cleaned_word = " ".join([word for word in words])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                    background_color=color,
                    width=width,
                    height=height,
                    max_font_size=max_font_size,
                    max_words=max_words,
                     ).generate(words)
    plt.figure(1,figsize=(10.5, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


##################################################################################################################
# File IO - Helper Functions - Gets the Language Model file locations
##################################################################################################################
def getFilesFromPath(path,FILE_SUFFIX):
    import os
    
    langMap = {}
    langModels = []
    
    for dirpath, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, "*"+FILE_SUFFIX):
            langModels.append({filename.split('.')[0]:dirpath+'/'+filename})
    
    return langModels    


##################################################################################################################
# Helper Functions - Remove punctuation
##################################################################################################################
def removePunctuation(sent,PUNCT):
    identifier = sent.split('\t')[0]
    text = sent.split('\t')[1]
    tokens = text.split()
   
    words = []
    
    for token in tokens:
        newChars = []
        for chr in token:
            if chr in PUNCT:
                newChars.append('')
            else:
                newChars.append(chr)
                
        words.append(''.join(newChars))
    return identifier,words


##################################################################################################################
# Function: Utility function to clean the document of all non words (i.e. punctuation, symbols, digits)
##################################################################################################################
def cleanNonWordChars(doc):
    if isTest: print("Entering.cleanNonWordChars; Cleaning Document")
    if isTest: outfile = open('outputNonWordsClean.txt','a')
    
    docWords = []
    #Remove non-words
    doc = re.sub(r"([a-zA-Z]+[0-9]+)|([0-9]+[a-zA-Z]+)|(&[a-zA-Z]+)|(\w+(-\w+)+)|([a-zA-Z])(\.[a-zA-Z])+\.?",'',doc)
    if isTest: outfile.write(doc); outfile.write('\n') 
    
    #Create pattern to extract words with apostrophies
    wordsPatternWithApostrophe = re.compile(r"[a-zA-Z]+'?[a-zA-Z]+")

    words = re.findall(wordsPatternWithApostrophe, doc)
    
    #Convert all words to lowercase
    docWords = [x.lower() for x in words]
    if isTest: outfile.write(str(docWords)); outfile.write('\n')
    
    
    if isTest: print("Exiting.cleanNonWordChars; Returning:")
    return docWords
##------------------------------------------------------------------------

##------------------------------------------------------------------------
# Util Function, update dictionary used for storing count values
##------------------------------------------------------------------------      
def updateDictCount(key,dict):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1
##------------------------------------------------------------------------



