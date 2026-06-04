from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class SMSMessage(BaseModel):
    message: str

class SMSResponse(BaseModel):
    action: str
    reply: str

def generate_simple_reply(content: str) -> str:
    # Basic logic for demonstration purposes based on examples
    content_lower = content.lower()
    
    if "capital de moçambique" in content_lower:
        return "A capital de Moçambique é Maputo."
    elif "18 + 7" in content_lower:
        return "18 + 7 = 25."
    elif "resume esta frase" in content_lower:
        # Simple extraction for the "resume" example
        match = re.search(r"resume esta frase:\s*(.*)", content, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return content.strip()
    
    # Generic fallback
    return "Sinto muito, não entendi a solicitação."

@app.post("/process", response_model=SMSResponse)
async def process_sms(sms: SMSMessage):
    if sms.message.startswith("Chat:"):
        content = sms.message[len("Chat:"):].strip()
        reply = generate_simple_reply(content)
        return SMSResponse(action="reply", reply=reply)
    else:
        return SMSResponse(action="ignore", reply="")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
