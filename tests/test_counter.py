from lib.counter import *

def test_the_count():
    counter = Counter()
    counter.add(7)
    result = counter.report()
    assert result == f"Counted to 7 so far."
