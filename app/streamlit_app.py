import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from minisql_llm.prompts import build_prompt

st.set_page_config(page_title="miniSQL-LLM", page_icon="🧠")
st.title("miniSQL-LLM")
st.write("Generate SQL from a database schema and a natural-language question.")

model_name = st.text_input("Model", "Qwen/Qwen2.5-1.5B-Instruct")
schema = st.text_area("Database schema", "customers(id, name, country), orders(id, customer_id, amount)")
question = st.text_input("Question", "Show total spending per customer")

if st.button("Generate SQL"):
    with st.spinner("Loading model and generating SQL..."):
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
        generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
        output = generator(build_prompt(schema, question), max_new_tokens=128, do_sample=False)[0]["generated_text"]
        st.code(output.split("### SQL:")[-1].strip(), language="sql")
