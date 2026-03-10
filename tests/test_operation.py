from src.matn_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(0,1)==1

def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(0,0)==0