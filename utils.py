import json
from app.config import *


def load_posts(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_posts_all():
    """возвращает посты"""
    return load_posts(POSTS_PATH)


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя.
    Функция должна вызывать ошибку ValueError если такого пользователя нет и пустой список, если у пользователя
    нет постов."""
    posts = load_posts(POSTS_PATH)

    for post in posts:
        if post['poster_name'] == user_name:
            return post
    return ValueError


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста. Функция должна вызывать ошибку ValueError
    если такого поста нет и пустой список, если у поста нет комментов. """
    pass


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    pass


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору. """
    pass

print(get_posts_by_user("leso"))
