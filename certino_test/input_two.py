from typing import Generator


def calc_valid_strings(lines: Generator) -> int:
    n_valid_strings = 0
    for line in lines:
        low_high_occurances, character, sentence = line.replace(":", " ").split()
        lowest_occur, highest_occur = [int(x) for x in low_high_occurances.split("-")]
        if lowest_occur <= sentence.count(character) <= highest_occur:
            n_valid_strings += 1

    return n_valid_strings


def calc_valid_positions(lines: Generator) -> int:
    n_valid_strings = 0
    for line in lines:
        positions, character, sentence = line.replace(":", " ").split()
        positions: list = [int(index) for index in positions.split("-")]
        n_positions = []
        for idx, c in enumerate(sentence, 1):
            if c == character:
                n_positions.append(idx)

        if len(n_positions) == 1 and n_positions[0] in positions:
            n_valid_strings += 1

    return n_valid_strings
