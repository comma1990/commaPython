# @Author  :  comma 
# @Date    :  2020-12-30 21:50


class TVshow:
    film_lst=['战狼2','红海行动','西游记女儿国','熊出没']
    def __init__(self,film_name):
        self.film_name=film_name
        print(f'正在播放《{self.film_name}》')
        print(f'您可以从{self.film_lst}中选择要点播的电影')

    def show(self,film):
        print(f'您选择了《{film}》,稍后将播放')

myshow=TVshow('红海行动')
name=str(input('请输入你想要的观看的电影：'))
myshow.show(name)