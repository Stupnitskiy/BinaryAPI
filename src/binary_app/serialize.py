from flask import jsonify

def get_list(collection):
    serialized_data = {
        'amount': len(collection),
        'files': [serialize_file(file) for file in collection]

    }
    return jsonify(serialized_data)


def put(data):
    return jsonify(serialize_file(data))


def serialize_file(data):
    return {
        'name': data.name,
        'size': data.size,
    }