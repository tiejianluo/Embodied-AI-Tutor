"""Testable paper-claim helpers for the Nature SoL cube tutor.

The Streamlit UI is intentionally interactive, but the paper mechanism also
needs pure functions that can be audited in unit, system, and acceptance tests.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import os
import re
from typing import Any, Dict, Iterable, List, Mapping, Sequence


APP_NAME = "Embodied AI Tutor"
APP_VERSION = "0.1.0-roadmap"
COMMIT_SHA = os.environ.get("SOL_COMMIT_SHA", "development")

CLAIMS = {
    "C1": "reversible cube manipulation",
    "C2": "comparison redirects attention to relations",
    "C3": "notation supports symbolic redescription",
    "C4": "transfer tests portable structural understanding",
    "C5": "teacher orchestration exposes supports",
    "C6": "research conditions are isolated and logged",
    "C7": "assessment scores the three transitions",
    "C8": "release artifacts are traceable",
}

CONDITION_FEATURES = {
    "A": {
        "manipulation": True,
        "comparison": False,
        "notation": False,
        "explanation": False,
        "transfer": False,
        "teacher_orchestration": False,
    },
    "B": {
        "manipulation": True,
        "comparison": True,
        "notation": False,
        "explanation": True,
        "transfer": False,
        "teacher_orchestration": True,
    },
    "C": {
        "manipulation": True,
        "comparison": True,
        "notation": True,
        "explanation": True,
        "transfer": True,
        "teacher_orchestration": True,
    },
}

RELATION_KEYWORDS = {
    "identity",
    "inverse",
    "undo",
    "preserve",
    "preserved",
    "invariant",
    "relation",
    "cycle",
    "order",
    "repeat",
    "return",
    "structure",
    "constraint",
    "same",
    "fixed",
    "composition",
}

PROCEDURE_KEYWORDS = {
    "move",
    "turn",
    "twist",
    "step",
    "first",
    "next",
    "then",
    "after",
    "left",
    "right",
}

SYMBOLIC_PATTERNS = (
    r"\b[UDLRFB]\^?4\s*=\s*e\b",
    r"\b[UDLRFB]\s*\*\s*[UDLRFB]'\s*=\s*e\b",
    r"\b[UDLRFB]\^-?1\s*=\s*[UDLRFB]\^?3\b",
    r"\bidentity\b",
)


@dataclass(frozen=True)
class Move:
    face: str
    direction: int
    token: str


def _normalise_token(token: str) -> str:
    return token.strip().replace("\u2019", "'").replace("\u2032", "'")


def parse_move_token(token: str) -> List[Move]:
    """Parse one cube move token and expand double/repeated turns.

    Supported examples: `U`, `U'`, `U2`, `U^2`, `U^4`, `U^-1`.
    """

    token = _normalise_token(token)
    if not token:
        return []

    match = re.fullmatch(r"([UDLRFB])(?:\^?(-?\d+)|('))?", token)
    if not match:
        raise ValueError(f"Invalid cube move token: {token}")

    face, exponent_text, prime = match.groups()
    if prime:
        exponent = -1
    elif exponent_text is not None:
        exponent = int(exponent_text)
    else:
        exponent = 1

    direction = 1 if exponent >= 0 else -1
    count = abs(exponent) % 4
    if count == 0 and exponent != 0:
        count = 4

    suffix = "'" if direction < 0 else ""
    return [Move(face=face, direction=direction, token=f"{face}{suffix}") for _ in range(count)]


def parse_sequence(sequence: str | Iterable[str]) -> List[Move]:
    if isinstance(sequence, str):
        tokens = sequence.replace("*", " ").replace(".", " ").split()
    else:
        tokens = list(sequence)

    moves: List[Move] = []
    for token in tokens:
        moves.extend(parse_move_token(token))
    return moves


def normalised_sequence(sequence: str | Iterable[str]) -> List[str]:
    return [move.token for move in parse_sequence(sequence)]


def condition_supports(condition: str, feature: str) -> bool:
    try:
        return CONDITION_FEATURES[condition][feature]
    except KeyError as exc:
        raise ValueError(f"Unknown condition or feature: {condition}.{feature}") from exc


def score_explanation(text: str) -> Dict[str, Any]:
    lower = text.lower()
    relation_hits = sorted({word for word in RELATION_KEYWORDS if word in lower})
    procedure_hits = sorted({word for word in PROCEDURE_KEYWORDS if word in lower})
    symbolic_hits = [
        pattern
        for pattern in SYMBOLIC_PATTERNS
        if re.search(pattern, lower, flags=re.IGNORECASE)
    ]

    score = 35 + len(relation_hits) * 8 + len(symbolic_hits) * 12 - len(procedure_hits) * 3
    score = max(0, min(100, score))

    return {
        "score": score,
        "relation_hits": relation_hits,
        "procedure_hits": procedure_hits,
        "symbolic_hits": len(symbolic_hits),
        "orientation": "relation" if len(relation_hits) >= len(procedure_hits) else "procedure",
    }


def score_transfer_mapping(mapping: Mapping[str, str]) -> Dict[str, Any]:
    required = ["state", "operation", "identity", "preserved_relation"]
    present = [key for key in required if str(mapping.get(key, "")).strip()]
    score = round(100 * len(present) / len(required))
    return {"score": score, "present": present, "missing": [key for key in required if key not in present]}


def compute_outcome_scores(
    *,
    explanation: str,
    notation: str,
    transfer_mapping: Mapping[str, str],
) -> Dict[str, int]:
    explanation_score = score_explanation(explanation)
    notation_score = score_explanation(notation)
    transfer_score = score_transfer_mapping(transfer_mapping)

    return {
        "relational_encoding": int(explanation_score["score"]),
        "symbolic_compression": int(notation_score["score"]),
        "transfer": int(transfer_score["score"]),
    }


def validate_event(event: Mapping[str, Any]) -> bool:
    required = {"type", "condition", "payload"}
    missing = required.difference(event.keys())
    if missing:
        raise ValueError(f"Event missing fields: {sorted(missing)}")
    if event["condition"] not in CONDITION_FEATURES:
        raise ValueError(f"Unknown event condition: {event['condition']}")
    if not isinstance(event["payload"], Mapping):
        raise ValueError("Event payload must be a mapping")
    return True


def build_session_export(
    *,
    session_id: str,
    condition: str,
    role: str,
    sequence: Sequence[str],
    events: Sequence[Mapping[str, Any]],
    explanation: str = "",
    notation: str = "",
    transfer_mapping: Mapping[str, str] | None = None,
    participant_id: str = "",
) -> Dict[str, Any]:
    if condition not in CONDITION_FEATURES:
        raise ValueError(f"Unknown condition: {condition}")
    for event in events:
        validate_event(event)

    transfer_mapping = transfer_mapping or {}
    scores = compute_outcome_scores(
        explanation=explanation,
        notation=notation,
        transfer_mapping=transfer_mapping,
    )

    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "commit_sha": COMMIT_SHA,
        "session_id": session_id,
        "participant_id": participant_id,
        "condition": condition,
        "role": role,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "features": CONDITION_FEATURES[condition],
        "sequence": list(sequence),
        "events": list(events),
        "explanations": [explanation] if explanation else [],
        "notation": notation,
        "transfer_mapping": dict(transfer_mapping),
        "scores": scores,
        "claims": CLAIMS,
    }


def claim_test_matrix() -> Dict[str, Dict[str, str]]:
    return {
        claim: {
            "unit": f"Unit coverage for {description}",
            "system": f"System coverage for {description}",
            "acceptance": f"Acceptance coverage for {description}",
        }
        for claim, description in CLAIMS.items()
    }

