from pkengine.card import Card

from pkengine.combination import Combination

from pkengine.combination import HighCard
from pkengine.combination import Pair
from pkengine.combination import TwoPair
from pkengine.combination import Set
from pkengine.combination import Streat
from pkengine.combination import Flash
from pkengine.combination import FullHouse
from pkengine.combination import Kare
from pkengine.combination import StreatFlash
from pkengine.combination import FlashRoyal

def find_combs(hand, suits, values):
    
    suits_dict = {i:[] for i in suits}
    val_sorted_dict = {i:[] for i in values}
    
    suits_counts = {i:0 for i in suits}
    val_sorted_counts = {i:0 for i in values}

    for card in hand:
        suits_dict[card.suit] += [card]
        val_sorted_dict[card.value] += [card]
        
        suits_counts[card.suit] += 1
        val_sorted_counts[card.value] += 1

    combinations = {i:[] for i in ['Pair', 'TwoPair', 'Set', 'Streat', 'Flash', 'FullHouse', 'Kare', 'StreatFlash', 'FlashRoyal']}

    sorted_hand = sorted(hand, reverse = True)

    streat_counter = 0

    last_key = list(val_sorted_dict.keys())[-1]
    for i in val_sorted_dict:

        if val_sorted_counts[i] == 2:
            kicker = []
            for card in sorted_hand:
                if card not in val_sorted_dict[i]:
                    kicker += [card]

            combinations['Pair'] += [Pair(val_sorted_dict[i], kicker[:3])]

        if val_sorted_counts[i] == 3:
            kicker = []
            for card in sorted_hand:
                if card not in val_sorted_dict[i]:
                    kicker += [card]

            combinations['Set'] += [Set(val_sorted_dict[i], kicker[:2])]

        if val_sorted_counts[i] == 4:
            kicker = []
            for card in sorted_hand:
                if card not in val_sorted_dict[i]:
                    kicker += [card]

            combinations['Kare'] += [Kare(val_sorted_dict[i], kicker[:1])]


        if val_sorted_counts[last_key] != 0 and val_sorted_counts[i] != 0:
            streat_counter += 1
        else:
            streat_counter = 0

        if streat_counter >= 4:
            combinations['Streat'] += [Streat(val_sorted_dict[i][0], [])]

        last_key = i

    for i in suits_dict:
        if suits_counts[i] >= 5:
            combinations['Flash'] += [Flash(max(suits_dict[i]), [])]

    if len(combinations['Pair']) > 1:
        sorted_pairs = sorted(combinations['Pair'], reverse = True)
        vals = [sorted_pairs[0].high_card, sorted_pairs[1].high_card]
        
        kicker = []
        for i in sorted_hand:
            if i not in kicker:
                kicker += [i]
                
        combinations['TwoPair'] += [TwoPair(sorted_pairs[0].high_card, sorted_pairs[1].high_card, kicker[:1])]

    if len(combinations['Pair']) >= 1 and len(combinations['Set']) >= 1 :
        sorted_pairs = sorted(combinations['Pair'], reverse = True)
        sorted_sets = sorted(combinations['Set'], reverse = True)
        
        combinations['FullHouse'] += [FullHouse(sorted_sets[0].high_card, sorted_pairs[0].high_card, [])]

    if len(combinations['Streat']) >= 1 and len(combinations['Flash']) >= 1 :
        for i in suits_dict:
            if suits_counts[i] < 5: continue
                
            val_suit_sorted_dict = {j:[] for j in values}
            for card in hand:
                val_suit_sorted_dict[card.value] += [card]
                
            last_key = list(val_suit_sorted_dict.keys())[-1]
            streat_count = 0
            for j in val_suit_sorted_dict:
                if val_sorted_counts[last_key] != 0 and val_sorted_counts[j] != 0:
                    streat_counter += 1
                else:
                    streat_counter = 0

                if streat_counter >= 4:
                    if val_suit_sorted_dict[j][0].value != 'A':
                        combinations['StreatFlash'] += [StreatFlash(val_suit_sorted_dict[j][0], [])]
                    else:
                        combinations['FlashRoyal'] += [FlashRoyal(val_suit_sorted_dict[j][0], [])]

                last_key = j
                
    c = []
    for i in combinations.values():
        if len(i) != 0:
            for j in i:
                c += [j]
                
    if len(c) == 0:
        c += [HighCard(sorted_hand[0], sorted_hand[1:5])]
    
    return max(c)