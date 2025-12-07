def shift_char(char, shift):
    span = 126 - 32 + 1
    idx = (ord(char) + shift) % span
    if idx < 32:
        return chr(idx + span)
    else:
        return chr(idx)
