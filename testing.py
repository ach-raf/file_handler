from file_handler import FileManipulation
_product = {
            'name': 'x',
            'description': '_product_description',
            'category': '_product_category',
            'ranges': '_product_ranges',
            'image_name': '{_media_name}.jpg',
            'pdf_name': '{_media_name}.pdf',
        }
json_handler = FileManipulation('./products')
json_handler.write_to_disk('test', 'json', _product)
