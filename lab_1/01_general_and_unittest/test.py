import unittest
from unittest.mock import patch
from app import Figure

# Функція з input() для завдання з mock (Крок 4, пункт 5)
def ask_user_figure():
    fig_type = input("Введіть тип фігури: ")
    fig_len = int(input("Введіть довжину: "))
    fig = Figure(fig_type, fig_len)
    return f"Створено {fig.get_figure_type} з довжиною {fig.get_figure_length}"

class TestFigure(unittest.TestCase):
    def setUp(self):
        self.square = Figure("квадрат", 5)
        self.rectangle = Figure("прямокутник", 10)
        self.triangle = Figure("трикутник", 7)

    # 1. Тест типу та виправленої довжини (⭐)
    def test_figure_type_and_length(self):
        self.assertEqual(self.square.get_figure_type, "квадрат")
        self.assertEqual(self.square.get_figure_length, 5)

    # 2. Тест кутів для всіх фігур (⭐)
    def test_get_angles(self):
        self.assertEqual(self.square.get_angles, 4)
        self.assertEqual(self.rectangle.get_angles, 4)
        self.assertEqual(self.triangle.get_angles, 3)

    # 3. Тести граничних умов: нуль, мінус, невідома фігура (🔥)
    def test_invalid_inputs(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)
        with self.assertRaises(AssertionError):
            Figure("трикутник", -5)
        with self.assertRaises(AssertionError):
            Figure("коло", 10)

    # 4. Тест із subTest для всіх типів Figure (⭐)
    def test_all_figures_subtest(self):
        for fig_type in Figure.FIGURES:
            with self.subTest(figure=fig_type):
                fig = Figure(fig_type, 4)
                self.assertEqual(fig.get_figure_type, fig_type)
                self.assertEqual(fig.get_figure_length, 4)

    # 5. Тестування функції з input() через patch / mock (⭐)
    @patch("builtins.input", side_effect=["квадрат", "8"])
    def test_ask_user_figure(self, mock_input):
        result = ask_user_figure()
        self.assertEqual(result, "Створено квадрат з довжиною 8")
        self.assertEqual(mock_input.call_count, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)