class Card:
    def __init__(self, s, v):
        true_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        true_suits = ['C', 'D', 'H', 'S']
        
        v = str(v)
        
        if s not in true_suits:
            raise ValueError
            
        if v not in true_values:
            raise ValueError
        
        self.name = s + '_' + v
        
        self.suit = s
        self.value = v
        self.value_strange = true_values.index(v)
    
    #@functools.lru_cache
    def __eq__(self, other): # ==
        if self.value_strange == other.value_strange: 
            return True
        return False
    
    def __lt__(self, other): # <
        if self.value_strange < other.value_strange: 
            return True
        return False
    
    def __le__(self, other): # <=
        if self.value_strange <= other.value_strange: 
            return True
        return False
    
    def __str__(self):
        return self.name