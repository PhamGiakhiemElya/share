from pyrogram import Client

api_id = 38072560
api_hash = "70b34502e975e8322081b6e4a72ef313"

with Client("assistant_session", api_id=api_id, api_hash=api_hash) as app:
    print("\n\n==> SESSION STRING CỦA BẠN:")
    print(app.export_session_string())
