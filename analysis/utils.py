import json
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--config", type=json.loads)
    return vars(parser.parse_args())
