import unittest
import tempfile
import os
from ex03 import estimate_values_based_on_data


def make_csv(rows: list[tuple]) -> str:
    f = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    for x, y in rows:
        f.write(f"{x},{y}\n")
    f.close()
    return f.name


class TestEstimateValues(unittest.TestCase):

    def test_docstring_example(self):
        path = make_csv([(2, 2), (4, 3)])
        result = estimate_values_based_on_data(path, [5, 0, -2])
        self.assertAlmostEqual(result[0], 3.5, places=5)
        self.assertAlmostEqual(result[1], 1.0, places=5)
        self.assertAlmostEqual(result[2], 0.0, places=5)
        os.unlink(path)

    def test_returns_list(self):
        path = make_csv([(1, 1), (2, 2)])
        result = estimate_values_based_on_data(path, [3])
        self.assertIsInstance(result, list)
        os.unlink(path)

    def test_return_elements_are_float(self):
        path = make_csv([(1, 1), (2, 2)])
        result = estimate_values_based_on_data(path, [3])
        self.assertIsInstance(result[0], float)
        os.unlink(path)

    def test_order_preserved(self):
        path = make_csv([(0, 0), (10, 10)])
        result = estimate_values_based_on_data(path, [1, 5, 9])
        self.assertLess(result[0], result[1])
        self.assertLess(result[1], result[2])
        os.unlink(path)

    def test_single_x_value(self):
        path = make_csv([(0, 0), (2, 4)])
        result = estimate_values_based_on_data(path, [1])
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], 2.0, places=5)
        os.unlink(path)

    def test_perfect_line(self):
        path = make_csv([(i, 3 * i + 1) for i in range(10)])
        result = estimate_values_based_on_data(path, [10, 20])
        self.assertAlmostEqual(result[0], 31.0, places=4)
        self.assertAlmostEqual(result[1], 61.0, places=4)
        os.unlink(path)


if __name__ == '__main__':
    unittest.main()
