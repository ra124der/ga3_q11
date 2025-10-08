import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_wins():
    """Test with multiple streaks to ensure the longest is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, 0, 1]) == 3

def test_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, -2, 3, 4, -5, 6]) == 2

def test_all_positive():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Test with only non-positive numbers, expecting 0."""
    assert longest_positive_streak([0, -1, -5, -10]) == 0

def test_single_positive_element():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_zero_element():
    """Test a list with a single zero."""
    assert longest_positive_streak([0]) == 0

def test_single_negative_element():
    """Test a list with a single negative number."""
    assert longest_positive_streak([-5]) == 0

def test_streak_at_the_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, -3, 4, 5, 6, 7]) == 4

def test_streak_at_the_beginning():
    """Test when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 4, -5, 6]) == 4