def expect_response(page, url_fragment):
    return page.expect_response(
        lambda response:
        url_fragment in response.url and response.ok
    )