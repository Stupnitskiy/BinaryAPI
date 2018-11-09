from flask import jsonify


def _serialize_file(data):
    return {
        'key': data.name,
        'size': data.size,
    }


def get_list(collection):
    serialized_data = {
        'amount': len(collection),
        'files': [_serialize_file(file) for file in collection]

    }
    return jsonify(serialized_data)


def put(data):
    return jsonify(_serialize_file(data))


def delete(data):
    return jsonify(_serialize_file(data))