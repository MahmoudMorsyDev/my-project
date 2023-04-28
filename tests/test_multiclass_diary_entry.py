from lib.multiclass_diary_entry import DiaryEntry

def test_diary_entry_init():
    diary_entry = DiaryEntry('hello people')
    assert diary_entry.contents == "hello people"
    assert diary_entry.contact_list == []

def test_add_contact():
    diary_entry = DiaryEntry("hey there")
    diary_entry.add_contact("4112345678")
    assert diary_entry.contact_list == ["4112345678"]    

def test_get_contacts():
    diary_entry = DiaryEntry("hey there")
    diary_entry.add_contact("3332342345678")
    assert diary_entry.get_contacts() == ["3332342345678"]