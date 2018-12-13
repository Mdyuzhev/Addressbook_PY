def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.deletion_first_group()
    app.session.logout()
