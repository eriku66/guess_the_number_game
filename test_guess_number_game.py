from unittest.mock import patch

import pytest
from guess_number_game import (
    get_number_of_attempts,
    get_range,
    get_valid_input,
    main,
    play_game,
)


def run_test_get_valid_input_success(
    input_value: str, return_value: int, allow_blank: bool = False
):
    with patch("builtins.input", return_value=input_value):
        assert get_valid_input("", allow_blank) == return_value


def test_get_valid_input_when_positive_number():
    run_test_get_valid_input_success("5", 5)


def test_get_valid_input_when_negative_number():
    run_test_get_valid_input_success("-5", -5)


def test_get_valid_input_when_blank_and_allow_blank():
    run_test_get_valid_input_success("-5", -5, allow_blank=True)


def run_test_get_valid_input_error(input_value: str):
    with patch("builtins.input", return_value=input_value):
        with pytest.raises(ValueError):
            get_valid_input("")


def test_get_valid_input_when_char():
    run_test_get_valid_input_error("a")


def test_get_valid_input_when_blank_and_not_allow_blank():
    run_test_get_valid_input_error("")


def run_test_get_range_success(input_values: slice, return_value: tuple):
    with patch("builtins.input", side_effect=input_values):
        assert get_range() == return_value


def test_get_range_when_max_is_over_min():
    run_test_get_range_success(["1", "2"], (1, 2))


def test_get_range_when_min_equals_max():
    run_test_get_range_success(["1", "1"], (1, 1))


def run_test_get_range_error(input_values: slice):
    with patch("builtins.input", side_effect=input_values):
        with pytest.raises(ValueError):
            get_range()


def test_get_range_when_min_is_over_max():
    run_test_get_range_error(["2", "1"])


def run_test_get_number_of_attempts_success(
    input_value: str, return_value: int | None, min: int = 1, max: int = 2
):
    with patch("builtins.input", return_value=input_value):
        assert get_number_of_attempts(min, max) == return_value


def test_get_number_of_attempts_when_positive_number():
    run_test_get_number_of_attempts_success("1", 1)


def test_get_number_of_attempts_when_blank():
    run_test_get_number_of_attempts_success("", min=1, max=2, return_value=2)
    run_test_get_number_of_attempts_success("", min=1, max=1, return_value=1)


def run_test_get_number_of_attempts_error(input_value: str):
    with patch("builtins.input", return_value=input_value):
        with pytest.raises(ValueError):
            get_number_of_attempts(1, 2)


def test_get_number_of_attempts_when_negative_number():
    run_test_get_number_of_attempts_error("-1")


def test_get_number_of_attempts_when_zero():
    run_test_get_number_of_attempts_error("0")


def run_test_play_game(capsys, random_value: int, result_message: str):
    with patch("builtins.input", side_effect=["1", "2"]):
        with patch("random.randint", return_value=random_value):
            play_game(1, 2, 2)
    captured = capsys.readouterr()
    assert result_message in captured.out


def test_play_game_win(capsys):
    run_test_play_game(capsys, random_value=2, result_message="Correct answer!")


def test_play_game_lose(capsys):
    run_test_play_game(
        capsys, random_value=3, result_message="You've reached the limit!"
    )


def run_test_main(input_values: slice, random_value: int, exit_code: int):
    with patch("builtins.input", side_effect=input_values):
        with patch("random.randint", return_value=random_value):
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == exit_code


def test_main_success():
    run_test_main(input_values=["1", "2", "", "2"], random_value=2, exit_code=0)


def test_main_value_error():
    run_test_main(input_values=["a"], random_value=0, exit_code=1)
