import pytest
from testdemo import Maopaopaixu_Test
@pytest.mark.run(order=1)
def testmupao():

    assert Maopaopaixu_Test([10,18,15,199,0,99,3,2,8]) == [0, 2, 3, 8, 10, 15, 18, 99, 199]
@pytest.mark.run(order=2)
def testmupao1():
    assert Maopaopaixu_Test([18,15,199,0,99,3,2,8]) == [ 2,  8, 15, 18, 99, 199]
@pytest.mark.run(order=3)
def testmupao2():
    assert Maopaopaixu_Test([18,15,199,0,99,3,2,8]) == [2, 3, 8, 15, 18, 99, 199]

