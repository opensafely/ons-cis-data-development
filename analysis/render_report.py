"""Render the report as an HTML file using the Jinja templating engine.

For more information about Jinja, see:
<https://jinja.palletsprojects.com/en/2.11.x/>
"""
import csv
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ENVIRONMENT = Environment(
    loader=FileSystemLoader("analysis"),
    undefined=StrictUndefined,
)


def main():
    f_out = Path("output/report.html")
    rendered_report = render_report(
        {
            "tables": (
                dict(for_column=x, rows=read_csv(f"output/safe/{x}.csv"))
                for x in ["visit_num"]
            ),
        }
    )
    f_out.write_text(rendered_report, encoding="utf-8")


def render_report(data):
    template = ENVIRONMENT.get_template("report_template.html")
    return template.render(data)


def read_csv(fname):
    with open(fname, newline="") as f:
        yield from csv.reader(f)


if __name__ == "__main__":
    main()
