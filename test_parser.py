from parser import parser


def main():
    test_parser()


def test_positive():
    assert parser(2) == 4
    assert parser(3) == 9


def test_negative():
    assert parser(-2) == 4
    assert parser(-3) == 9


def test_zero():
    assert parser(0) == 0



if __name__ == "__main__":
    main()

