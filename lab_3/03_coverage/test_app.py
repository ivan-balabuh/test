import pytest
from app import Figure


def test_get_angles_no_assert():
    fig = Figure("triangle")
    _ = fig.get_angles


@pytest.mark.parametrize(
    "figure_type, expected",
    [
        ("triangle", 3),
        ("square", 4),
        ("rectangle", 4),
        ("circle", None),
    ],
)
def test_get_angles_all_branches(figure_type, expected):
    fig = Figure(figure_type)
    assert fig.get_angles == expected
