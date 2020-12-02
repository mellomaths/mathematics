import math


def distance_between_points(x1, y1, z1, x2, y2, z2) :
  """
  Calculates the distance between two points in space (3D).
  To use this function in 2D, pass both z1 and z2 as 0.

  Keyword arguments:
  x1 - x position of point 1
  y1 - y position of point 1
  z1 - z position of point 1
  x2 - x position of point 2
  y2 - y position of point 2
  z2 - z position of point 2

  Returns: a float
  """

  distance_x = (x2 - x1) * (x2 - x1)
  distance_y = (y2 - y1) * (y2 - y1)
  distance_z = (z2 - z1) * (z2 - z1)
  distance = math.sqrt(distance_x + distance_y + distance_z)
  return distance