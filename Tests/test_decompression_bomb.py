from helper import unittest, PillowTestCase, tearDownModule

from PIL import Image

test_file = "Images/lena.ppm"

ORIGINAL_LIMIT = Image.MAX_IMAGE_PIXELS


class TestDecompressionBomb(PillowTestCase):

    def tearDown(self):
        Image.MAX_IMAGE_PIXELS = ORIGINAL_LIMIT

    def test_no_warning_small_file(self):
        # Implicit assert: no warning.
        # A warning would cause a failure.
        Image.open(test_file)

    def test_no_warning_no_limit(self):
        # Arrange
        # Turn limit off
        Image.MAX_IMAGE_PIXELS = None
        self.assertEqual(Image.MAX_IMAGE_PIXELS, None)

        # Act / Assert
        # Implicit assert: no warning.
        # A warning would cause a failure.
        Image.open(test_file)

    def test_warning(self):
        # Arrange
        # Set limit to a low, easily testable value
        Image.MAX_IMAGE_PIXELS = 10
        self.assertEqual(Image.MAX_IMAGE_PIXELS, 10)

        # Act / Assert
        self.assert_warning(
            Image.DecompressionBombWarning,
            lambda: Image.open(test_file))

if __name__ == '__main__':
    unittest.main()

# End of file
