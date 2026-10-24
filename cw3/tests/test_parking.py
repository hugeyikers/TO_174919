"""Testy czarnoskrzynkowe: parking_fee (PK-1 ... PK-5)."""
import pytest

from sut import parking_fee


# EP – klasy poprawne (także klasy WYJŚĆ: 0 zł, 5 zł, 10 zł ...)
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(600, 20.0, id="daily"),
    pytest.param(10, 0.0, id="free_0_15"),
    pytest.param(30, 5.0, id="fee_5_1_hour"),
    pytest.param(90, 10.0, id="fee_10_2_hours"),
    pytest.param(150, 15.0, id="fee_15_3_hours"),
])
def test_ep_valid_classes(minutes, fee):
    assert parking_fee(minutes) == fee


# 2.
@pytest.mark.parametrize("minutes", [
    pytest.param(-10, id="negative"),
    pytest.param(1500, id="above_1440"),
])
def test_ep_out_of_range(minutes):
    with pytest.raises(ValueError):
        parking_fee(minutes)


# 3.
@pytest.mark.parametrize("minutes", [
    pytest.param(15.5, id="float"),
    pytest.param("sto", id="str"),
    pytest.param(False, id="bool"),
    pytest.param(None, id="none"),
])
def test_ep_wrong_type(minutes):
    with pytest.raises(TypeError):
        parking_fee(minutes)


# 4. 
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(0, 0.0, id="bound_0"),
    pytest.param(15, 0.0, id="bound_15"),
    pytest.param(16, 5.0, id="bound_16"),
    pytest.param(60, 5.0, id="bound_60"),
    pytest.param(61, 10.0, id="bound_61"),
    pytest.param(120, 10.0, id="bound_120"),
    pytest.param(121, 15.0, id="bound_121"),
    pytest.param(180, 15.0, id="bound_180"),
    pytest.param(181, 20.0, id="bound_181"),
    pytest.param(1440, 20.0, id="bound_1440"),
])
def test_bva_2p(minutes, fee):
    assert parking_fee(minutes) == fee


# 5.
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(1, 0.0, id="bound_1", marks=pytest.mark.xfail(reason="DEF-03", strict=True)),
    pytest.param(14, 0.0, id="bound_14"),
    pytest.param(59, 5.0, id="bound_59"),
    pytest.param(119, 10.0, id="bound_119"),
    pytest.param(179, 15.0, id="bound_179"),
    pytest.param(1439, 20.0, id="bound_1439"),
])
def test_bva_3p_extra(minutes, fee):
    assert parking_fee(minutes) == fee


# 6.
@pytest.mark.parametrize("minutes", [
    pytest.param(-1, id="bound_minus_1"),
    pytest.param(1441, id="bound_1441"),
])
def test_bva_out_of_range(minutes):
    with pytest.raises(ValueError):
        parking_fee(minutes)
