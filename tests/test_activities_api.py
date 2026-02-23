def test_root_redirects_to_static_index(client):
    # Arrange
    target_path = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (302, 307)
    assert response.headers["location"] == target_path


def test_get_activities_returns_all_activities_and_no_cache_header(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in payload
    assert "participants" in payload[expected_activity]
    assert response.headers["cache-control"] == "no-store, no-cache, must-revalidate, max-age=0"