from .settings import CHUNK_SIZE


def send_by_chunks(connection, data):
    first, rest = data[:CHUNK_SIZE], data[CHUNK_SIZE:]
    connection.send(first)
    if rest:
        send_by_chunks(connection, rest)


def recv_by_chunks(connection):
    data_chunk = connection.recv(CHUNK_SIZE)
    if len(data_chunk) == CHUNK_SIZE:
        return data_chunk + recv_by_chunks(connection)
    return data_chunk
