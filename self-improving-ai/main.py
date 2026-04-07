from agent import run_task
from evaluator import evaluate
from improver import suggest_improvement
import json

def human_check(suggestion):
    print("\nSuggested Improvement:\n")
    print(suggestion)
    decision = input("\nApprove? (y/n): ")
    return decision.lower() == "y"

task = "Write a Python function to sort a list efficiently."
current_prompt = task

for iteration in range(3):
    print(f"\n--- Iteration {iteration+1} ---")

    output = run_task(current_prompt)
    print("\nOutput:\n", output)

    score = evaluate(task, output)
    print("\nEvaluation:\n", score)

    improvement = suggest_improvement(task, output, score)

    if human_check(improvement):
        current_prompt = improvement
    else:
        print("Keeping current strategy.")