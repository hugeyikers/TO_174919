"""Testy czarnoskrzynkowe: validate_password (HS-1 ... HS-4)."""
import pytest

from sut import validate_password


def password_of_length(n):
    """Hasło z liter i cyfr o długości n, np. 5 -> 'a1a1a'."""
    return ("a1" * n)[:n]


def test_example_valid_password():
    assert validate_password("haslo123") is True


def test_example_wrong_type():
    with pytest.raises(TypeError):
        validate_password(None)


# 1.
@pytest.mark.parametrize("password", [
    pytest.param("Haslo123", id="standard_valid"),
    pytest.param("Za żółć 1", id="polish_letters_and_spaces", marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
    pytest.param("H@slo!23#", id="special_chars", marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
])
def test_ep_valid(password):
    assert validate_password(password) is True


# 2.
@pytest.mark.parametrize("password", [
    pytest.param("123456789", id="no_letter"),
    pytest.param("HasloBezCyfry", id="no_digit"),
    pytest.param("Has1", id="too_short"),
    pytest.param("BardzoDlugieHaslo12345", id="too_long"),
])
def test_ep_invalid(password):
    assert validate_password(password) is False


#3.
@pytest.mark.parametrize("n, expected", [
    pytest.param(7, False, id="bound_7"),
    pytest.param(8, True, id="bound_8"),
    pytest.param(20, True, id="bound_20"),
    pytest.param(21, False, id="bound_21"),
])
def test_bva_length_2p(n, expected):
    assert validate_password(password_of_length(n)) is expected


# 4.
@pytest.mark.parametrize("n, expected", [
    pytest.param(9, True, id="bound_9"),
    pytest.param(19, True, id="bound_19"),
])
def test_bva_length_3p_extra(n, expected):
    assert validate_password(password_of_length(n)) is expected