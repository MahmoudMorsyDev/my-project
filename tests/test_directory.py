from lib.gratitudes import *

def test_directory():
    gratit = Gratitudes()
    gratit.add("Life")
    gratit.add("God")
    result = gratit.format()
    assert result == "Be grateful for: Life, God"

