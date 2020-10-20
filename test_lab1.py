import pytest
import lab1


@pytest.mark.parametrize("input,expected",
                         [((6, 4, 75000), "wrong level mod"),
                          ((7, 4, 75000), 22500),
                          ((10, -1, 75000), "wrong review mod"),
                          ((10, 3, 50), "wrong salary value")])
def test_decision_table_calculate_bonus(input, expected):
    assert lab1.calculate_bonus(*input) == expected


@pytest.mark.parametrize("input,expected",
                         [(69999, None),
                          (70000, 70000),
                          (750000, 750000),
                          (750001, None)])
def test_boundary_val_salary_check(input, expected):
    assert lab1.salary_check(input) == expected


@pytest.mark.parametrize("input,expected",
                         [(6, None),  
                          (7, 0.05),
                          (10, 0.1),
                          (11, 0.1),
                          (13, 0.15),
                          (14, 0.15),
                          (15, 0.2),
                          (17, 0.2),
                          (18, None)])
def test_eq_part_boundary_val_get_mod_from_level(input, expected):
    assert lab1.get_mod_from_level(input) == expected


@pytest.mark.parametrize("input,expected",
                         [(0.9, None),
                          (1, 0),  
                          (2, 0.25),
                          (2.3, 0.25),
                          (2.5, 0.5),
                          (2.6, 0.5),
                          (3, 1),
                          (3.1, 1),
                          (3.5, 1.5),
                          (3.6, 1.5),
                          (4, 2),
                          (5, 2),
                          (5.1, None)])  
def test_eq_part_boundary_val_get_mod_from_review(input, expected):
    assert lab1.get_mod_from_review(input) == expected


@pytest.mark.parametrize("input,expected",
                         [('test', None),
                          ([1, 1], None),
                          ((1, 1), None)])
def test_negative_get_mod_from_level(input, expected):  
    assert lab1.get_mod_from_level(input) == expected


@pytest.mark.parametrize("input,expected",
                         [('test', None),
                          ([1, 1], None),
                          ((1, 1), None)])
def test_negative_get_mod_from_review(input, expected):
    assert lab1.get_mod_from_review(input) == expected


@pytest.mark.parametrize("input,expected",
                         [('test', None),
                          ([1, 1], None),
                          ((1, 1), None)])
def test_negative_salary(input, expected):
    assert lab1.salary_check(input) == expected

@pytest.mark.parametrize("input,expected",
                         [(('test', 'test2', 'test3'), 'wrong level mod')])
def test_negatibe_calculate_bonus(input, expected):
    assert lab1.calculate_bonus(*input) == expected
