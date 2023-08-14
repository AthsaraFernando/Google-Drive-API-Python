from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scopes and credentials JSON file
SCOPES = ['https://www.googleapis.com/auth/drive.file']
CREDENTIALS_JSON_FILE = 'credentials.json'

# Create a flow object to authenticate and authorize
flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_JSON_FILE, SCOPES)
credentials = flow.run_local_server()

# Build the Drive API service
drive_service = build('drive', 'v3', credentials=credentials)

# Upload the file
file_name = 'text.txt'
file_metadata = {'name': file_name}
media = MediaFileUpload(file_name, mimetype='text/plain')
uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print(f"File '{file_name}' uploaded with ID: {uploaded_file['id']}")

#testing