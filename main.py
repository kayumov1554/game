from flask import Flask, jsonify
import asyncio
from contextlib import suppress
from bot.utils.launcher import process

app = Flask(__name__)

@app.route('/start', methods=['GET'])
def start_process():
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
    return jsonify({"status": "process started"})

async def main():
    await process()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
