from itertools import groupby
'''
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
for keys, groups in groupby(things, lambda x:x[0]):
    print(keys)
    print(list(groups))
    for things in groups:
        print(things)
'''
from operator import itemgetter
a = ["cat","dog","cow","tiger","lion","Fox","Shark","Snake","turtle","mouse","monkey","bear"]
for letters, words in groupby(sorted(a),key=itemgetter(0)):
    print(letters)
    # print(list(words))
    for i in words:
        print(i)