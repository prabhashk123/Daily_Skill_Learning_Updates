import pytest

def testLogin():
    print("Login Successful")
     
def testLogoff():
    print("Logoff Successful")
 
@pytest.mark.skip  
def testCalculations():
    assert 2+2 ==4
 
@pytest.mark.xfail    
def testCalculation():
    assert 2+2 ==5


    
    