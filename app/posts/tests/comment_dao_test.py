import pytest

from app.posts.dao.comment_dao import CommentDao
from app.config import *


class TestCommentDao:

    @pytest.fixture
    def comments_dao(self):
        return CommentDao(COMMENTS_PATH)

    @pytest.fixture
    def post_pk(self):
        parameters_to_get_by_pk = []
        for comment in CommentDao(f"{COMMENTS_PATH}").get_all():
            parameters_to_get_by_pk.append(comment['post_pk'])
        return parameters_to_get_by_pk


    def test_get_all_check_type(self, comments_dao):
        """ Проверка всех комментариев на правильность типов """
        comments = comments_dao.get_all()
        assert type(comments) == list, "Список комментариев должен быть списком"
        assert type(comments[0]) == dict, "Элемент списка постов должен быть словарём"



    # @pytest.mark.parametrize("post_pk", post_pk)
    # def test_post_by_pk(self, comments_dao, post_pk):
    #     # print(type(pk))
    #     # print(type(comments_dao.get_post_by_pk(pk)['pk']))
    #     # comment = comments_dao.get_post_by_pk(pk)
    #     # assert comment['pk'] == pk, "Ключи комментариев должны совпадать"
