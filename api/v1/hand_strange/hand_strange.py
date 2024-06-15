from typing import List

from  api.v1.hand_strange.models.session import Session

from pkengine.funcs import find_combs
from pkengine.card import Card

import asyncio
from fastapi import APIRouter, Request

router = APIRouter()

def get_winers(session):
    hands = {hand.user_id:[Card(s = card.suit, v = card.value) for card in hand.cards] for hand in session.hands}
    table = [Card(s = card.suit, v = card.value) for card in session.table.cards]
    combs = {uid:find_combs(hands[uid] + table, ['C', 'D', 'H', 'S'], ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']) for uid in hands}

    winers = sorted(combs, key = lambda x: combs[x], reverse = True)

    equal = []
    for i in winers[1:]:
        if combs[winers[0]] == combs[i]:
            equal += [i]

    if equal != []: equal = [winers[0]] + equal

    return {'id':session.id, 'winers':winers, 'equal':equal}

@router.post('/api/v1/hand_strange')
async def test(sessions: List[Session], request : Request):
    
    result = [None for i in range(len(sessions))]

    loop = asyncio.get_running_loop()
    for c_s, session in enumerate(sessions):
        result[c_s] = await loop.run_in_executor(request.app.state.executor, get_winers, session)

    return result