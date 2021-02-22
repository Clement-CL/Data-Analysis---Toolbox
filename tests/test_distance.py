from clem_toolbox.distance import haversine

def test_distance_type():
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 48.03509454612089, -3.523117322968529
    assert type(haversine(lon1, lat1, lon2, lat2)) == float
    assert haversine(lon1, lat1, lon2, lat2) == 444.9210795014478
