from application import application
from bs4 import BeautifulSoup


def test_index_route():
    response = application.test_client().get("/")
    assert response.status_code == 200


def test_find_palindrome_post_route():
    response = application.test_client().post(
        "/lengthPalindrome", data={"input": "bbaaa"}
    )
    soup = BeautifulSoup(response.data, features="html.parser")
    assert soup.find("div", {"class": "alert"}).text == "\n          aaa\n        "
    assert response.status_code == 200
