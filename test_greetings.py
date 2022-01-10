from greetings import determine_saying
import pytest

def test_determine_saying():
    # test morning times. (7am <= t < 11am.)
    time = 7
    assert determine_saying(time) == "morning"
    time = 8
    assert determine_saying(time) == "morning"
    time = 9
    assert determine_saying(time) == "morning"
    time = 11
    assert determine_saying(time) == "morning"

    # test afternoon times (noon <= t < 5pm)
    time = 12
    assert determine_saying(time) == "afternoon"
    time = 15
    assert determine_saying(time) == "afternoon"
    time = 16
    assert determine_saying(time) == "afternoon"

    # test evening times (5pm <= t < 7pm)
    time = 17
    assert determine_saying(time) == "evening"
    time = 18
    assert determine_saying(time) == "evening"

    # test night times (7pm <= t < 7am)
    time = 19
    assert determine_saying(time) == "night"
    time = 20
    assert determine_saying(time) == "night"
    time = 21
    assert determine_saying(time) == "night"
    time = 24
    assert determine_saying(time) == "night"
    time = 0
    assert determine_saying(time) == "night"
    time = 1
    assert determine_saying(time) == "night"
    time = 6

    



    pass

pytest.main(["-v", "--tb=line", "-rN", __file__])