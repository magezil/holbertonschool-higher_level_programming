#!/usr/bin/python3
"""
This module defines the function matrix_mul()
Raises:
    ValueError: If the last dimension of m_a is not the same size
                as the second-to-last dimension of m_b.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the result of m_a * m_b
    """
    return np.dot(m_a, m_b).tolist()
