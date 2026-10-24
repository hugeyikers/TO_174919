"""Testy czarnoskrzynkowe: grade_from_percent (OC-1 ... OC-4)."""
import pytest

from sut import grade_from_percent


# 1.
@pytest.mark.parametrize("percent, grade", [
    pytest.param(25, 2.0, id="fail"),
    pytest.param(55, 3.0, id="satisfactory"),
    pytest.param(65, 3.5, id="satisfactory_plus"),
    pytest.param(75, 4.0, id="good"),
    pytest.param(85, 4.5, id="good_plus"),
    pytest.param(95, 5.0, id="very_good"),
])
def test_ep_valid_classes(percent, grade):
    assert grade_from_percent(percent) == grade


# 2.
@pytest.mark.parametrize("percent", [
    pytest.param(-10, id="negative"),
    pytest.param(110, id="above_100"),
])
def test_ep_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)


# 3.
@pytest.mark.parametrize("percent", [
    pytest.param(75.5, id="float", marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
    pytest.param("pięć", id="str", marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
    pytest.param(None, id="none"),
    pytest.param(True, id="bool", marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
])
def test_ep_wrong_type(percent):
    with pytest.raises(TypeError):
        grade_from_percent(percent)


# 4.
@pytest.mark.parametrize("percent, grade", [
    pytest.param(0, 2.0, id="bound_0"),
    pytest.param(50, 2.0, id="bound_50"),
    pytest.param(51, 3.0, id="bound_51"),
    pytest.param(60, 3.0, id="bound_60"),
    pytest.param(61, 3.5, id="bound_61"),
    pytest.param(70, 3.5, id="bound_70"),
    pytest.param(71, 4.0, id="bound_71"),
    pytest.param(80, 4.0, id="bound_80"),
    pytest.param(81, 4.5, id="bound_81"),
    pytest.param(90, 4.5, id="bound_90", marks=pytest.mark.xfail(reason="DEF-02", strict=True)),
    pytest.param(91, 5.0, id="bound_91"),
    pytest.param(100, 5.0, id="bound_100"),
])
def test_bva_2p(percent, grade):
    assert grade_from_percent(percent) == grade


@pytest.mark.parametrize("percent, grade", [
    pytest.param(1, 2.0, id="bound_1"),
    pytest.param(49, 2.0, id="bound_49"),
    pytest.param(59, 3.0, id="bound_59"),
    pytest.param(69, 3.5, id="bound_69"),
    pytest.param(79, 4.0, id="bound_79"),
    pytest.param(89, 4.5, id="bound_89"),
    pytest.param(99, 5.0, id="bound_99"),
])
def test_bva_3p_extra(percent, grade):
    assert grade_from_percent(percent) == grade


# 5.
@pytest.mark.parametrize("percent", [
    pytest.param(-1, id="bound_minus_1"),
    pytest.param(101, id="bound_101"),
])
def test_bva_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)
