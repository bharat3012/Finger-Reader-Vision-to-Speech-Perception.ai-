#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:00:16 2019

@author: bharat
"""

from gtts.gtts import tts
from tts import gTTS

def speech(tex, lan):
    tts = gTTS(text=tex, lang= lan)
    tts.save("first.mp3")