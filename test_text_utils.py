from text_utils import count_chars, count_words, count_sentences

def test_count_chars():
    assert count_chars("Hello, World!") == 13
    assert count_chars("Hello, World! How are you?") == 26
    assert count_chars("Hello, World! How are you? I'm fine.") == 35

def test_count_words():
    assert count_words("Hello, World!") == 2
    assert count_words("Hello, World! How are you?") == 6
    assert count_words("Hello, World! How are you? I'm fine.") == 8

def test_count_sentences():
    assert count_sentences("Hello, World!") == 1
    assert count_sentences("Hello, World! How are you?") == 2
    assert count_sentences("Hello, World! How are you? I'm fine.") == 3

def test_empty_string():
    assert count_chars("") == 0
    assert count_words("") == 0
    assert count_sentences("") == 0