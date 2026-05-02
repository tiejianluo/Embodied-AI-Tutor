import unittest

from sol_framework import build_session_export, normalised_sequence, validate_event


class LearningFlowSystemTests(unittest.TestCase):
    def test_condition_c_learning_flow_exports_analyzable_log(self):
        sequence = normalised_sequence("U^4")
        events = [{"type": "condition_start", "condition": "C", "payload": {"condition": "C"}}]
        events.extend({"type": "move", "condition": "C", "payload": {"move": move}} for move in sequence)
        events.append({"type": "compare", "condition": "C", "payload": {"contrast": "U^4 vs R R'"}})
        events.append({"type": "notation", "condition": "C", "payload": {"notation": "U^4 = e"}})
        events.append({"type": "transfer", "condition": "C", "payload": {"domain": "robot rotation"}})

        for event in events:
            self.assertTrue(validate_event(event))

        export = build_session_export(
            session_id="system-c",
            condition="C",
            role="learner",
            sequence=sequence,
            events=events,
            explanation="The repeated operation returns to identity and preserves order.",
            notation="U^4 = e",
            transfer_mapping={
                "state": "robot heading",
                "operation": "rotate 90 degrees",
                "identity": "starting heading",
                "preserved_relation": "four rotations return to the start",
            },
        )

        self.assertEqual(export["features"]["comparison"], True)
        self.assertEqual(export["features"]["notation"], True)
        self.assertEqual(export["features"]["transfer"], True)
        self.assertEqual(len(export["sequence"]), 4)
        self.assertGreaterEqual(export["scores"]["relational_encoding"], 60)
        self.assertGreaterEqual(export["scores"]["symbolic_compression"], 40)
        self.assertEqual(export["scores"]["transfer"], 100)


if __name__ == "__main__":
    unittest.main()
