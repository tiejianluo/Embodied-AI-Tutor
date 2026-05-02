import os
import sys
import unittest

from sol_framework import (
    CLAIMS,
    build_session_export,
    claim_test_matrix,
    normalised_sequence,
)


class MockModule:
    def __getattr__(self, name):
        return MockModule()

    def __iter__(self):
        return iter([])

    def __len__(self):
        return 0

    def __call__(self, *args, **kwargs):
        if args and isinstance(args[0], int):
            return tuple(MockModule() for _ in range(args[0]))
        if args and isinstance(args[0], list):
            return tuple(MockModule() for _ in args[0])
        return MockModule()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class MockPIL:
    class Image:
        pass

    PngImagePlugin = MockModule()


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.modules.setdefault("streamlit", MockModule())
sys.modules.setdefault("plotly", MockModule())
sys.modules.setdefault("plotly.graph_objects", MockModule())
sys.modules["plotly.graph_objects"].Figure = MockModule()
sys.modules.setdefault("matplotlib", MockModule())
sys.modules.setdefault("matplotlib.pyplot", MockModule())
sys.modules.setdefault("matplotlib.patches", MockModule())
sys.modules.setdefault("PIL", MockPIL)

from app import Cube


class PaperClaimAcceptanceTests(unittest.TestCase):
    def test_c1_cube_identity_and_inverse_are_executable(self):
        cube = Cube()
        start = cube.get_current_state()
        cube.apply_sequence("U^4")
        self.assertTrue((cube.get_current_state() == start).all())
        cube.apply_sequence("R R'")
        self.assertTrue((cube.get_current_state() == start).all())

    def test_c1_to_c8_are_represented_in_acceptance_matrix(self):
        matrix = claim_test_matrix()
        self.assertEqual(set(matrix), set(CLAIMS))
        for claim in CLAIMS:
            self.assertIn("unit", matrix[claim])
            self.assertIn("system", matrix[claim])
            self.assertIn("acceptance", matrix[claim])

    def test_researcher_can_export_condition_c_evidence(self):
        export = build_session_export(
            session_id="acceptance-c",
            condition="C",
            role="researcher",
            sequence=normalised_sequence("U^4"),
            events=[
                {"type": "move", "condition": "C", "payload": {"move": "U"}},
                {"type": "compare", "condition": "C", "payload": {"target": "identity"}},
                {"type": "notation", "condition": "C", "payload": {"notation": "U^4 = e"}},
                {"type": "transfer", "condition": "C", "payload": {"domain": "clock cycle"}},
            ],
            explanation="Four repeated turns return to identity and preserve the cyclic relation.",
            notation="U^4 = e",
            transfer_mapping={
                "state": "clock hand position",
                "operation": "quarter turn",
                "identity": "starting position",
                "preserved_relation": "four turns return to the start",
            },
        )
        self.assertEqual(export["condition"], "C")
        self.assertEqual(export["features"]["teacher_orchestration"], True)
        self.assertGreaterEqual(export["scores"]["relational_encoding"], 60)
        self.assertGreaterEqual(export["scores"]["symbolic_compression"], 40)
        self.assertEqual(export["scores"]["transfer"], 100)
        self.assertIn("commit_sha", export)


if __name__ == "__main__":
    unittest.main()

