# Image Processor

Um pacote simples para processamento de imagens em Python que permite redimensionar imagens e convertê-las para escala de cinza.

## Instalação

```bash
pip install image_processor
```

## Uso

```python
from image_processor import ImageProcessor

# Redimensionar imagem
ImageProcessor.resize_image('input.jpg', 'output_resized.jpg', (100, 100))

# Converter para escala de cinza
ImageProcessor.convert_to_grayscale('input.jpg', 'output_grayscale.jpg')
```

## Testes

Para rodar os testes, execute:

```bash
python -m unittest discover -s tests
```
