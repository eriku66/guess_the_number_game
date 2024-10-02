from unittest.mock import patch

import pytest
from guess_number_game import (
    get_number_of_attempts,
    get_range,
    get_valid_input,
    main,
    play_game,
)


def test_get_valid_input_when_positive_number():
    with patch("builtins.input", return_value="5"):
        assert get_valid_input("") == 5


def test_get_valid_input_when_negative_number():
    with patch("builtins.input", return_value="-5"):
        assert get_valid_input("") == -5


def test_get_valid_input_when_char():
    with patch("builtins.input", return_value="a"):
        with pytest.raises(ValueError):
            get_valid_input("")


def test_get_valid_input_when_blank_and_not_allow_blank():
    with patch("builtins.input", return_value=""):
        with pytest.raises(ValueError):
            get_valid_input("", allow_blank=False)


def test_get_valid_input_when_blank_and_allow_blank():
    with patch("builtins.input", return_value=""):
        assert get_valid_input("", allow_blank=True) is None


def test_get_range_when_max_is_over_min():
    with patch("builtins.input", side_effect=["1", "2"]):
        assert get_range() == (1, 2)


def test_get_range_when_min_equals_max():
    with patch("builtins.input", side_effect=["1", "1"]):
        assert get_range() == (1, 1)


def test_get_range_when_min_is_over_max():
    with patch("builtins.input", side_effect=["2", "1"]):
        with pytest.raises(ValueError):
            get_range()


def test_get_number_of_attempts_when_positive_number():
    with patch("builtins.input", return_value="1"):
        assert get_number_of_attempts(1, 2) == 1


def test_get_number_of_attempts_when_blank():
    with patch("builtins.input", return_value=""):
        assert get_number_of_attempts(1, 2) == 2
    with patch("builtins.input", return_value=""):
        assert get_number_of_attempts(1, 1) == 1


def test_get_number_of_attempts_when_negative_number():
    with patch("builtins.input", return_value="-1"):
        with pytest.raises(ValueError):
            get_number_of_attempts(1, 2)


def test_get_number_of_attempts_when_zero():
    with patch("builtins.input", return_value="0"):
        with pytest.raises(ValueError):
            get_number_of_attempts(1, 2)


def test_play_game_win(capsys):
    with patch("builtins.input", side_effect=["1", "2"]):
        with patch("random.randint", return_value=2):
            play_game(1, 2, 2)
    captured = capsys.readouterr()
    assert "Correct answer!" in captured.out


def test_play_game_lose(capsys):
    with patch("builtins.input", side_effect=["1", "2"]):
        with patch("random.randint", return_value=3):
            play_game(1, 3, 2)
    captured = capsys.readouterr()
    assert "You've reached the limit!" in captured.out


def test_main_success(capsys):
    with patch("builtins.input", side_effect=["1", "2", "", "2"]):
        with patch("random.randint", return_value=2):
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 0


def test_main_value_error(capsys):
    with patch("builtins.input", side_effect=["a"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 1
