import math
import ntpath
import os
import flanders
from .view_vectors import compute_view_vectors


def read_points(file_name):
    polygons = []
    with open(file_name, "r") as f:
        for line in f:
            points = []
            num_points = int(line)
            for _ in range(num_points):
                line = next(f)
                point = [float(element) for element in line.split()]
                points.append(point)
            polygons.append(points)
    return polygons


def get_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2.0 + (p2[1] - p1[1]) ** 2.0)


def main(
    boundary_file_name,
    island_file_names,
    view_angle_deg,
    min_distance,
    max_distance,
    output_directory,
):

    # there is only one boundary
    boundary_points = read_points(boundary_file_name)[0]
    view_vectors = compute_view_vectors(boundary_points, scale=-1.0)

    all_points = boundary_points
    for island_file in island_file_names:
        for islands_points in read_points(island_file):
            view_vectors += compute_view_vectors(islands_points, scale=1.0)
            all_points += islands_points

    all_points = [(p[0], p[1]) for p in all_points]

    num_points = len(all_points)

    tree = flanders.build_search_tree(all_points)

    observer_indices = list(range(num_points))
    view_angles_deg = [90.0 for _ in observer_indices]

    indices = flanders.nearest_indices_from_indices(
        tree, observer_indices, view_vectors, view_angles_deg
    )

    distances = [
        get_distance(all_points[i], all_points[indices[i]]) for i in range(num_points)
    ]
    distances = iter(distances)

    # now we have a reversed list of distances
    # we will go again through all input files and augment each of them with the distance
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for file_name in [boundary_file_name] + island_file_names:
        with open(file_name, "r") as f_in:
            file_name_without_path = ntpath.basename(file_name)
            with open(
                os.path.join(output_directory, file_name_without_path), "w"
            ) as f_out:
                for line in f_in.read().splitlines():
                    if len(line.split()) == 1:
                        f_out.write(line + "\n")
                    else:
                        d = next(distances)
                        # the distance is capped by min_distance and max_distance
                        d = max(d, min_distance)
                        d = min(d, max_distance)
                        f_out.write("{0} {1}\n".format(line, d))
