from laxleague.src.laxleague.player import Player
from laxleague.src.laxleague.guardian import Guardian

def test_construction():
    p = Player('Tatiana', 'Jones')
    assert 'Tatiana' == p.first_name
    assert 'Jones' == p.last_name
    assert [] == p.guardians

def test_add_guardian():
    g = Guardian('Mary', 'Jones')
    p = Player('Tatiana', 'Jones')
    p.add_guardian(g)
    assert  [g] == p.guardians

