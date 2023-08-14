import json


class Params:

    def __init__(self, test_params_file_path, env_params_file_path):
        self.params = {
            "test_params_file_name": test_params_file_path,
            "env_params_file_name": env_params_file_path
        }

        test_params_file = open(test_params_file_path)
        data = json.load(test_params_file)

        for key, value in data.items():
            self.params[key] = value

        test_params_file.close()

        env_params_file = open(env_params_file_path)
        data = json.load(env_params_file)

        for key, value in data.items():
            if str(key) == 'env_name':
                self.prefix = value
                self.params[key] = value
            else:
                for key1, value1 in data[key].items():
                    current_key_param = "{}_{}".format(str(key), str(key1))
                    self.params[current_key_param] = value1

        env_params_file.close()

        new_pairs = None

        for key in self.params:
            if str.startswith(key, self.prefix):
                if new_pairs is None:
                    new_pairs = {
                        key[len(self.prefix) + 1:]: self.params[key]
                    }
                else:
                    new_pairs[key[len(self.prefix) + 1:]] = self.params[key]
                if key[len(self.prefix) + 1:] == 'URL':
                    new_pairs[key[len(self.prefix) + 1:]] = self.update_url(self.params[key])

        if new_pairs is not None:
            for key in new_pairs:
                self.params[key] = new_pairs[key]

    @staticmethod
    def update_url(url: str):
        if url is None or url == '':
            raise Exception('URL can not be empty')
        if not url.startswith("https://"):
            url = 'https://' + url
        if not url.endswith('/'):
            url = url + '/'
        return url
