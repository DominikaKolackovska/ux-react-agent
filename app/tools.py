import re
from typing import Dict, Any, Optional

def compute_readability(text: str) -> Dict[str, Any]:
    sentences = [s for s in re.split(r"[.!?]", text) if s.strip()]
    words = re.findall(r"\b\w+\b", text)

    avg_sentence_len = len(words) / max(1, len(sentences))
    avg_word_len = sum(len(w) for w in words) / max(1, len(words))

    return {
        "sentences": len(sentences),
        "words": len(words),
        "avg_sentence_length": round(avg_sentence_len, 2),
        "avg_word_length": round(avg_word_len, 2),
        "assessment": (
            "Hard to scan – sentences too long."
            if avg_sentence_len > 18
            else "Readable UX copy."
        ),
    }


def score_usability_heuristics(problem_description: str) -> Dict[str, Any]:
    keywords = {
        "Visibility of system status": ["loading", "feedback", "waiting"],
        "User control and freedom": ["back", "undo", "cancel"],
        "Error prevention": ["error", "mistake", "wrong"],
        "Consistency": ["confusing", "inconsistent"],
    }

    result = []
    text = problem_description.lower()

    for heuristic, cues in keywords.items():
        score = sum(1 for c in cues if c in text) + 1
        result.append({"heuristic": heuristic, "severity": min(score, 5)})

    return {
        "summary": "Higher score = bigger UX risk",
        "heuristics": sorted(result, key=lambda x: x["severity"], reverse=True),
    }


def suggest_ab_tests(goal: str, current_flow: str) -> Dict[str, Any]:
    return {
        "goal": goal,
        "tests": [
            {
                "hypothesis": "Clear CTA reduces hesitation",
                "variant_a": "CTA: Pokračovať",
                "variant_b": "CTA: Pokračovať k platbe (30s)",
                "metric": "Checkout completion rate",
            },
            {
                "hypothesis": "Progress indicator reduces drop-off",
                "variant_a": "No progress",
                "variant_b": "3-step progress bar",
                "metric": "Step-to-step conversion",
            },
        ],
    }


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "compute_readability",
            "description": "Analyze UX copy readability",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                },
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "score_usability_heuristics",
            "description": "Score UX problem using heuristics",
            "parameters": {
                "type": "object",
                "properties": {
                    "problem_description": {"type": "string"},
                },
                "required": ["problem_description"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "suggest_ab_tests",
            "description": "Generate A/B test ideas",
            "parameters": {
                "type": "object",
                "properties": {
                    "goal": {"type": "string"},
                    "current_flow": {"type": "string"},
                },
                "required": ["goal", "current_flow"],
            },
        },
    },
]

AVAILABLE_FUNCTIONS = {
    "compute_readability": compute_readability,
    "score_usability_heuristics": score_usability_heuristics,
    "suggest_ab_tests": suggest_ab_tests,
}
