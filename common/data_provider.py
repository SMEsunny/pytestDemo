import os
from  common.read_data import data


class DataProvider:
    
    #从指定目录中将配置文件加载进字典中
    def load_data_from_dir(self,paths):
        #获得文件列表
        files = self.get_all_files(paths)
        #遍历文件并读取文件写入集合
        self.data = {}
        for file in files:
            fileName = str(file).split(".")[0]
            fileName = os.path.relpath(fileName,start=os.getcwd()).replace("\\","/")
            type = str(file).split(".")[1]
            if type == "yml":
                self.data[fileName] = data.load_yaml(file)
            elif type == "ini":
                self.data[fileName] = data.load_ini(file)
            elif type == "json":
                self.data[fileName] = data.load_json(file)
            else:
                raise Exception("暂不支持读写该文件")
            
        return self.data
    
    #通过文件相对与项目路径取数据
    def get_data(self,path):
        return self.data[path]
    
     
    
    def get_all_files(self,paths, base_path=None):
        """
        获取一个或多个目录及其子目录下的所有文件的相对路径，或直接返回传递的文件路径。
        
        :param paths: 单个目录、文件路径的字符串或目录、文件路径的列表
        :param base_path: 指定的基准目录路径，从中生成文件的相对路径。如果为None，则使用当前工作目录。
        :return: 所有文件相对于base_path的相对路径列表
        """
        
        # 如果传入的paths是字符串，则将其转换为列表
        if isinstance(paths, str):
            paths = [paths]

        # 如果没有提供基准路径，使用当前工作目录
        if base_path is None:
            base_path = os.getcwd()

        # 初始化文件列表
        files_list = []

        # 循环遍历传入的路径列表
        for path in paths:
            path = base_path + path
            if os.path.isfile(path):
                # 如果是文件，直接添加
                files_list.append(path)
            elif os.path.isdir(path):
                # 如果是目录，遍历目录下的所有文件
                for root,dir,files in os.walk(path):
                    for file in files:
                        # 去除__init__.py文件
                        if file != "__init__.py":
                            # 构造文件的绝对路径
                            file_path = os.path.join(root, file)
                            # 添加文件
                            files_list.append(file_path)

        return files_list
    
    
if __name__ == "__main__":
    data_provider = DataProvider()
    # print(data_provider.get_all_files(["/data","/config"]))
    print(data_provider.load_data_from_dir("/config"))
    data_provider.get_data("/config/setting")