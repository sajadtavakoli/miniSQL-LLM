# miniSQL-LLM

A compact LLM for natural-language-to-SQL generation.

This project demonstrates:
- schema-aware prompt engineering
- supervised fine-tuning with LoRA/QLoRA
- Hugging Face Transformers, TRL, and PEFT
- SQL validity and execution-based evaluation
- a Streamlit demo

## Example

Input:

```text
Schema: customers(id, name, country), orders(id, customer_id, amount)
Question: Show total spending per customer.
```

Output:

```sql
SELECT customer_id, SUM(amount) AS total_spending
FROM orders
GROUP BY customer_id;
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Prepare data

```bash
python scripts/prepare_dataset.py --input data/sample_text2sql.jsonl --output data/processed/train.jsonl
```

## Train with QLoRA

```bash
python scripts/train_qlora.py --config configs/qlora_config.yaml --train_file data/processed/train.jsonl
```

## Run inference

```bash
python scripts/inference.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --schema "customers(id, name, country), orders(id, customer_id, amount)" \
  --question "Show total spending per customer"
```

## Evaluate

```bash
python scripts/evaluate.py --predictions results/predictions.jsonl
```

## Demo

```bash
streamlit run app/streamlit_app.py
```

