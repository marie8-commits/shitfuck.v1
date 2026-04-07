from openai import OpenAI

client = OpenAI()

def evaluate(task, output):
    prompt = f"""
    Task: {task}
    Output: {output}

    Score this from 1-10 for:
    - correctness
    - clarity
    - usefulness

    Return JSON.
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content