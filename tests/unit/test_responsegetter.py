from src import responsegetter

def test_get_response(mocker):
    input_data = "whats 1+1"

    response = responsegetter.get_response(input_data)
    
    assert len(response) > 0
    twoinresponse = "2" in response
    twostringresponse = "two" in response
    twoisinresponse = twoinresponse or twostringresponse
    assert twoisinresponse

