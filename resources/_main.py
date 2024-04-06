from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    # Converte PDF para lista de imagens
    images = convert_from_path(pdf_path)

    # Salva cada imagem em output_folder
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, 'PNG')

    print(f"PDF convertido para imagens. {len(images)} imagens foram salvas em {output_folder}.")

# Caminho para o arquivo PDF que você quer converter
pdf_path = '/var/www/html/sptrans/sptrans.pdf'

# Pasta de saída onde as imagens serão salvas
output_folder = '/var/www/html/sptrans/'

# Chama a função para converter PDF para imagens
pdf_to_images(pdf_path, output_folder)
