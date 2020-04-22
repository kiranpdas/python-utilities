from cryptography.fernet import Fernet


class Crypter:

    def __init__(self):
        __key = None
        __data = None

    # helpers
    def __load_data_from_file(self, filename):
        """Returns the data from the given filename
        """
        with open(filename, "rb") as file:
            data = file.read()

        return data

    def __write_data_to_file(self, data, filename):
        """Writes the given data to given filename
        """
        with open(filename, "wb") as file:
            file.write(data)

    # properties
    @property
    def key(self):
        return self.__key

    @property
    def data(self):
        return self.__data

    # operations on key
    def generate_key(self):
        """Generates a key and save it into a file with given filename
        """
        self.__key = Fernet.generate_key()

    def load_key_from_file(self, filename):
        """Generates a key and save it into a file with given filename
        """
        self.__key = self.__load_data_from_file(filename)

    def save_key_to_file(self, filename):
        """Saves the key to given filename
        """
        self.__write_data_to_file(self.__key, filename)

    # operations on data
    def encrypt_data_from_file(self, filename):
        """Encrypts the data from the file with given filename
        """
        data = self.__load_data_from_file(filename)
        f = Fernet(self.__key)
        self.__data = f.encrypt(data)

    def decrypt_data_from_file(self, filename):
        """Decrypts the data from the file with given filename
        """
        data = self.__load_data_from_file(filename)
        f = Fernet(self.__key)
        self.__data = f.decrypt(data)

    def save_data_to_file(self, filename):
        """Saves the current data to file with given filename
        """
        self.__write_data_to_file(self.__data, filename)
