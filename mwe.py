# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 09:36:33 2022

@author: maria
"""
from neuron import h
h.load_file("stdlib.hoc")
h.load_file("nrngui.hoc")

def check():
    mt = h.MechanismType(1)
    mname  = h.ref('')
    for i in range(mt.count()):
        mt.select(i)
        mt.selected(mname)
        if mname[0] == 'ostim':
            return "Good"
    return "Nope"
    
soma = h.Section(name='soma')

testpp = h.ostim(0.5)