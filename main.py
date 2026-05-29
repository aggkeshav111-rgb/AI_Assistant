from flask import Flask,url_for,request,flash,render_template,jsonify
import os 
from dotenv import load_dotenv
from openai import OpenAI

app = Flask(__name__)

load_dotenv()
api_key=os.getenv("groq_api_key")
client=OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

#url made=>i.e. endpoint
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask",methods=["POST"])
def ask():
    query=request.form.get("query")
    response=client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {"role":"system","content":"act like a helpful personal assistant"},
            {"role":"user","content":query}
        ],
        temperature=0.2,
        max_output_tokens=512
    )
    answer=response.output_text.strip()
    return jsonify({"response":answer}),200

@app.route("/summarize",methods=["POST"])
def summarize():
    email=request.form.get("email")
    prompt=f"summarize the email in 3-4 sentences :{email}"
    response=client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {"role":"system","content":"act like an expert email assistant"},
            {"role":"user","content":prompt}
        ]
    )
    summary=response.output_text.strip()
    return jsonify({"response":summary}),200

if __name__=="__main__":
    app.run(debug=True)
