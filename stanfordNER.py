#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:32:59 2017

@author: Santhosh
"""
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/Users/santhosh/PythonProjects/santhosh2129-RestAPI/stanford/classifiers/english.conll.4class.distsim.crf.ser.gz',
					   '/Users/santhosh/PythonProjects/santhosh2129-RestAPI/stanford/stanford-ner.jar',
					   encoding='utf-8')


def performIdentification(inText):
    tokenized_text = word_tokenize(inText)
    classified_text = st.tag(tokenized_text)
    return classified_text