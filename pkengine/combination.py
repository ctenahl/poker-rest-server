class Combination:
    def __init__(self, hc, kicker):
        self.high_card = hc
        self.kicker = kicker
    
    #@functools.lru_cache
    def __eq__(self, other): # ==
        if self.strange == other.strange and self.high_card == other.high_card and self.kicker == other.kicker:
            return True

        return False
    
    def __lt__(self, other): # <
        if self.strange < other.strange:
            return True
        
        elif self.strange == other.strange and self.high_card < other.high_card:
            return True
        
        elif self.strange == other.strange and self.high_card == other.high_card and self.kicker != []:
            if self.kicker < other.kicker:
                return True

        return False
        
class HighCard(Combination):
    strange = 0

class Pair(Combination):
    strange = 1

class TwoPair(Combination):
    strange = 2
    
    def __init__(self, hc, lc, kicker):
        self.high_card = hc
        self.low_card = lc
        self.kicker = kicker
        
    def __lt__(self, other): # <
        if self.strange < other.strange:
            return True
        
        elif self.strange == other.strange and self.high_card < other.high_card:
            return True
        
        elif self.strange == other.strange and self.high_card == other.high_card and self.low_card < other.low_card:
            return True
        
        elif self.strange == other.strange and self.high_card == other.high_card and self.low_card == other.low_card and self.kicker != []:
            if self.kicker < other.kicker:
                return True

        return False

class Set(Combination):
    strange = 3

class Streat(Combination):
    strange = 4

class Flash(Combination):
    strange = 5

class FullHouse(Combination):
    strange = 6
    
    def __init__(self, hc, lc, kicker):
        self.high_card = hc
        self.low_card = lc
        self.kicker = kicker
        
    def __lt__(self, other): # <
        if self.strange < other.strange:
            return True
        
        elif self.strange == other.strange and self.high_card < other.high_card:
            return True
        
        elif self.strange == other.strange and self.high_card == other.high_card and self.low_card < other.low_card:
            return True

        return False

class Kare(Combination):
    strange = 7

class StreatFlash(Combination):
    strange = 8

class FlashRoyal(Combination):
    strange = 9