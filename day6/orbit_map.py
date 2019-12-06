from typing import Type


class Body:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent_body = parent

    def __repr__(self):
        return self.name

    def has_parent(self) -> bool:
        return self.parent is not None

    def orbit_complexity(self) -> int:
        if self.parent_body is not None:
            return self.parent_body.orbit_complexity() + 1
        else:
            return 0

    def parents(self, ) -> list:
        parents = []
        if self.parent_body is not None:
            parents.append(self.parent_body)
            parents.extend(self.parent_body.parents())
        return parents


class OrbitMap:
    _bodies = {}

    def __init__(self, input: str, debug: bool = False):
        for orbit in open(input):  # first pass - only creating bodies, not orbits
            center, satellite = orbit.strip().split(')')
            if debug:
                print("{} orbits around {}".format(satellite, center))

            if center not in self._bodies:
                self._bodies[center] = Body(name=center)

            if satellite not in self._bodies:
                self._bodies[satellite] = Body(name=satellite)

        for orbit in open(input):  # second pass - set up orbits
            center, satellite = orbit.strip().split(')')
            self._bodies[satellite].parent_body = self._bodies[center]

        if debug:
            print("Map contains {} bodies".format(len(self._bodies)))

    def count_orbits(self) -> int:
        count = 0
        for body in self._bodies.values():
            count = count + body.orbit_complexity()

        return count

    def plan_route(self, you: str, target: str, debug: bool = False) -> int:
        origin = self._bodies[you].parent_body
        dest = self._bodies[target].parent_body

        origin_parents = origin.parents()
        dest_parents = dest.parents()

        if debug:
            print("Origin parents: {}".format(origin_parents))
            print("Destination parents: {}".format(dest_parents))

        for body in origin_parents:
            if body in dest_parents:
                common_parent = body
                break

        if debug:
            print("The common parent is: {}".format(common_parent))

        steps = 0
        for body in origin_parents:
            steps += 1
            if body is common_parent:
                break

        for body in dest_parents:
            steps +=1
            if body is common_parent:
                break

        return steps
