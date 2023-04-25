from lib.class_challenge import *


def test_grammar_stats():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Life is beautiful.") == True
    assert grammar_stats.check("Life is beautiful.") == True
    assert grammar_stats.check("life is beautiful") == False
    assert grammar_stats.check("life is beautiful") == False
    assert grammar_stats.check("life is beautiful") == False
    assert grammar_stats.check("life is beautiful") == False
    assert grammar_stats.check("life is beautiful") == False
    assert grammar_stats.check("life is beautiful") == False
    assert grammar_stats.check("Life is beautiful.") == True
    assert grammar_stats.check("Life is beautiful.") == True
    assert grammar_stats.percentage_good() == 40