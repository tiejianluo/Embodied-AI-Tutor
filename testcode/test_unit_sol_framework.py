import unittest

from sol_framework import (
    build_session_export,
    condition_supports,
    normalised_sequence,
    parse_move_token,
    score_explanation,
    score_transfer_mapping,
)


class SolFrameworkUnitTests(unittest.TestCase):
    def test_parse_identity_and_inverse_notation(self):
        self.assertEqual(normalised_sequence("U^4"), ["U", "U", "U", "U"])
        self.assertEqual(normalised_sequence("R R'"), ["R", "R'"])
        self.assertEqual(normalised_sequence("F2"), ["F", "F"])
        self.assertEqual(normalised_sequence("U^-1"), ["U'"])

    def test_invalid_notation_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_move_token("Q")

    def test_condition_feature_flags_match_paper_design(self):
        self.assertTrue(condition_supports("A", "manipulation"))
        self.assertFalse(condition_supports("A", "comparison"))
        self.assertTrue(condition_supports("B", "comparison"))
        self.assertFalse(condition_supports("B", "notation"))
        self.assertTrue(condition_supports("C", "notation"))
        self.assertTrue(condition_supports("C", "transfer"))

    def test_explanation_scoring_rewards_relation_language(self):
        relation = score_explanation("U^4 = e returns to identity and preserves the relation order.")
        procedure = score_explanation("First turn right, then move, then step after step.")
        self.assertGreater(relation["score"], procedure["score"])
        self.assertEqual(relation["orientation"], "relation")

    def test_transfer_mapping_requires_structural_roles(self):
        score = score_transfer_mapping(
            {
                "state": "robot orientation",
                "operation": "rotate 90 degrees",
                "identity": "original heading",
                "preserved_relation": "four rotations return to identity",
            }
        )
        self.assertEqual(score["score"], 100)
        self.assertEqual(score["missing"], [])

    def test_export_contains_traceability_metadata(self):
        export = build_session_export(
            session_id="s1",
            condition="C",
            role="researcher",
            sequence=["U", "U", "U", "U"],
            events=[{"type": "move", "condition": "C", "payload": {"move": "U"}}],
            explanation="The operation repeats until identity.",
            notation="U^4 = e",
            transfer_mapping={
                "state": "clock hand",
                "operation": "quarter turn",
                "identity": "12 o'clock",
                "preserved_relation": "four turns return",
            },
        )
        self.assertEqual(export["app_name"], "Embodied AI Tutor")
        self.assertIn("app_version", export)
        self.assertEqual(export["condition"], "C")
        self.assertEqual(export["scores"]["transfer"], 100)


if __name__ == "__main__":
    unittest.main()

