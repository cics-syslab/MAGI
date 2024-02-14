import unittest

from utils.render import process_distribution_version


class TestDistributionVersionProcessor(unittest.TestCase):

    def test_process_valid_private(self):
        input_str = """
        Some random text
        // PRIVATE_BEGIN
        This is private
        // PRIVATE_END
        This is outside any block
        /* PUBLIC_BEGIN */
        This is public
        /* PUBLIC_END */
        """
        output = process_distribution_version(input_str, "private", True)
        self.assertIn("Some random text", output)
        self.assertIn("This is private", output)
        self.assertIn("This is public", output)
        self.assertIn("This is outside any block", output)

    def test_process_valid_private_no_public(self):
        input_str = """
        Some random text
        // PRIVATE_BEGIN
        This is private
        // PRIVATE_END
        This is outside any block
        /* PUBLIC_BEGIN */
        This is public
        /* PUBLIC_END */
        """
        output = process_distribution_version(input_str, "private", False)
        self.assertIn("Some random text", output)
        self.assertIn("This is private", output)
        self.assertNotIn("This is public", output)
        self.assertIn("This is outside any block", output)

    def test_process_valid_public(self):
        input_str = """
        Some random text
        // PRIVATE_BEGIN
        This is private
        // PRIVATE_END
        This is outside any block
        /* PUBLIC_BEGIN */
        This is public
        /* PUBLIC_END */
        """

        output = process_distribution_version(input_str, "public")
        self.assertIn("Some random text", output)
        self.assertNotIn("This is private", output)
        self.assertIn("This is public", output)
        self.assertIn("This is outside any block", output)

    def test_unmatched_block(self):
        input_str = """
        Some text
        /* PUBLIC_BEGIN */
        This is public
        """
        with self.assertRaises(ValueError) as context:
            process_distribution_version(input_str, "public")
        self.assertIn("Unmatched blocks detected:", str(context.exception))

    def test_invalid_version(self):
        input_str = "Some text"
        with self.assertRaises(ValueError) as context:
            process_distribution_version(input_str, "invalid_version")
        self.assertIn(
            "version_type should be either 'public' or 'private'.", str(context.exception))
