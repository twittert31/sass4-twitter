from shapely.geometry import Polygon, Point, LineString

def main():
  grid_polygon = Polygon(((0,0), (1,0), (1,1),(1,0)))
  grid_lines = LineString([(0,0), (1,0), (1,1),(1,0),(0,0)])
  # check once if you have to add another coordinate to complete the loop
  print(grid_polygon)

  print(grid_lines)
  point1 = Point(1,1)
  point2 = Point(0.5,0.5)
  print("p1",point1)
  print("within polygon:",point1.within(grid_polygon))
  print("on the line:",point1.within(grid_lines))
  print("p2",point2)
  print("within polygon:",point2.within(grid_polygon))
  print("on the line:",point2.touches(grid_lines))
  return 0
if __name__ == "__main__":
  main()