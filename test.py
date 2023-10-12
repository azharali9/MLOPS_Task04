from calculator import Calculator

def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

def test_subtract():
    calc = Calculator()
    result = calc.subtract(5, 3)
    assert result == 2

# Run the tests
if __name__ == '__main__':
    test_add()
    test_subtract()
    
   