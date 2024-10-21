def get_camelot_key(pitch_class, mode):
    """
    Convert pitch class and mode to Camelot key
    """
    return {
        0: {1: "8B", 0: "5A"},
        1: {1: "3B", 0: "12A"},
        2: {1: "10B", 0: "7A"},
        3: {1: "5B", 0: "2A"},
        4: {1: "12B", 0: "9A"},
        5: {1: "7B", 0: "4A"},
        6: {1: "2B", 0: "11A"},
        7: {1: "9B", 0: "6A"},
        8: {1: "4B", 0: "1A"},
        9: {1: "11B", 0: "8A"},
        10: {1: "6B", 0: "3A"},
        11: {1: "1B", 0: "10A"},
    }[pitch_class][mode]
