
from pydantic import BaseModel, Field



class BussinessOverview(BaseModel):
    summary: str = Field(description="clear one-paragraph business summary")
    primary_target_audience: str = Field(description="specific audience description(one primary target)")
    core_pain_point: str = Field(description="Main problem this audience has(One core piain point)")
    unique_value_proposition: str = Field(description="Why this bussiness wins(One clear advantage)")
    not_priority: str = Field(description="What should be avoided or deprioritized ") 
