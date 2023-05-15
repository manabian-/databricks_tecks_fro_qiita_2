import pytest
from pytest_test.src.utilities import add_num

def test__add_num__001():
    """successes（正常系テスト）"""
    assert add_num(1, 1) == 2

def test__add_num__002():
    """successes（異常系テスト）"""
    # 文字を引数とすることでエラーとなる想定
    with pytest.raises(TypeError) as e:
        add_num(1, 'ABC')

def test__add_num__003():
    """failures"""
    assert add_num(1, 1) == 1

def test__add_num__004():
    """failures(errors)"""
    assert add_num(1 + "a") ==1

@pytest.mark.skip(reason='スキップ用')
def test__add_num__005():
    """skipped"""
    assert a

@pytest.mark.xfail
def test__add_num__006():
    """XFAIL"""
    assert add_num(1, 1) == 1

@pytest.mark.xfail
def test__add_num__007():
    """XPASS"""
    assert add_num(1, 1) == 2