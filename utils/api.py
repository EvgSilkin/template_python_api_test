from utils.Http_methods import Http_methods

"""Методы для тестирования Google maps api"""

base_url = ""
key = ""

class Model_api():
    @staticmethod
    def create_model(json_model):
        result_post = Http_methods.post(base_url, json_model)
        return result_post
    @staticmethod
    def get_model(id):
        url = base_url + id
        result_get = Http_methods.get(url)
        return result_get
    @staticmethod
    def put_model(id, json_model):
        url = base_url + id
        result_put = Http_methods.put(url, json_model)
        return result_put
    @staticmethod
    def delete_new_place(id, json_model):
        url = base_url + id
        result_delete = Http_methods.delete(url, json_model)
        return result_delete