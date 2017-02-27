from botsock.utils import get_data_info


def test_return_value_of_get_data_info():
    data = 'a'
    assert '(type - str, length - 1)' == get_data_info(data)
