#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:06:21 2019

@author: arbeit
"""

import numpy as np
import pytest
from maxima import find_maxima

test_cases = [([0, 1, 2, 1, 2, 1, 0], [2, 4]),
              ([-i**2 for i in range(-3, 4)], [3]),
              ([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)], [16,78]),
              ([4, 2, 1, 3, 1, 2], [0, 3, 5]),
              ([4, 2, 1, 3, 1, 5], [0, 3, 5]),
              ([4, 2, 1, 3, 1], [0, 3]),
              ([1, 2, 2, 1], [1, 2]),
              ([1, 2, 2, 3, 1], [3]),
              ([1, 3, 2, 2, 1], [1]),
              ([3, 2, 2, 3], [0, 3])]

@pytest.mark.parametrize('input, expected_result', test_cases)
def test_lower(input, expected_result):
    output = find_maxima(input)
    
    assert output == expected_result