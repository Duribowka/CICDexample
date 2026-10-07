from main import addition, substraction, multiplication, division


def test():
    assert addition(10, 5) == 15
    assert substraction(10, 5) == 5
    assert multiplication(10, 5) == 50
    assert division(10, 5) == 2



if __name__ == "__main__":
    test()
    print("All tests passed!")