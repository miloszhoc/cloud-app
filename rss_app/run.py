import os

from rss_app import create_app

if __name__ == "__main__":
    app = create_app(os.environ['CONFIG'])
    app.run()
