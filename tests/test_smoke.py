from hello_web.app import create_app

def test_index_route():
    app = create_app()
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200

def test_api_hello():
    app = create_app()
    client = app.test_client()
    r = client.get('/api/hello')
    assert r.json == {"message": "Hello from Flask!"}