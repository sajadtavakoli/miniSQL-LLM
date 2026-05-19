import argparse
import json
from pathlib import Path

def format_example(row):
    text = f"""### Instruction:
{row.get('instruction', 'Convert the question into a SQL query.')}

### Database schema:
{row['schema']}

### Question:
{row['question']}

### SQL:
{row['sql']}"""
    return {"text": text, **row}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.input, encoding="utf-8") as fin, open(args.output, "w", encoding="utf-8") as fout:
        for line in fin:
            row = json.loads(line)
            fout.write(json.dumps(format_example(row)) + "\n")

if __name__ == "__main__":
    main()
