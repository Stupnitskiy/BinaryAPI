TEST_KEY = 'test_key'
TEST_DATA = 'test_data'

def test_put(client): 
    response = client.put('/api/binary/put', data=dict(
        key=TEST_KEY,
        data=TEST_DATA,
    ))

    json_data = response.get_json()

    assert json_data.get('key') == TEST_KEY
    assert json_data.get('size') == len(TEST_DATA)


def test_getlist(client):
    response = client.get('/api/binary/get')
    json_data = response.get_json()

    expected_data = {
        'key': TEST_KEY,
        'size': len(TEST_DATA),
    }

    assert expected_data in json_data.get('files')


def test_get(client):
    response = client.get('/api/binary/get/%s' % (TEST_KEY))
    data = response.data.decode()

    assert data == TEST_DATA