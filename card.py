suits = ["heart", "spade", "diamond", "club", "wild"]

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

face_cards = {
    "J": 11,
    "Q": 12,
    "K": 13,
    11: "J",
    12: "Q",
    13: "K"
}

ace_is_high = True
if ace_is_high:
    values.insert(0, 1)
    face_cards["ace"] = 1
else:
    values.append(14)
    face_cards["ace"] = 14


class Card:
    def __init__(self, aSuit, aValue):
        if aSuit in suits:
            self.suit = aSuit
        else:
            raise Exception(
                f"Attempted to create a card with suit:{aSuit} not in suits:{suits}")

        if aValue in values:
            self.value = aValue
        else:
            raise Exception(
                f"Attempted to create a card with value:{aValue} not in values:{values}")
