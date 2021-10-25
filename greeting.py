# -*- coding: utf-8 -*-
"""
This module provides greeting in Chichewa and Tumbuka
"""

def mwadzuka(name):
    """Morning greeting in Chichewa"""
    print("Mwadzuka bwanji " +name +"?")
    
    
def mwatandala(nganya):
    """ Afternoon greeting in Tumbuka Language"""
    print("Mwatandala uli " +nganya +"?")

user = input("Chonde lowetsani dzina lanu:  ")
    
mwadzuka(user)
mwatandala(user)