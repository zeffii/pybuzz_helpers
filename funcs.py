import sys

lib_origin = r'C:\Python24\Lib'
if not (lib_origin in sys.path):
    sys.path.append(lib_origin)

import random

def hex_to_int(hex_val):
    hex_val = str(hex_val) # just in case
    return int("0x" + hex_val, 0)

def seq_sample_from(items, tick):
    num_items = len(items)
    return items[tick % num_items]

def random_choice(items):
    index = random.randint(0, len(items)-1)
    return items[index]

def random_choice_wdict(weighted_dict):
    '''weights will automatically be normalized to total 1.0'''
    summed_weights = sum(weighted_dict.values())
    random_float = random.random() * summed_weights
    lower = 0.0
    last_item = None

    # using sorted to keep the order stable
    for k, v in sorted(weighted_dict.items()):
        higher = lower + v
        if random_float >= lower and random_float < higher:
            return k
        lower += v
        last_item = k

    return k

def utrk_mixin(SPCC):

    def utrk9p(trk=0, offset=None, note=None, smp=None, vol=None, pan=None, p1=None, p1val=None, p2=None, p2val=None):
        ''' 
        UTRK communication function, expects assignments of:

            [offset, note, sample, vol, pan, param1, param1_val, param2, param_val]
            ....     ...   ..      ..   ..   ..      ....        ..      ....

        '''
        for assignment_idx, param in enumerate([offset, note, smp, vol, pan, p1, p1val, p2, p2val]):
            if not (param is None): 
                SPCC(assignment_idx, trk, param)

    return utrk9p

