import os
import tempfile
import shutil
import pytest
from .main import main


def compare_files(file1, file2):
    with open(file1, "r") as f:
        lines1 = f.read().splitlines()
    with open(file2, "r") as f:
        lines2 = f.read().splitlines()
    for i, line in enumerate(lines1):
        tuples = [
            (float(n1), float(n2))
            for (n1, n2) in zip(lines1[i].split(), lines2[i].split())
        ]
        for (f1, f2) in tuples:
            assert f1 == pytest.approx(f2)


def test_main():
    _this_path = os.path.dirname(os.path.realpath(__file__))

    if os.getenv("GENERATE_REFERENCES", False):
        output_dir = os.path.join(_this_path, "..", "example", "output")
    else:
        output_dir = tempfile.mkdtemp()

    boundary_file_name = os.path.join(_this_path, "..", "example", "boundary.txt")
    island_file_names = [os.path.join(_this_path, "..", "example", "islands.txt")]

    main(
        boundary_file_name=boundary_file_name,
        island_file_names=island_file_names,
        view_angle_deg=90.0,
        min_distance=3.0,
        max_distance=40.0,
        output_directory=output_dir,
    )

    if not os.getenv("GENERATE_REFERENCES", False):
        compare_files(
            os.path.join(_this_path, "..", "example", "output", "boundary.txt"),
            os.path.join(output_dir, "boundary.txt"),
        )
        compare_files(
            os.path.join(_this_path, "..", "example", "output", "islands.txt"),
            os.path.join(output_dir, "islands.txt"),
        )
        shutil.rmtree(output_dir)
