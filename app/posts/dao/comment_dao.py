import json


class CommentDao:

    def __init__(self, path):
        self.path = path

    def _load(self):
        """ Загружает комментарии из comments.json """
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_all(self):
        """ Получает все комментарии """
        return self._load()

    def get_post_by_pk(self, pk):
        """ Получает коментарий по pk """
        comments = self.get_all()
        matches_comments = []

        for comment in comments:
            if comment['post_pk'] == pk:
                matches_comments.append(comment)
        return matches_comments
