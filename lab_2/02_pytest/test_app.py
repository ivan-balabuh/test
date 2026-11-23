import pytest
from app import Figure  # Перевірте точну назву вашого модуля з класом Figure


# --- БАЗОВІ ТЕСТИ ТА ЗАВДАННЯ З МАРКЕРАМИ (⭐) ---

@pytest.mark.unit
def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"


@pytest.mark.unit
def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


# --- ПАРАМЕТРИЗАЦІЯ (⭐) ---

# ⭐ Додайте параметризований тест для всіх дозволених фігур
@pytest.mark.parametrize("figure", Figure.FIGURES)
def test_allowed_figure(figure):
    obj = Figure(figure, 1)
    assert obj.type == figure


# --- FIXTURES (⭐) ---

# ⭐ Створіть fixture, яка повертає фігуру з довжиною 10, і перевірте її властивості
@pytest.fixture
def figure_length_10():
    return Figure("квадрат", 10)


def test_figure_length_10_properties(figure_length_10):
    assert figure_length_10.type == "квадрат"
    assert figure_length_10.get_figure_length == 10


# ⭐ Створіть fixture зі scope="module" та перевірте, що її можна використовувати у двох тестах
@pytest.fixture(scope="module")
def allowed_figures():
    return Figure.FIGURES


def test_allowed_figures_not_empty(allowed_figures):
    assert len(allowed_figures) > 0


def test_triangle_in_allowed_figures(allowed_figures):
    assert "трикутник" in allowed_figures


@pytest.mark.parametrize(
    "invalid_type",
    ["коло", "трапеція", "ромб", "", None, 123]
)
def test_invalid_figure_types(invalid_type):
    with pytest.raises(AssertionError):
        Figure(invalid_type, 5)


@pytest.mark.parametrize(
    "invalid_length",
    [0, -1, -100, "5", None]
)
def test_invalid_figure_lengths(invalid_length):
    with pytest.raises((AssertionError, TypeError)):
        Figure("квадрат", invalid_length)