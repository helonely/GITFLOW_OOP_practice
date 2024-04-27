import pytest

from src.article import Article


@pytest.fixture
def one_article():
    Article.articles = dict()
    return Article.insert("test1", "test1")


@pytest.fixture
def two_articles():
    Article.articles = dict()
    Article.insert('test1', 'test1')
    return Article.insert('test1', 'test1')


def test_insert(one_article):
    """
    Тест для проверки, что кол-во статей равно единице
    """
    assert len(Article.articles) == 1


def test_article_id(one_article):
    """
    Тест на проверку установки ID статей
    """
    assert one_article.article_id == 1


def test_increase_id(two_articles):
    """
    Тест на проверку увеличения ID статей
    """
    assert two_articles.article_id == 2


def test_increase_article_count(two_articles):
    """Тест на увеличение списка статей"""
    assert len(Article.articles) == 2
