import pytest

@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    mocker.patch("src.responsegetter.get_preprompt", return_value="solve the question briefly")
    mocker.patch("src.responsegetter.setup_llm", return_value=lambda x: "two or 2")

