"""Testy czarnoskrzynkowe: ticket_price (BL-1 ... BL-4)."""
import pytest

from sut import ticket_price


# EP – klasy poprawne: jedna typowa wartość z każdej klasy WEJŚCIA
# (uwaga: cena 10.0 dotyczy dwóch różnych grup wieku)
@pytest.mark.parametrize("age, price", [
    pytest.param(40, 20.0, id="normal"),
    pytest.param(5, 0.0, id="free_child"),
    pytest.param(15, 10.0, id="discount_youth"),
    pytest.param(70, 10.0, id="discount_senior"),
])
def test_ep_valid_classes(age, price):
    assert ticket_price(age) == price


# 2.
@pytest.mark.parametrize("age", [
    pytest.param(-5, id="negative"),
    pytest.param(125, id="above_120"),
])
def test_ep_out_of_range(age):
    with pytest.raises(ValueError):
        ticket_price(age)


# 3.
@pytest.mark.parametrize("age", [
    pytest.param(15.5, id="float"),
    pytest.param("osiem", id="str"),
    pytest.param(None, id="none"),
    pytest.param(False, id="bool"),
])
def test_ep_wrong_type(age):
    with pytest.raises(TypeError):
        ticket_price(age)


# 4.
@pytest.mark.parametrize("age, price", [
    pytest.param(0, 0.0, id="bound_0"),
    pytest.param(6, 0.0, id="bound_6"),
    pytest.param(7, 10.0, id="bound_7"),
    pytest.param(18, 10.0, id="bound_18"),
    pytest.param(19, 20.0, id="bound_19"),
    pytest.param(64, 20.0, id="bound_64"),
    pytest.param(65, 10.0, id="bound_65"),
    pytest.param(120, 10.0, id="bound_120", marks=pytest.mark.xfail(reason="DEF-05", strict=True)),
])
def test_bva_2p(age, price):
    assert ticket_price(age) == price


# 5.
@pytest.mark.parametrize("age", [
    pytest.param(-1, id="bound_minus_1"),
    pytest.param(121, id="bound_121"),
])
def test_bva_2p_out_of_domain(age):
    with pytest.raises(ValueError):
        ticket_price(age)


# 6.
@pytest.mark.parametrize("age, price", [
    pytest.param(1, 0.0, id="bound_1"),
    pytest.param(5, 0.0, id="bound_5"),
    pytest.param(8, 10.0, id="bound_8"),
    pytest.param(17, 10.0, id="bound_17"),
    pytest.param(20, 20.0, id="bound_20"),
    pytest.param(63, 20.0, id="bound_63"),
    pytest.param(66, 10.0, id="bound_66"),
    pytest.param(119, 10.0, id="bound_119", marks=pytest.mark.xfail(reason="DEF-05", strict=True)),
])
def test_bva_3p_extra(age, price):
    assert ticket_price(age) == price
