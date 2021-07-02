def test_download_page_without_resources(requests_mock, tmpdir):
    page_url = 'http://test.com'
    requests_mock.get(page_url, text='<html></html>')
    download(page_url, str(tmpdir))
    resources_dir_path = tmpdir / 'test-com_files'
    assert os.path.isfile(tmpdir / 'test-com.html')
    assert not os.path.isdir(resources_dir_path)
def test_download_unavailable_page(requests_mock, tmpdir):
    page_url = 'http://test.com'
    requests_mock.get(page_url, status_code=HTTPStatus.NOT_FOUND)
    with pytest.raises(RequestException):
        download(page_url, str(tmpdir))
