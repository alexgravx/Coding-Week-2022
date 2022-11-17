## Importations ##

from projet_w2.InsultBlock.insult_detector.detecteur_v1 import detecteur_v1
from projet_w2.InsultBlock.insult_detector.detecteur_v2 import detecteur_v2
from projet_w2.InsultBlock.insult_detector.detecteur_v3 import detecteur_v3
from projet_w2.InsultBlock.insult_detector.cas_particuliers import insulte_cachee

## Fonctions ##


def detecteur(text):
    if detecteur_v1(text) or detecteur_v2(text) or detecteur_v3(text) or insulte_cachee(text):
        return True
    return False

## Test ##


def test_detecteur():
    bool = detecteur('test')
    assert bool != None
