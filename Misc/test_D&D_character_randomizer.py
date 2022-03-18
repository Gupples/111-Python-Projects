from DND_character_randomizer import roll_dice, validate_stat_rolls, get_race
from DND_character_randomizer import get_class, get_background, get_stat_array
import pytest

def test_roll():
    for _ in range(100):
        roll = roll_dice()
        assert roll > 0 and roll <= 20

def test_validate_stat_rolls():
    # Test invalid roll (total of 66)
    rolls = [11, 11, 11, 11, 11, 11]
    info = validate_stat_rolls(rolls)
    is_valid = info[0]
    roll_total = info[1]
    assert is_valid == False
    assert roll_total == 66

    # Test total of 70
    rolls = [11, 11, 11, 11, 13, 13]
    info = validate_stat_rolls(rolls)
    is_valid = info[0]
    roll_total = info[1]
    assert is_valid == True
    assert roll_total == 70

    # Test max stats (total of 120)
    rolls = [20, 20, 20, 20, 20, 20]
    info = validate_stat_rolls(rolls)
    is_valid = info[0]
    roll_total = info[1]
    assert is_valid == True
    assert roll_total == 120

def test_get_stat_array():
    test_rolls = get_stat_array()
    roll_list_length = len(test_rolls)
    assert roll_list_length == 6
    for i in range(roll_list_length):
        assert test_rolls[i] > 0
        assert test_rolls[i] <= 20 
    assert sum(test_rolls) >= 70


def test_get_race():
    races = ["Aarakocra", "Aasimar", "Bugbear", "Centaur",
        "Changeling", "Dragonborn", "Dwarf", "Elf", "Firbolg",
        "Genasi", "Gnome", "Goblin", "Goliath", "Half-Elf", 
        "Half-Orc", "Halfling", "Hobgoblin", "Human", "Kenku", 
        "Kobold", "Lizardfolk", "Loxodon", "Minotaur", "Orc", 
        "Tabaxi", "Tiefling", "Tortle", "Triton", "Warforged", 
        "Yuan-Ti Pureblood"]
    for _ in range(100):
        test_race = get_race()
        assert test_race in races

def test_get_class():
    classes = ["Artificier", "Blood Hunter", "Barbarian", 
        "Bard", "Cleric", "Druid", "Fighter", "Monk", 
        "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock",
        "Wizard"]
    for _ in range(100):
        test_class = get_class()
        assert test_class in classes

def test_get_background():
    backgrounds = ["Acolyte", "Anthropologist", "Athlete",
        "Charlatan", "Cloistered Scholar", "Courtier",
        "Criminal/Spy", "Entertainer", "Far Traveler",
        "Folk Hero", "Gladiator", "Hermit", "Inheritor",
        "Knight", "Noble", "Outlander", "Pirate", "Sage",
        "Sailor", "Soldier", "Urchin"]
    for _ in range(100):
        test_background = get_background()
        assert test_background in backgrounds


pytest.main(["-v", "--tb=line", "-rN", __file__])