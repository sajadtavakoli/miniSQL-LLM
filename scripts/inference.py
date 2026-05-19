import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from minisql_llm.prompts import build_prompt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--schema", required=True)
    parser.add_argument("--question", required=True)
    parser.add_argument("--max_new_tokens", type=int, default=128)
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(args.model, device_map="auto", trust_remote_code=True)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    prompt = build_prompt(args.schema, args.question)
    output = generator(prompt, max_new_tokens=args.max_new_tokens, do_sample=False)[0]["generated_text"]
    print(output.split("### SQL:")[-1].strip())

if __name__ == "__main__":
    main()
