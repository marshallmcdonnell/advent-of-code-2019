import argparse

from wire import Wire

class Grid:
    BIG_DIST = 999999

    def __init__(self, wires=None):
        self._wires = []
        self._intersections = []
        
        if wires:
            self.add_wires(wires)

    @staticmethod
    def manhattan_distance(point1, point2):
        ''' Compute the manhattan distance between two points
        Ref: https://en.wikipedia.org/wiki/Taxicab_geometry

        :param point1: Point as a tuple of floats 
        :type point1: tuple(float)
        :param point2: Point as a tuple of floats 
        :type point2: tuple(float)
        :return: 1-norm distance of points
        '''
        series = [ abs(p - q) for p, q in zip(point1, point2)]
        return sum(series)

    def _compute_intersections(self):
        '''Compute the intesections of all Wires on Grid '''
        # Check each wire against all others for intersections
        for w1 in self.wires:
            for w2 in self.wires:
                if w1 == w2:
                    continue
                intersections = []
                for i, p in enumerate(w1.points):
                    print("   Point {} of {}".format(i, len(w1.points)))
                    if p in w2.points:
                        intersections.append(p)

        # Remove origin point since will always be an intersection
        intersections.remove((0,0))

        # Set the intersections for the object
        self._intersections = intersections
 
    def _compute_closest_intersection(self):
        ''' Compute the closest intersection to the origin
        Example: point, dist = self._compute_closest_intersection()

        :return: Closest intersection point and its distance or (None, None)
                 if no intersection points exists
        '''
        # initialize the minimums 
        closest = None
        min_distance = self.BIG_DIST

        # Loop over intersections to find the closest to origin
        for intersection in self.intersections:
            distance = self.manhattan_distance(intersection, (0,0))
            if distance < min_distance:
                min_distance = distance
                closest = intersection

        # Set minimum distance to None if we didn't find an intersection
        if not closest:
            min_distance = None

        return closest, min_distance
 
    def add_wires(self, wires):
        ''' Add wire(s) to the Grid object
        :param wires: List of Wire objects to add to Grid
        :type wire: Wire or list[Wire]
        '''
        if isinstance(wires, list):
            for wire in wires:
                self._wires.append(wire)
        else:
            self._wires.append(wires)

    @property
    def wires(self):
        ''' Gets the current Wires on the Grid '''
        return self._wires

    @property
    def intersections(self):
        ''' Gets the current intersections of all Wires on the Grid '''
        self._compute_intersections()
        return sorted(self._intersections)
      
    @property
    def closest_intersection(self):
        ''' Gets the closest intersection to the origin on the Grid '''
        intersection, distance = self._compute_closest_intersection()
        return intersection

    @property
    def closest_intersection_distance(self):
        ''' Gets the closest intersection distance to the origin on the Grid '''
        intersection, distance = self._compute_closest_intersection()
        return distance


if __name__ == "__main__":
    # Parse CLI arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str,
                        help="Input file with wires.")
    parser.add_argument("--part", type=int, default=1,
                        choices=[1, 2],
                        help="Either sovling part 1 or part 2 of problem")
    args = parser.parse_args()

    # Read in input file with list of masses and parse
    with open(args.input_file, 'r') as f:
        contents = f.readlines()

    wires = []
    for instructions in contents:
        wires.append(Wire(instructions))

    assert len(wires) == 2
    
    grid = Grid(wires)
    msg = "Closest intersection: {} Distance: {}"
    msg = msg.format(grid.closest_intersection, grid.closest_intersection_distance)
    print(msg)
