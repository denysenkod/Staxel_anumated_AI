#PHONEME_TO_VISEME_10 = {
#    # Silence
#    '': 'Neutral', 'SIL': 'Neutral', 'PAU': 'Neutral', '.': 'Neutral',
#
#    # A
#    'AA': 'A', 'AH': 'A',
#
#    # E
#    'IY': 'E', 'IH': 'E', 'EH': 'E', 'EY': 'E',
#
#    # O
#    'OW': 'O', 'AO': 'O',
#
#    # U
#    'UW': 'U', 'UH': 'U',
#
#    # FV
#    'F': 'FV', 'V': 'FV',
#
#    # MBP
#    'M': 'MBP', 'B': 'MBP', 'P': 'MBP',
#
#    # WQ
#    'W': 'WQ', 'R': 'WQ', 'L': 'WQ', 'Y': 'WQ', 'ER': 'WQ',
#
#    # TH
#    'TH': 'TH', 'DH': 'TH',
#
#    # S
#    'S': 'S', 'Z': 'S', 'SH': 'S', 'CH': 'S', 'JH': 'S', 'ZH': 'S',
#}

PHONEME_TO_VISEME_10 = {
    "AA": "A", "AA0": "A", "AA1": "A", "AA2": "A",
    "AE": "A", "AE0": "A", "AE1": "A", "AE2": "A",
    "AH": "A", "AH0": "A", "AH1": "A", "AH2": "A",
    "AO": "O", "AO0": "O", "AO1": "O", "AO2": "O",
    "AW": "O", "AW1": "O", "AW2": "O",
    "AY": "AI", "AY0": "AI", "AY1": "AI", "AY2": "AI",
    "B": "MBP",
    "CH": "CH",
    "D": "DNT",
    "DH": "TH",
    "EH": "E", "EH0": "E", "EH1": "E", "EH2": "E",
    "ER": "R", "ER0": "R", "ER1": "R", "ER2": "R",
    "EY": "E", "EY0": "E", "EY1": "E", "EY2": "E",
    "F": "FV",
    "G": "GK",
    "HH": "Neutral",  # NEW: mapped to something mild — breathy, almost no lip motion
    "IH": "E", "IH0": "E", "IH1": "E", "IH2": "E",
    "IY": "E", "IY0": "E", "IY1": "E", "IY2": "E",
    "JH": "CH",
    "K": "GK",
    "L": "L",
    "M": "MBP",
    "N": "DNT",
    "NG": "DNT",
    "OW": "O",
    "OY": "O",
    "P": "MBP",
    "R": "R",
    "S": "SH",      # sibilant, grouped with SH for visual similarity
    "SH": "SH",
    "T": "DNT",
    "TH": "TH",
    "UH": "U", "UH0": "U", "UH1": "U", "UH2": "U",
    "UW": "U", "UW0": "U", "UW1": "U", "UW2": "U",
    "V": "FV",
    "W": "WQ",
    "Y": "E",
    "Z": "SH",
    "ZH": "SH",

    # Punctuation or unknowns
    ".": "Neutral",
    "!": "Neutral",
    "?": "Neutral",
}


def phonemes_to_viseme_timeline(phoneme_timeline):
    viseme_timeline = []

    def map_phoneme(phoneme):
        phoneme = phoneme.upper().strip("0123456789")
        return PHONEME_TO_VISEME_10.get(phoneme, 'Neutral')  # Default to 'Neutral' for unknowns

    last_viseme = None
    viseme_start = None
    viseme_end = None

    for phoneme, start, end in phoneme_timeline:
        viseme = map_phoneme(phoneme)

        if viseme == last_viseme:
            viseme_end = end  # Extend
        else:
            if last_viseme is not None:
                viseme_timeline.append((last_viseme, viseme_start, viseme_end))
            last_viseme = viseme
            viseme_start = start
            viseme_end = end

    if last_viseme is not None:
        viseme_timeline.append((last_viseme, viseme_start, viseme_end))

    return viseme_timeline