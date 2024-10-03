from unittest.mock import patch

import pytest

from guess_number_game import (
    get_number_of_attempts,
    get_range,
    get_valid_input,
    main,
    play_game,
)


@pytest.mark.parametrize(
    "input_value, return_value, allow_blank",
    [
        ("5", 5, False),
        ("-5", -5, False),
        ("", None, True),
    ],
)
def test_get_valid_input_success(
    input_value: str, return_value: int, allow_blank: bool
):
    with patch("builtins.input", return_value=input_value):
        assert get_valid_input("", allow_blank) == return_value


@pytest.mark.parametrize("input_value", ["a", ""])
def test_get_valid_input_error(input_value: str):
    with patch("builtins.input", return_value=input_value):
        with pytest.raises(ValueError):
            get_valid_input("")


@pytest.mark.parametrize(
    "input_values, return_value", [(["1", "2"], (1, 2)), (["1", "1"], (1, 1))]
)
def test_get_range_success(input_values: slice, return_value: tuple):
    with patch("builtins.input", side_effect=input_values):
        assert get_range() == return_value


@pytest.mark.parametrize("input_values", [(["2", "1"])])
def test_get_range_error(input_values: slice):
    with patch("builtins.input", side_effect=input_values):
        with pytest.raises(ValueError):
            get_range()


@pytest.mark.parametrize(
    "input_value, return_value, min, max",
    [("1", 1, 1, 2), ("", 2, 1, 2), ("", 1, 1, 1)],
)
def test_get_number_of_attempts_success(
    input_value: str, return_value: int | None, min: int, max: int
):
    with patch("builtins.input", return_value=input_value):
        assert get_number_of_attempts(min, max) == return_value


@pytest.mark.parametrize("input_value", [("-1"), ("0")])
def test_get_number_of_attempts_error(input_value: str):
    with patch("builtins.input", return_value=input_value):
        with pytest.raises(ValueError):
            get_number_of_attempts(1, 2)


@pytest.mark.parametrize(
    "random_value, result_message",
    [(2, "Correct answer!"), (3, "You've reached the limit!")],
)
def test_play_game(capsys, random_value: int, result_message: str):
    with patch("builtins.input", side_effect=["1", "2"]):
        with patch("random.randint", return_value=random_value):
            play_game(1, 2, 2)
    captured = capsys.readouterr()
    assert result_message in captured.out


@pytest.mark.parametrize(
    "input_values, random_value, exit_code",
    [
        (["1", "2", "", "2"], 2, 0),
        (["a"], 0, 1),
    ],
)
def test_main(input_values: slice, random_value: int, exit_code: int):
    with patch("builtins.input", side_effect=input_values):
        with patch("random.randint", return_value=random_value):
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == exit_code
