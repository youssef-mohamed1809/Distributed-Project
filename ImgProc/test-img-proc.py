import unittest
import cv2
import numpy as np

from img_processing import histEqualize, grayscale, blur, detect_edge, invert_color, shrink, enlarge, sharpen

class TestImageProcessingFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # dummy for shrink,enlarge,invert
        cls.img = np.ones((100, 100, 3), dtype=np.uint8) * 255  # White image
        cls.gray_img = cv2.cvtColor(cls.img, cv2.COLOR_BGR2GRAY)

        # dummy for blur
        cls.chessboard = np.zeros((100, 100, 3), dtype=np.uint8)
        square_size = 100 // 10
        for i in range(10):
            for j in range(10):
                if (i + j) % 2 == 0:
                    # Fill the square with white (255)
                    cls.chessboard[i * square_size:(i + 1) * square_size, j * square_size:(j + 1) * square_size] = 255

        #dummy for sharpen, edge, hist
        cls.sharpenimg = np.zeros((100, 100,3), dtype=np.uint8)
            # Draw grey + white circles in the center
        center = (100 // 2, 100 // 2)
        radius = 100 // 4  # Radius of the circle
        cv2.circle(cls.sharpenimg, center, radius, 255, -1)

        center2 = (100 // 2, 100 // 2)
        radius2 = 100 // 8  # Radius of the circle
        cv2.circle(cls.sharpenimg, center2, radius2, 125, -1)

    def test_histEqualize(self): #
        gray_img = grayscale(self.sharpenimg)
        eq_img = histEqualize(gray_img)
        self.assertEqual(eq_img.shape, gray_img.shape)
        self.assertNotEqual(np.sum(eq_img), np.sum(gray_img))

    def test_grayscale(self):
        gray_img = grayscale(self.img)
        self.assertEqual(len(gray_img.shape), 2)
        self.assertEqual(gray_img.shape, (100, 100))

    def test_blur(self):
        blurred_img = blur(self.chessboard)
        self.assertEqual(blurred_img.shape, self.chessboard.shape)
        # Check that the image has been blurred by comparing pixel values
        self.assertTrue(np.std(blurred_img) < np.std(self.chessboard), "Blurred image should have lower standard deviation")

    def test_detect_edge(self): #
        edges = detect_edge(self.sharpenimg)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        self.assertEqual(edges.shape, self.sharpenimg.shape)
        self.assertTrue(np.any(edges))

    def test_invert_color(self):
        inverted_img = invert_color(self.img)
        self.assertEqual(inverted_img.shape, self.img.shape)
        self.assertTrue(np.all(inverted_img == 0))

    def test_shrink(self):
        shrunk_img = shrink(self.img)
        self.assertEqual(shrunk_img.shape, (50, 50, 3))

    def test_enlarge(self):
        enlarged_img = enlarge(self.img)
        self.assertEqual(enlarged_img.shape, (200, 200, 3))

    def test_sharpen(self): #
        sharpened_img = sharpen(self.sharpenimg)
        self.assertEqual(sharpened_img.shape, self.img.shape)
        self.assertTrue(np.mean(sharpened_img) != np.mean(self.img))

if __name__ == '__main__':
    unittest.main()
