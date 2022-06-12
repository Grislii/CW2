import json


class BookmarksDao:

    def __init__(self, path):
        self.path = path

    def _load(self):
        """ Загружает закладки из bookmarks.json """
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_all(self):
        """ Возвращает все закладки """
        return self._load()

    def get_by_pk(self, pk):
        """ Возвращает закладку по pk """
        bookmarks = self.get_all()
        for bookmark in bookmarks:
            if bookmark['pk'] == pk:
                return bookmark

    def add_bookmark(self, posts):
        """ Добавляет закладку """
        with open(self.path, "w+", encoding="utf-8") as file:
            json.dump(posts, file)

    def is_exists_post(self, post):
        """ Проверяет существует ли такой пост в закладках """
        bookmarks = self.get_all()

        for bookmark in bookmarks:
            if post == bookmark:
                return True
        return False

    def delete_bookmark(self, post):
        """ Удаляет пост из закладок"""
        bookmarks = self.get_all()
        new_bookmarks = []

        for bookmark in bookmarks:
            if post != bookmark:
                new_bookmarks.append(bookmark)

        with open(self.path, "w+", encoding="utf-8") as file:
            json.dump(new_bookmarks, file)

    def get_all_pk(self):
        """ Получает все pk из закладок """
        bookmarks = self.get_all()
        pk_list = []

        for bookmark in bookmarks:
            pk_list.append(bookmark['pk'])

        return pk_list