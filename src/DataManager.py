import yaml, os

from pytg.Manager import Manager
from pytg.load import get_module_content_folder

class DataManager(Manager):
    def create_data(self, module, table, object_id):
        return self.save_data(module, table, object_id, self.load_data(module, table, "__default"))

    def load_data(self, module, table, object_id):
        module_folder = get_module_content_folder(module)

        return yaml.safe_load(open("{}/data/{}/{}.yaml".format(module_folder, table, object_id), "r"))

    def save_data(self, module, table, object_id, data):
        module_folder = get_module_content_folder(module)

        yaml.safe_dump(data, open("{}/data/{}/{}.yaml".format(module_folder, table, object_id), "w"))

        return data

    def delete_data(self, module, table, object_id):
        module_folder = get_module_content_folder(module)

        os.remove("{}/data/{}/{}.yaml".format(module_folder, table, object_id))

    def has_data(self, module, table, object_id):
        module_folder = get_module_content_folder(module)

        return os.path.exists("{}/data/{}/{}.yaml".format(module_folder, table, object_id))

    def load_table_entries(self, module, table):
        module_folder = get_module_content_folder(module)

        entries = []

        files = os.listdir("{}/data/{}".format(module_folder, table))
        files.remove("__default.yaml")

        for f in files:
            entry_id = f.replace(".yaml", "")

            data = self.load_data(module, table, entry_id)

            entries.append(data)

        return entries

    def find_entry_by_field(self, module, table, field, value):
        module_folder = get_module_content_folder(module)

        files = os.listdir("{}/data/{}".format(module_folder, table))
        files.remove("__default.yaml")

        for f in files:
            entry_id = f.replace(".yaml", "")

            data = self.load_data(module, table, entry_id)

            if data[field] == value:
                return data

        return None

