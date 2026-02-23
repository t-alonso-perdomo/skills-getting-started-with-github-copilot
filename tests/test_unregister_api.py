def test_unregister_removes_student_successfully(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": student_email})
    payload = response.json()
    activities_response = client.get("/activities")
    activities_payload = activities_response.json()

    # Assert
    assert response.status_code == 200
    assert payload["message"] == f"Unregistered {student_email} from {activity_name}"
    assert student_email not in activities_payload[activity_name]["participants"]


def test_unregister_returns_404_when_student_not_signed_up(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "not-signed@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_returns_404_when_activity_does_not_exist(client):
    # Arrange
    activity_name = "Unknown Club"
    student_email = "anyone@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": student_email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"