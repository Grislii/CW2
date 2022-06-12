import pytest

from app.posts.dao.posts_dao import PostsDAO
from app.config import *


class TestPostsDao:

    @pytest.fixture
    def posts_dao(self):
        return PostsDAO(f"{POSTS_PATH}")

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_get_all_check_type(self, posts_dao):
        """ Проверка всех постов на правильность типов """
        posts = posts_dao.get_all()
        assert type(posts) == list, "Список постов должен быть списком"
        assert type(posts[0]) == dict, "Элементы списка должны быть словарём"

    def test_get_all_has_keys(self, posts_dao, keys_expected):
        """ Проверка правильной структуры ключей """
        posts = posts_dao.get_all()
        for post in posts:
            post = post
            post_keys = set(post.keys())
            print(keys_expected)
            print(post_keys)
            assert post_keys == keys_expected, "Полученные ключи неверны"

    def test_get_one_check_type(self, posts_dao):
        """ Получение одного поста """
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, "Пост должен быть словарем"

    def test_get_one_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_post_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == keys_expected, "Полученные ключи неверны"

    parameters_to_get_by_pk = []
    for post in PostsDAO(f"{POSTS_PATH}").get_all():
        parameters_to_get_by_pk.append(post['pk'])

    @pytest.mark.parametrize("post_pk", parameters_to_get_by_pk)
    def test_get_one_check_type_has_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_post_by_pk(post_pk)
        assert post["pk"] == post_pk, "Номер полученного поста не соответстуент номеру запрошенного"

    # parameters_to_get_by_poster_name = []
    # for post in PostsDAO(f"{POSTS_PATH}").get_all():
    #     parameters_to_get_by_poster_name.append(post['poster_name'])
    #
    # @pytest.mark.parametrize("poster_name", parameters_to_get_by_poster_name)
    # def test_get_by_user(self, posts_dao, poster_name):
    #     #assert False, type(poster_name)
    #     post = posts_dao.get_by_user(poster_name)
    #     assert post["poster_name"] == poster_name, "Имя создателя поста не совпадает"
