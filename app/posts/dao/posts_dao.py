import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def _load(self):
        """ Загружает посты из posts.json """
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_all(self):
        """возвращает посты"""
        return self._load()

    def get_by_user(self, user_name):
        """возвращает посты определенного пользователя.
        Функция должна вызывать ошибку ValueError если такого пользователя нет и пустой список, если у пользователя
        нет постов."""
        posts = self.get_all()
        posts_by_user = []

        for post in posts:
            if post['poster_name'] == user_name:
                posts_by_user.append(post)
        return posts_by_user

    def get_comments_by_pk(self, post_id):
        """возвращает комментарии определенного поста. Функция должна вызывать ошибку ValueError
        если такого поста нет и пустой список, если у поста нет комментов. """
        pass

    def search_for_posts(self, query):
        """возвращает список постов по ключевому слову"""
        posts = self.get_all()
        matching_posts = []

        query_lower = query.lower()

        for post in posts:
            if query_lower in post['content'].lower():
                matching_posts.append(post)
        return matching_posts

    def get_post_by_pk(self, pk):
        """возвращает один пост по его идентификатору. """
        posts = self.get_all()

        for post in posts:
            if post['pk'] == pk:
                return post
        raise ValueError
