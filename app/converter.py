from PIL import Image
import pillow_heif


class converter:
    def convert_heic(self, input_path, output_path, format):
        for file in input_path:
            file_output = f"{output_path}/{self.extract_filename(file)}.{format}"
            heif_file = pillow_heif.open_heif(file)
            img = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
            img.save(file_output, format)

    def extract_filename(self, file_path):
        file_name_with_extension = file_path.split("/")[-1]
        file_name = file_name_with_extension.split(".")[0]

        return file_name