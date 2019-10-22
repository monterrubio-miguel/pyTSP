from .base_algorithm import BaseAlgorithm
from operator import itemgetter
from random import randrange


class TourConstructionHeuristics(BaseAlgorithm):

    # find the closest neighbor (or the farthest) to a given node in the tour
    # or not yet visited (default)
    # returns the neighbor as well as the distance between the two
    def closest_neighbor(self, tour, node, in_tour=False, farthest=False):
        neighbors = self.distances[node]
        current_dist = [(c, d) for c, d in neighbors.items()
                        if (c in tour if in_tour else c not in tour)]
        return sorted(current_dist, key=itemgetter(1))[-farthest]

    # find the neighbor k closest to the tour, i.e such that
    # cik + ckj - cij is minimized with (i, j) an edge of the tour
    # add k between the edge (i, j), resulting in a tour with subtour (i, k, j)
    # used for the cheapest insertion algorithm
    def dijkstra(self):
        city = randrange(1, self.size)
        current, tour, tour_length, tour_lengths = city, [city], 0, []
        while len(tour) != len(self.cities):
            arg_min, edge_length = self.closest_neighbor(tour, current)
            tour_length += edge_length
            tour_lengths.append(tour_length)
            tour.append(arg_min)
            current = arg_min
        # we close the tour by adding the last edge length
        tour_length += self.distances[current][city]
        tour_lengths.append(tour_length)
        intermediate_steps = [[]]
        for point in self.format_solution(tour):
            intermediate_steps.append(intermediate_steps[-1] + [point])
        print('TESTING')
        return intermediate_steps[2:], tour_lengths
