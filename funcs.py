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

def random_choice_w(items_w_weights):
    pass

def utrk9p(trk=0, offset=None, note=None, smp=None, vol=None, pan=None, p1=None, p1val=None, p2=None, p2val=None):
    ''' 
    UTRK communication function, expects assignments of:

        [offset, note, sample, vol, pan, param1, param1_val, param2, param_val]
        ....     ...   ..      ..   ..   ..      ....        ..      ....

    '''
    for assignment_idx, param in enumerate([offset, note, smp, vol, pan, p1, p1val, p2, p2val]):
        if not (param is None): 
            SendPeerCtrlChange(assignment_idx, trk, param)
