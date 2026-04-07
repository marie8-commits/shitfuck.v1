from openai import OpenAI

client = OpenAI()

def suggest_improvement(task, output, evaluation):
    prompt = f"""
    Task: {task}
    Output: {output}
    Evaluation: {evaluation}

    Suggest a better prompt or strategy to improve performance.
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content