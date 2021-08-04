import yaml
import os



#读取yaml文件
def  read_yaml():
    with open(os.getcwd()+'/extract.yaml',encoding='utf-8') as f:#打开yaml文件
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

#写入yaml文件,mode='a'表示追加的方式写入
def  write_yaml(data):
    with open(os.getcwd()+'/extract.yaml',encoding='utf-8',mode="a") as f:
        yaml.dump(data,stream=f,allow_unicode=True)

#清空yaml文件
def clear_yaml():
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode="w") as f:
        f.truncate()