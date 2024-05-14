from unittest.mock import patch
from source import pricing_module
import json


def test_f2_with_fixed_f1():
    val = json.loads('{"price":10}')

    with patch("source.pricing_module.fetch_product", return_value=val):
        assert pricing_module.calculate_tax(12) == 10 * 0.2
