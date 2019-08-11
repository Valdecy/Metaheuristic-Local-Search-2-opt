# Metaheuristic-Local-Search-2-opt
2-opt Function for TSP problems. The function returns: 1) A list with the order of the cities to visit, and the total distance for visiting this same list order.

This Function accepts coordinates or a distance matrix as input.

* X = Distance Matrix

* buid_distance_matrix (HELPER FUNCTION) = Tranforms coordinates in a distance matrix (euclidean distance).

* city_tour = Initial list of visitation.

* seed (HELPER FUNCTION) = Generates a random list of visitation.

* recursive_seeding = Total number of iterations, if this number is negative then 2-opt optimal of the seed is found. The Default Value is -1.

* plot_tour_distance_matrix (HELPER FUNCTION) = A projection is generated based on the distance matrix. The estimated projection may present plot with path crosses, even for optimal solution. Red Point = Initial city; Orange Point = Second City

* plot_tour_coordinates (HELPER FUNCTION) = Plots the optimal solution. Red Point = Initial city; Orange Point = Second City
