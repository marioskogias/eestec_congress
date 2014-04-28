# -*- coding: utf-8 -*-
from models import Participant
import codecs

def load():
    """Read from csv and add to database"""
    with codecs.open('participants.csv', 'r', 'utf-8') as f:
        for line in f:
            line = unicode(line)
            try:
                data = line.split(',')
                lc = str(data[0])
                name = str(data[1])
                surname = str(data[2])
                new_part = Participant(first_name=name,
                                       last_name=surname, lc=lc)
                new_part.save()
            except:
                print line
