from PIL import Image

class ImageProcessor:
    """Classe para processar imagens."""

    @staticmethod
    def resize_image(input_path, output_path, size):
        """Redimensiona a imagem para o tamanho especificado."""
        with Image.open(input_path) as img:
            img = img.resize(size)
            img.save(output_path)
            return output_path

    @staticmethod
    def convert_to_grayscale(input_path, output_path):
        """Converte a imagem para escala de cinza."""
        with Image.open(input_path) as img:
            grayscale_img = img.convert("L")
            grayscale_img.save(output_path)
            return output_path
