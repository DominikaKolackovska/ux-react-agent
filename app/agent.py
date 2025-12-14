import json
from typing import List, Dict, Any
from openai import OpenAI
from app.tools import TOOLS, AVAILABLE_FUNCTIONS

class ReactAgent:
    def __init__(self, client: OpenAI, model: str = "gpt-4o", max_iterations: int = 8):
        self.client = client
        self.model = model
        self.max_iterations = max_iterations

    def run(self, messages: List[Dict[str, Any]]) -> str:
        for iteration in range(1, self.max_iterations + 1):
            print(f"\n--- Iteration {iteration} ---")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
                parallel_tool_calls=False,
            )

            msg = response.choices[0].message

            if msg.tool_calls:
                messages.append(
                    {
                        "role": "assistant",
                        "content": msg.content,
                        "tool_calls": [
                            {
                                "id": tc.id,
                                "type": "function",
                                "function": {
                                    "name": tc.function.name,
                                    "arguments": tc.function.arguments,
                                },
                            }
                            for tc in msg.tool_calls
                        ],
                    }
                )

                for tc in msg.tool_calls:
                    fn_name = tc.function.name
                    fn_args = json.loads(tc.function.arguments or "{}")
                    tool_id = tc.id

                    print(f"Calling tool: {fn_name}({fn_args})")

                    result = AVAILABLE_FUNCTIONS[fn_name](**fn_args)

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_id,
                            "name": fn_name,
                            "content": json.dumps(result),
                        }
                    )

                continue

            messages.append({"role": "assistant", "content": msg.content})
            return msg.content

        return "ERROR: Max iterations reached"
