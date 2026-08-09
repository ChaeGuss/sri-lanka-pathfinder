from math import atan2, cos, radians, sin, sqrt

EARTH_RADIUS_KM = 6371.0  # Average radius of the Earth in kilometers

def geographic_distance(coordinate_a: tuple[float, float], coordinate_b: tuple[float, float], ) -> float:
    """Return approximate great circle distance in Kilometres"""

    lat1, lon1 = coordinate_a
    lat2, lon2 = coordinate_b

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2) # Haversine intermediate value

    central_angle = 2 * atan2(sqrt(a), sqrt(1 - a),)

    return EARTH_RADIUS_KM * central_angle     # Distance on the spherical model is radius × central angle


