import pytest

from flaskr.db import get_db


def test_update(client, auth, app):
    auth.login()
    assert client.get("/").status_code == 200
    client.post("/", data={"email": "nuevo@gmail.com"})

    with app.app_context():
        db = get_db()
        post = db.execute("SELECT * FROM user WHERE id = 1").fetchone()
        assert post["title"] == "nuevo@gmail.com"
