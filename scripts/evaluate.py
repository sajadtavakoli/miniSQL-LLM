import argparse
import json
from pathlib import Path
from minisql_llm.sql_utils import exact_match, is_valid_sql

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", required=True, help="JSONL with prediction and reference fields")
    parser.add_argument("--database", default=None)
    args = parser.parse_args()

    total = exact = valid = 0
    for line in open(args.predictions, encoding="utf-8"):
        row = json.loads(line)
        total += 1
        exact += int(exact_match(row["prediction"], row["reference"]))
        ok, _ = is_valid_sql(row["prediction"], args.database)
        valid += int(ok)

    metrics = {
        "n": total,
        "exact_match": exact / max(total, 1),
        "sql_validity": valid / max(total, 1),
    }
    Path("results").mkdir(exist_ok=True)
    Path("results/metrics.json").write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
