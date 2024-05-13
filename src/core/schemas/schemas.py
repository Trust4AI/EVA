from pydantic import BaseModel


class TestResult(BaseModel):
    input: str
    output: str
    evaluation_result: str
    evaluation_type: str


class Input(BaseModel):
    query: str
    type: str
    expected_result: str

    class Config:
        from_attributes = True

class Output(BaseModel):
    expected_result: str
    generated_result: str

    class Config:
        from_attributes = True
