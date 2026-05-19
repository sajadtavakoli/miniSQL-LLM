def build_prompt(schema: str, question: str) -> str:
    return f"""### Instruction:
Convert the question into a valid SQL query.

### Database schema:
{schema}

### Question:
{question}

### SQL:
"""
