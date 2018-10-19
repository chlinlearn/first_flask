#encoding:utf-8
#从flask框架导入flask这个类
from flask import Flask,render_template,redirect,url_for

#初始化一个flask对象
#flask()
'''
需要传递一个参数__name__
1.方便flask框架寻找资源
2.方便flask插件比如flask-Sqlalchemy出现错误时，方便寻找出错的位置
'''


app = Flask(__name__)



#app.route是一个装饰器，@开头，并且在函数的上面，说明是装饰器
#装饰器的作用是做一个URL与视图函数的映射
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')
    # books=[
    #     {
    #         'name':'西游记',
    #         'author':'吴承恩',
    #         'price':209
    #     },
    #     {
    #         'name': '红楼梦',
    #         'author': '曹雪芹',
    #         'price': 212
    #     },
    #     {
    #         'name': '三国演义',
    #         'author': '罗贯中',
    #         'price': 300
    #     },
    #     {
    #         'name': '水浒传',
    #         'author': '施耐庵',
    #         'price': 189
    #     }
    # ]
    # return render_template('index.html',books=books)
    # user={
    #     'username':'xcl',
    #     'age':20
    # }
    # return   render_template('index.html',user=user)
#     #重定向
#     login_url=url_for('login')
#     return redirect(login_url)
#     return '这是首页'
#
# @app.route('/login/')
# def login():
#     return '这是登录页面'

# @app.route('/question/<is_login>')
# def question(is_login):
#     if is_login=='1':
#         return '这是发布问答页面'
#     else:
#         return redirect(url_for('login'))

    # class Person(object):
    #     name='abc'
    #     age=18
    # p=Person()
    #
    # #使用字典定义
    # context_dict={
    #     'username':'xcl',
    #     'gender':'男',
    #     'age':20,
    #     #访问模型中的属性
    #     'person':p,
    #     'website':{
    #         'baidu':'www.baidu.com',
    #         'google':'www.google.com'
    #     }
    # }
    # return render_template('index.html',**context_dict)


#如果当前这个文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    #app.run()启动应用服务器，接受用户请求
    #while True:
    #listen()
    app.run(debug=True)
