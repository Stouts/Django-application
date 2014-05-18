""" Test main. """


def test_home(client):
    """ Ensure the home page works. """
    response = client.get('/')
    assert response.status_code == 200


def test_admin(client):
    """ Ensure the admin works. """
    response = client.get('/desk/')
    assert response.status_code == 200
