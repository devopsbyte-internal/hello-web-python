from __future__ import annotations
import argparse
from flask import Flask, jsonify, render_template

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/api/hello")
    def api_hello():
        return jsonify({"message": "Hello from Flask!"})

    return app

def main() -> None:
    parser = argparse.ArgumentParser(description="hello-web demo server")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5173, help="Port (default: 5173)")
    parser.add_argument("--debug", action="store_true", help="Enable debug reload")
    args = parser.parse_args()

    app = create_app()
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == "__main__":
    main()