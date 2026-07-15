from src.open_llm_vtuber.utils.sentence_divider import (
    comma_splitter,
    contains_end_punctuation,
    is_complete_sentence,
    segment_text_by_regex,
)


def test_is_complete_sentence():
    assert is_complete_sentence("Hello world.")
    assert is_complete_sentence("你好！")
    assert not is_complete_sentence("Hello world")


def test_contains_end_punctuation():
    assert contains_end_punctuation("Done. And more")
    assert not contains_end_punctuation("no ending here")


def test_comma_splitter():
    before, after = comma_splitter("first part, second part")
    assert before == "first part,"
    assert after == "second part"


def test_segment_text_by_regex():
    sentences, remainder = segment_text_by_regex("One. Two! Three incomplete")
    assert sentences == ["One.", "Two!"]
    assert remainder.strip() == "Three incomplete"
