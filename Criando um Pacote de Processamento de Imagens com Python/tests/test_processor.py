import unittest
import os
from image_processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):

    def setUp(self):
        self.input_image_path = 'test_image.jpg'  # Coloque uma imagem de teste nesse caminho
        self.resized_image_path = 'resized_image.jpg'
        self.grayscale_image_path = 'grayscale_image.jpg'

    def test_resize_image(self):
        output_path = ImageProcessor.resize_image(self.input_image_path, self.resized_image_path, (100, 100))
        self.assertTrue(os.path.exists(output_path))

    def test_convert_to_grayscale(self):
        output_path = ImageProcessor.convert_to_grayscale(self.input_image_path, self.grayscale_image_path)
        self.assertTrue(os.path.exists(output_path))

    def tearDown(self):
        # Remove arquivos criados durante os testes
        if os.path.exists(self.resized_image_path):
            os.remove(self.resized_image_path)
        if os.path.exists(self.grayscale_image_path):
            os.remove(self.grayscale_image_path)

if __name__ == '__main__':
    unittest.main()
