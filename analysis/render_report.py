"""Render the report as an HTML file using the Jinja templating engine.

For more information about Jinja, see:
<https://jinja.palletsprojects.com/en/2.11.x/>
"""
import csv
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

import utils

ENVIRONMENT = Environment(
    loader=FileSystemLoader("analysis"),
    undefined=StrictUndefined,
)


def main():
    args = utils.parse_args()
    rendered_report = render_report(
        {
            "tables": (
                dict(for_column=p.stem, rows=read_csv(p))
                for p in (Path(t) for t in args["config"]["tables"])
            ),
        }
    )
    Path(args["config"]["to"]).write_text(rendered_report, encoding="utf-8")


def render_report(data):
    template = ENVIRONMENT.get_template("report_template.html")
    return template.render(data)


def read_csv(fpath):
    with fpath.open(newline="") as f:
        yield from csv.reader(f)


if __name__ == "__main__":
    main()
