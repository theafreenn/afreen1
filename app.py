from flask import Flask, render_template, request
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

app = Flask(__name__)

gauth = GoogleAuth()
client_config = {
    "client_id": "537226443014-dg242kpmnvn6itftg7o79uj26jlmnffs.apps.googleusercontent.com",
    "client_secret": "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",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "redirect_uris": ["https://exper-mocha.vercel.app/"],
    "revoke_uri": "https://oauth2.googleapis.com/revoke"
}

gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    gfile = drive.CreateFile({'title': file.filename})
    gfile.SetContentString(file.read().decode("latin-1"))  # Adjust encoding if needed
    gfile.Upload()

    return "File uploaded successfully to Google Drive!"


if __name__ == "__main__":
    app.run(debug=False)
