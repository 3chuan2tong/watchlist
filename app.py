import os
import sys
import click
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# 确定数据库文件前缀
prefix = 'sqlite:///' if sys.platform.startswith('win') else 'sqlite:////'

# 配置 Flask 应用
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy
db = SQLAlchemy(app)

# 定义用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

# 定义电影模型
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    year = db.Column(db.String(4))

# 创建所有表
def create_database(app):
    with app.app_context():  # 创建应用上下文
        try:
            db.create_all()
        except Exception as e:
            click.echo(f'Error creating database: {e}')

create_database(app)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    name = 'sanchuan'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    return render_template('index.html', name=name, movies=movies)

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    with app.app_context():  # 创建应用上下文
        try:
            if drop:
                db.drop_all()
            create_database(app)
            click.echo('Initialized database.')
        except Exception as e:
            click.echo(f'Error initializing database: {e}')
