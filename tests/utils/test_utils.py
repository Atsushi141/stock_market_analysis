from src.utils.utils import add_one_day

def test_add_one_day():
    assert add_one_day("2026-01-01") == "2026-01-02"
