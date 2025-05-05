import argparse
from data.fetch_data import fetch_all_data
from models.projection_engine import build_projections
from platforms.draftkings import optimize_dk
from platforms.fanduel import optimize_fd
from platforms.underdog import generate_underdog_props
from platforms.prizepicks import generate_prizepicks_props

def main(date):
    data = fetch_all_data(date)
    projections = build_projections(data)
    optimize_dk(projections)
    optimize_fd(projections)
    generate_underdog_props(projections)
    generate_prizepicks_props(projections)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    main(args.date)
