class TestAuthRouter:
    def test_login(self, client):
        response = client.post(
            "/api/v1/auth/login",
        )
        assert response.status_code == 200
        assert response.json()["message"] == "로그인 성공"

    def test_register(self, client):
        response = client.post(
            "/api/v1/auth/register",
        )
        assert response.status_code == 200
        assert response.json()["message"] == "회원가입 성공"
