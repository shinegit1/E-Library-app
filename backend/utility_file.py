import os
import enum


class PersonType(enum.Enum):
    LIBRARIAN = ['Librarian', 'librarian']
    CUSTOMER = ['Customer', 'customer']


class FileType(enum.Enum):
    PDF = ['.pdf', '.PDF']
    IMAGE = ['.png', '.jpg', '.jpeg']


def validate_pdf_extension(value):
    # check the file extension is in pdf format or not
    file_extension = os.path.splitext(value.name)[1]
    if file_extension == FileType.PDF.value:
        return file_extension
    else:
        raise ValueError("Invalid file type. Only PDF file accepted.")


def validate_image_extension(value) -> str:
    # check the image file extension valid or not
    file_extension = os.path.splitext(value.name)[1]
    if file_extension in FileType.IMAGE.value:
        return file_extension
    else:
        raise ValueError("Invalid file type passed.")


def new_filename(file, title: str):
    # Returns a file with new name set by title of pdf book
    file_extension = os.path.splitext(file.name)[1]
    file.name = title + file_extension
    return file


def delete_old_path(path: str) -> None:
    # function delete given path from the system
    if os.path.exists(path):
        os.remove(path)