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


