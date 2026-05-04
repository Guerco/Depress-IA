# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:42:46 2026

@author: BIEL
"""

from transformers import pipeline

preenchedor = pipeline('fill-mask', model='roberta-base')
resultado = preenchedor("Eu gosto de <mask>.")
print(resultado)