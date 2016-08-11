# -*- coding: utf-8 -*-
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# These scales are taken from Supercollider's scales file/dict

distances = {
    
    # TWELVE TONES PER OCTAVE
    'minorPentatonic': ([0,3,5,7,10], 12),
    'majorPentatonic': ([0,2,4,7,9], 12),

    'ritusen': ([0,2,5,7,9], 12),
    'egyptian': ([0,2,5,7,10], 12),

    'kumoi': ([0,2,3,7,9], 12),
    'hirajoshi': ([0,2,3,7,8], 12),
    'iwato': ([0,1,5,6,10], 12),
    'chinese': ([0,4,6,7,11], 12),
    'indian': ([0,4,5,7,10], 12),
    'pelog': ([0,1,3,7,8], 12),

    'prometheus': ([0,2,4,6,11], 12),
    'scriabin': ([0,1,4,7,9], 12),

    # 6 note scales
    'whole': ([0,2,4,6,8,10], 12),
    'augmented': ([0,3,4,7,8,11], 12),
    'augmented2': ([0,1,4,5,8,9], 12),

    # Partch's Otonalities and Utonalities
    'partch_o1': ([0,8,14,20,25,34], 43),
    'partch_o2': ([0,7,13,18,27,35], 43),
    'partch_o3': ([0,6,12,21,29,36], 43),
    'partch_o4': ([0,5,15,23,30,37], 43),
    'partch_o5': ([0,10,18,25,31,38], 43),
    'partch_o6': ([0,9,16,22,28,33], 43),
    'partch_u1': ([0,9,18,23,29,35], 43),
    'partch_u2': ([0,8,16,25,30,36], 43),
    'partch_u3': ([0,7,14,22,31,37], 43),
    'partch_u4': ([0,6,13,20,28,38], 43),
    'partch_u5': ([0,5,12,18,25,33], 43),
    'partch_u6': ([0,10,15,21,27,34], 43),

    # hexatonic modes with no tritone
    'hexMajor7': ([0,2,4,7,9,11], 12),
    'hexDorian': ([0,2,3,5,7,10], 12),
    'hexPhrygian': ([0,1,3,5,8,10], 12),
    'hexSus': ([0,2,5,7,9,10], 12),
    'hexMajor6': ([0,2,4,5,7,9], 12),
    'hexAeolian': ([0,3,5,7,8,10], 12),

    # 7 note scales
    'major': ([0,2,4,5,7,9,11], 12),
    'ionian': ([0,2,4,5,7,9,11], 12),
    'dorian': ([0,2,3,5,7,9,10], 12),
    'phrygian': ([0,1,3,5,7,8,10], 12),
    'lydian': ([0,2,4,6,7,9,11], 12),
    'mixolydian': ([0,2,4,5,7,9,10], 12),
    'aeolian': ([0,2,3,5,7,8,10], 12),
    'minor': ([0,2,3,5,7,8,10], 12),
    'locrian': ([0,1,3,5,6,8,10], 12),

    'harmonicMinor': ([0,2,3,5,7,8,11], 12),
    'harmonicMajor': ([0,2,4,5,7,8,11], 12),

    'melodicMinor': ([0,2,3,5,7,9,11], 12),
    'melodicMinorDesc': ([0,2,3,5,7,8,10], 12),
    'melodicMajor': ([0,2,4,5,7,8,10], 12),

    'bartok': ([0,2,4,5,7,8,10], 12),
    'hindu': ([0,2,4,5,7,8,10], 12),

    # raga modes
    'todi': ([0,1,3,6,7,8,11], 12),
    'purvi': ([0,1,4,6,7,8,11], 12),
    'marva': ([0,1,4,6,7,9,11], 12),
    'bhairav': ([0,1,4,5,7,8,11], 12),
    'ahirbhairav': ([0,1,4,5,7,9,10], 12),

    'superLocrian': ([0,1,3,4,6,8,10], 12),
    'romanianMinor': ([0,2,3,6,7,9,10], 12),         
    'hungarianMinor': ([0,2,3,6,7,8,11], 12),
    'neapolitanMinor': ([0,1,3,5,7,8,11], 12),
    'enigmatic': ([0,1,4,6,8,10,11], 12),
    'spanish': ([0,1,4,5,7,8,10], 12),

    # modes of whole tones with added note ->
    'leadingWhole': ([0,2,4,6,8,10,11], 12),
    'lydianMinor': ([0,2,4,6,7,8,10], 12),
    'neapolitanMajor': ([0,1,3,5,7,9,11], 12),
    'locrianMajor': ([0,2,4,5,6,8,10], 12),

    # 8 note scales
    'diminished': ([0,1,3,4,6,7,9,10], 12),
    'diminished2': ([0,2,3,5,6,8,9,11], 12),

    # maqam ajam
    'ajam': ([0,4,8,10,14,18,22], 24),
    'jiharkah': ([0,4,8,10,14,18,21], 24),
    'shawqAfza': ([0,4,8,10,14,16,22], 24),

    # maqam sikah
    'sikah': ([0,3,7,11,14,17,21], 24),
    'sikahDesc': ([0,3,7,11,13,17,21], 24),
    'huzam': ([0,3,7,9,15,17,21], 24),
    'iraq': ([0,3,7,10,13,17,21], 24),
    'bastanikar': ([0,3,7,10,13,15,21], 24),
    'mustar': ([0,5,7,11,13,17,21], 24),

    # maqam bayati
    'bayati': ([0,3,6,10,14,16,20], 24),
    'karjighar': ([0,3,6,10,12,18,20], 24),
    'husseini': ([0,3,6,10,14,17,21], 24),

    # maqam nahawand
    'nahawand': ([0,4,6,10,14,16,22], 24),
    'nahawandDesc': ([0,4,6,10,14,16,20], 24),
    'farahfaza': ([0,4,6,10,14,16,20], 24),
    'murassah': ([0,4,6,10,12,18,20], 24),
    'ushaqMashri': ([0,4,6,10,14,17,21], 24),

    # maqam rast
    'rast': ([0,4,7,10,14,18,21], 24),
    'rastDesc': ([0,4,7,10,14,18,20], 24),
    'suznak': ([0,4,7,10,14,16,22], 24),
    'nairuz': ([0,4,7,10,14,17,20], 24),
    'yakah': ([0,4,7,10,14,18,21], 24),
    'yakahDesc': ([0,4,7,10,14,18,20], 24),
    'mahur': ([0,4,7,10,14,18,22], 24),

    # maqam hijaz
    'hijaz': ([0,2,8,10,14,17,20], 24),
    'hijazDesc': ([0,2,8,10,14,16,20], 24),
    'zanjaran': ([0,2,8,10,14,18,20], 24),

    # maqam hijazKar
    'zanjaran': ([0,2,8,10,14,16,22], 24),

    # maqam saba
    'saba': ([0,3,6,8,12,16,20], 24),
    'zamzam': ([0,2,6,8,14,16,20], 24),

    # maqam kurd
    'kurd': ([0,2,6,10,14,16,20], 24),
    'kijazKarKurd': ([0,2,8,10,14,16,22], 24),

    # maqam nawa Athar
    'nawaAthar': ([0,4,6,12,14,16,22], 24),
    'nikriz': ([0,4,6,12,14,18,20], 24),

    # Ascending/descending scales
    'melodicMinor': ([0,2,3,5,7,9,11], 12),
    'sikah': ([0,3,7,11,14,17,21], 24),
    'nahawand': ([0,4,6,10,14,16,22], 24)
}

def make_chord(base, scale, intervals):
    '''
    takes intervals = [0,1,1,1,2]
    numbers in intervals represent num of allowed distances to jump from the previous note.
    '''
    dist, total_distance = scale
    
    outmix = []
    for i in range(6):
        outmix.extend([j + (i*total_distance) for j in dist])
    
    cpts = []
    last_index = 0
    for i in intervals:
        last_index += i
        cpts.append(base + outmix[last_index])
    
    return cpts

