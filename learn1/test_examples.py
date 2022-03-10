class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        assert a+b == 14

    def test_check_math(self):
        a = 5
        b = 11
        expected_some = 14
        assert a + b == expected_some, f"че то у тебя тут не равно {expected_some}"