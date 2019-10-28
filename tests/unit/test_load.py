from io import TextIOBase

import csv

from price_searcher_app.products import load


def test_get_open_local_gzip(mocker):
    # act
    file_ = load.open_local_gzip('files/products.csv.gz')

    # assert
    assert isinstance(file_, TextIOBase)


def test_csv_to_dicts():
    # arrange
    file_ = open('files/test_products.csv', 'rt')

    # act
    raw_dicts = load.csv_to_dicts(file_)

    # assert
    assert isinstance(raw_dicts, csv.DictReader)

    raw_dicts_list = list(raw_dicts)
    assert len(raw_dicts_list) == 9

    for raw_dict in raw_dicts_list:
        dict_vals = raw_dict.values()
        assert len(dict_vals) == 6
        for val in dict_vals:
            # assert the leading space was skipped
            assert ' ' not in val


def test_get_remote_file_json(mocker):
    # arrange
    response_mock = mocker.Mock()
    requests_mock = mocker.patch.object(
        load.requests,
        'get',
        return_value=response_mock
    )

    # act
    load.get_remote_file_json('www.website.with.json.com')

    # assert
    requests_mock.assert_called_once()
    response_mock.json.assert_called_once()
