def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1, 0.1) == [100, 800, 900, 0]
    assert fair_sharer([0, 0, 0, 1000], 2, 0.2) == [360, 0, 360, 280]
    assert fair_sharer([1, 2, 3, 4], 0, 0.1) == [1, 2, 3, 4]
    assert fair_sharer([100, 0, 0, 100], 5, 0.05) == [50, 50, 50, 50]
    
    print("All tests passed.")
