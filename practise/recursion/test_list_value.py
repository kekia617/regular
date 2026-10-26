from list_value import flatten

def test_regular():
    assert flatten([]) == []
    assert flatten([1]) == [1]
    assert flatten([[]]) == []
    assert flatten([1, 2, [3, 4]]) == [1, 2, 3, 4]
    assert flatten([1, [], [[]], [2, 3, [4, 5]]]) == [1, 2, 3, 4, 5]
def test_base_case():
    assert flatten([[[[[[[[[]]]]]]]]]) == []
    assert flatten(['a']) == ['a']