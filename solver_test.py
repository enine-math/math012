import solver


def is_solved():
    assert not solver.solver(28)


def test_solver():
    assert solver.solver(5) == 28
