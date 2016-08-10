import sys

lib_origin = r'C:\Python24\Lib'
if not (lib_origin in sys.path):
    sys.path.append(lib_origin)

import random

def format_params(params):
    return [(params[i], params[i+1]) for i in range(0, len(params)-1, 2)]

def format3_params(params):
    return [(params[i], params[i+1], params[i+2]) for i in range(0, len(params)-1, 3)]

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
        last_item = k
        if random_float >= lower and random_float < higher:
            return last_item
        lower += v

    return last_item

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

def assign_utrk9(buzz, name, start_index, params):
    utrk1 = buzz.GetMachine(name)
    params = format_params(params)
    for idx, (k, v) in enumerate(params):
        peerCtrlIndex = idx + start_index
        buzz.SetPeerCtrlTarget(peerCtrlIndex, utrk1, 2, v)
        buzz.SetPeerCtrlName(peerCtrlIndex, k)
        print(idx, k, v)

    return utrk_mixin(buzz.SendPeerCtrlChange)

def pbseq(triggers):
    '''
    input: "1...1...1...1...1..."
    output: [0,4,8,12,16]
    '''
    return [idx for idx, k in enumerate(list(triggers)) if not k == '.']

def pbseq_func(triggers, behaviours, tick, wrap_around=True):
    '''
    input: 
        triggers="1...2...b...1...2..."
        behaviours={
            # trigger id: return value 
            '1': 0, '2': 4, 'b': 20 }
    output: [0,None, None, None, 4, . . . 20, . . .0, . . . 4]
    # use for volumes / offsets / panning / sample_idx
    returns the value associated with the key, or None if not listed.
    '''
    list_triggers = list(triggers)
    if wrap_around:
        item = list_triggers[tick % len(list_triggers)]
        return behaviours.get(item)
    else:
        if tick < len(list_triggers):
            item = list_triggers[tick]
            return behaviours.get(item)
    return None


class Assign_Greenmilk:

    def __init__(self, buzz, name, start_index, params):
        self.machine_name = buzz.GetMachine(name)
        self.params = format3_params(params)
        self.lookups = {}
        self.buzz = buzz
        
        # assign all necessary slots and make lookup-table.
        for idx, (group, k, v) in enumerate(self.params):
            peerCtrlIndex = idx + start_index
            self.buzz.SetPeerCtrlTarget(peerCtrlIndex, self.machine_name, group, v)
            self.buzz.SetPeerCtrlName(peerCtrlIndex, k)
            print(peerCtrlIndex, group, k, v)
            self.lookups[k] = peerCtrlIndex


    def greenmilk(self, **params):
        trk = params.get('trk', 2)  # global params ignore this?

        for param_name, param_value in params.items():
            if param_name == 'trk':
                continue
            peerCtrlIndex = self.lookups[param_name]
            self.buzz.SendPeerCtrlChange(peerCtrlIndex, trk, param_value)
