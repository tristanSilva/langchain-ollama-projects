"""
The Practical Toolkit — 8 Techniques
1. Role Assignment — tell it who to be
Before asking anything, assign an identity. This shapes every word of the response.
python"You are a senior Python developer who gives concise, production-ready code only."
"You are a Filipino barangay secretary who answers in simple, plain language."
The role sets the tone, vocabulary, and format of everything that follows.

2. Output Format Specification — tell it exactly what to return
Never assume. Always state the format explicitly.
python# Weak
"Give me info about LangChain."

# Strong
"Return ONLY a JSON object. No intro. No explanation.
Start with {{ and end with }}.
Keys: name, purpose, used_for (list of 3)."
For non-JSON: specify bullet points, numbered lists, tables, word limits, line limits.

3. Gating Words — your discovery today
These are boundary instructions that suppress the LLM's natural conversational behavior:
python"Return ONLY..."
"Do NOT include any introduction."
"Start your response with the first item, nothing before it."
"No explanation. No preamble. No closing sentence."
"Answer in exactly one sentence."
"Do not say 'here is' or 'certainly' or 'of course'."
Think of gating words as the walls of a container. Without walls, water flows everywhere. With walls, it goes exactly where you direct it.

4. Few-Shot Examples — show it, don't just tell it
The most powerful technique. Give the LLM one or two examples of the exact output you want.
python
Convert the following into a barangay record format.

Example input: "Juan is 35 years old and lives in Sta. Cruz."
Example output:
Name: Juan
Age: 35
Barangay: Sta. Cruz

Now convert this:
Input: "Maria is 28 and resides in Barangay Dinaga."

One good example beats three paragraphs of instructions.

5. Step-by-Step Instruction — chain of thought
For complex tasks, break the instruction into numbered steps. The LLM follows sequential structure better than paragraphs.
python
Do the following steps in order:
1. Read the constituent name from the input
2. Identify their barangay
3. Check if age is above 18
4. Return result as JSON only

This mirrors how you would instruct a junior developer. Numbered steps reduce ambiguity.

6. Constraint Stacking — layer your limits
Combine multiple constraints in one prompt. Each constraint removes one degree of freedom from the LLM's response.
python

You are a JSON API. 
Return ONLY valid JSON.
No markdown. No explanation. No intro sentence.
Maximum 3 keys.
All values must be strings.

Each line closes one escape route the LLM might take.


7. Negative Instructions — tell it what NOT to do
LLMs respond well to explicit prohibitions, not just positive instructions.
python"Do NOT use bullet points."
"Do NOT repeat the question."
"Do NOT include any text outside the JSON block."
"Do NOT apologize or add a closing remark."
Pair every positive instruction with its negative counterpart when precision matters.

8. Temperature Control — not in the prompt, but in the model
When you need consistent, predictable output — lower the temperature. When you need creativity — raise it.
pythonllm = ChatOllama(model="llama3", temperature=0)  # Most deterministic
llm = ChatOllama(model="llama3", temperature=0.7)  # More creative
For JSON output and structured data — always use temperature=0. For creative writing or brainstorming — use 0.7 or higher.

The Priority Order for Your Projects
When building BarangayIS or any production system, apply techniques in this order:
1. Role assignment first       → sets the personality
2. Output format specification → sets the structure  
3. Gating words                → removes filler
4. Few-shot examples           → removes ambiguity
5. Temperature = 0             → removes randomness
If output is still wrong after all five — rewrite the prompt from scratch using First Principles. Ask: what is the absolute minimum instruction that produces exactly what I need?


"""