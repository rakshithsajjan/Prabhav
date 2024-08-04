import logging

from app import create_app


app = create_app()

if __name__ == "__main__":
    logging.info("app started")
    app.run(debug=False, host="0.0.0.0", port=8000)