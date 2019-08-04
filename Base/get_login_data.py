import os

import yaml


class Get_Login_Data:
    def __init__(self):
        pass

    def get_yaml_data(self, yaml_name):
        """
        返回yaml文件的数据
        :return:
        """
        with open('./Data' + os.sep + yaml_name, 'r') as f:
            return yaml.safe_load(f)
