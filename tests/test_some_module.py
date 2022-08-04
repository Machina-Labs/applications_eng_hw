"""Test some_module
"""
import unittest

import numpy as np

from python_template.some_module import normalize


class TestSomeModule(unittest.TestCase):
    def test_normalize(self):
        """Tests normalize function
        """
        vecs = np.random.rand(12, 3)

        norm_vecs = normalize(vecs)

        self.assertTrue(np.allclose(np.linalg.norm(
            norm_vecs), np.ones(norm_vecs.shape[0])))


if __name__ == "__main__":
    unittest.main()
