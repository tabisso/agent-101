
from pydantic import BaseModel, Field
from typing import List     



class BussinessOverview(BaseModel):
    summary: str = Field(description="clear one-paragraph business summary")
    primary_target_audience: str = Field(description="specific audience description(one primary target)")
    core_pain_point: str = Field(description="Main problem this audience has(One core piain point)")
    unique_value_proposition: str = Field(description="Why this bussiness wins(One clear advantage)")
    not_priority: str = Field(description="What should be avoided or deprioritized ") 



class MarketingChannel(BaseModel):
    channel_name: str = Field(description="Name of the marketing channel")
    priority: int = Field(description="Priority level of this channel (1 being highest)")
    why_this_channel: str = Field(description="Specific reason for choosingthis channel")



class IgnoredChannel(BaseModel):
    channel_name: str = Field(description="Name of the marketing channel to ignore")
    reason: str = Field(description="Reason for ignoring this channel") 



class MarketingStrategy(BaseModel):
    primary_goal: str = Field(description="The main marketing goal")
    core_message: str = Field(description="The central message to convey")
    channels: List[MarketingChannel] = Field(description="List of 3 channels")
    ignored_channels: IgnoredChannel = Field(description="One marketing channel to ignore with reason")


class EmailCampaign(BaseModel):
    email_number: int = Field(description="Email sequence number")
    objective: str = Field(description="Objective of the email")
    subject : str = Field(description="Subject line of the email")
    body: str = Field(description="Body content of the email")
    call_to_action: str = Field(description="Call to action of the email")


class EmailList(BaseModel):
    emails: List[EmailCampaign] = Field(description="List of 3 email campaigns")

class FinalOutput(BaseModel):
    business_overview: BussinessOverview 
    marketing_strategy: MarketingStrategy 
    email_campaigns: List[EmailCampaign] = Field(description="List of email campaigns")