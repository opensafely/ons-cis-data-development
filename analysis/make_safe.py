import csv
from pathlib import Path

import sdc
import utils


def main():
    args = utils.parse_args()
    for table in args["config"]["tables"]:
        make_safe(table["from"], table["columns"], table["to"])


def make_safe(in_, columns_to_make_safe, out_):
    p_in = Path(in_)
    p_out = Path(out_)
    p_out.parent.mkdir(parents=True, exist_ok=True)

    args = {"newline": ""}
    with p_in.open("r", **args) as f_in, p_out.open("w", **args) as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        header = next(reader)
        writer.writerow(header)

        # Do values in each column need to be made safe?
        make_safe_flags = [x in columns_to_make_safe for x in header]
        for row in reader:
            # Starting with safe_row as an empty list ensures that we copy in either
            # values that have been made safe or values that do not need making safe.
            safe_row = []
            for value, make_safe_flag in zip(row, make_safe_flags):
                if make_safe_flag:
                    value = int(value)
                    # This is where we make the unsafe value a safe value.
                    value = sdc.redact_le_seven(value)
                    value = sdc.round_to_nearest_five(value)
                safe_row.append(value)
            assert len(row) == len(safe_row)
            writer.writerow(safe_row)


if __name__ == "__main__":
    main()
