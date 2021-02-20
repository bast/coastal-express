import click
import glob
from .main import main


@click.command()
@click.option("--boundary", help="File containing the boundary.")
@click.option(
    "--islands", help="File(s) containing island data - you can use wildcards."
)
@click.option("--view-angle", help="View angle in degrees.")
@click.option("--min-distance", help="Min distance.")
@click.option("--max-distance", help="Max distance.")
@click.option("--output-dir", help="Output folder.")
def cli(boundary, islands, view_angle, min_distance, max_distance, output_dir):
    main(
        boundary_file_name=boundary,
        island_file_names=glob.glob(islands),
        view_angle_deg=float(view_angle),
        min_distance=float(min_distance),
        max_distance=float(max_distance),
        output_directory=output_dir,
    )


if __name__ == "__main__":
    cli()
