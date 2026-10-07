from pydantic import BaseModel, Field

class TaskRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000, description="Input text to process")

class TaskResponse(BaseModel):
    task: str = Field(..., description="Name of the executed task")
    content: str = Field(..., description="Generated text response from the model")
    tokens: int = Field(..., description="Total tokens used")
    model: str = Field(..., description="Model name utilized for generation")