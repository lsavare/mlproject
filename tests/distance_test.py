from mlproject.distance import haversine

def test_data_type():
    assert type(haversine(1,2,3,4)) == type(1.0)