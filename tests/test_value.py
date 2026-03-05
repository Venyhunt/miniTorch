from graphgrad.value import Value

def test_value_initialization():
    v= Value(5.0)                         # we are calling Value calss through an obj
    assert v.data == 5.0
    assert v.grad == 0.0
    
def test_value_repr():
    v = Value(3.0)
    assert "Value" in repr(v)

    