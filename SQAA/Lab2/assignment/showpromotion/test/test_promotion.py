import pytest
import source.print_promotion as showpromotion_functions

def test_print_promotion1():
    result = showpromotion_functions.print_promotion(total_cost = 0)
    assert result == "Thank you and see you next time"

def test_print_promotion50():
    result = showpromotion_functions.print_promotion(total_cost = 100)
    assert result == "Thank you and see you next time"

def test_print_promotion150():
    result = showpromotion_functions.print_promotion(total_cost = 250)
    assert result == "Thank you and see you next time"

def test_print_promotion499():
    result = showpromotion_functions.print_promotion(total_cost = 499)
    assert result == "Thank you and see you next time"



def test_print_promotion500():
    result = showpromotion_functions.print_promotion(total_cost=500)
    assert result =="Free ice cream cone = 1"

def test_print_promotion501():
    result = showpromotion_functions.print_promotion(total_cost=501)
    assert result =="Free ice cream cone = 1"

def test_print_promotion600():
    result = showpromotion_functions.print_promotion(total_cost=600)
    assert result =="Free ice cream cone = 1"

def test_print_promotion699():
    result = showpromotion_functions.print_promotion(total_cost=699)
    assert result =="Free ice cream cone = 1"



def test_print_promotion700():
    result = showpromotion_functions.print_promotion(total_cost=700)
    assert result =="Free chocolate cake = 1"

def test_print_promotion701():
    result = showpromotion_functions.print_promotion(total_cost=701)
    assert result =="Free chocolate cake = 1"

def test_print_promotion1000():
    result = showpromotion_functions.print_promotion(total_cost=1000)
    assert result =="Free chocolate cake = 1"

def test_print_promotion1199():
    result = showpromotion_functions.print_promotion(total_cost=1199)
    assert result =="Free chocolate cake = 1"



def test_print_promotion1200():
    result = showpromotion_functions.print_promotion(total_cost=1200)
    assert result =="Free ice cream cone = 1 and chocolate cake = 1"

def test_print_promotion1350():
    result = showpromotion_functions.print_promotion(total_cost=1350)
    assert result =="Free ice cream cone = 1 and Free chocolate cake = 1"

def test_print_promotion1500():
    result = showpromotion_functions.print_promotion(total_cost=1500)
    assert result =="Free ice cream cone = 1 and chocolate cake = 1"

def test_print_promotion1699():
    result = showpromotion_functions.print_promotion(total_cost=1699)
    assert result =="Free ice cream cone = 1 and Free chocolate cake = 1"

def test_print_promotion3600():
    result = showpromotion_functions.print_promotion(total_cost=3600)
    assert result =="Free ice cream cone = 3 and chocolate cake = 3"

def test_print_promotion4099():
    result = showpromotion_functions.print_promotion(total_cost=4099)
    assert result =="Free ice cream cone = 3 and Free chocolate cake = 3"



def test_print_promotion3100():
    result = showpromotion_functions.print_promotion(total_cost=3100)
    assert result =="Free ice cream cone = 2 and chocolate cake = 3"

def test_print_promotion3599():
    result = showpromotion_functions.print_promotion(total_cost=3599)
    assert result =="Free ice cream cone = 2 and chocolate cake = 3"

def test_print_promotion4300():
    result = showpromotion_functions.print_promotion(total_cost=4300)
    assert result =="Free ice cream cone = 3 and chocolate cake = 4"

def test_print_promotion4799():
    result = showpromotion_functions.print_promotion(total_cost=4799)
    assert result =="Free ice cream cone = 3 and chocolate cake = 4"



def test_print_promotionError1():
    result = showpromotion_functions.print_promotion(total_cost=๑)
    assert result =="Error"

def test_print_promotionError2():
    result = showpromotion_functions.print_promotion(total_cost=-๑)
    assert result =="Error"

def test_print_promotionError3():
    result = showpromotion_functions.print_promotion(total_cost=IV)
    assert result =="Error"   

def test_print_promotionError4():
    result = showpromotion_functions.print_promotion(total_cost=สามสิบ)
    assert result =="Error" 

