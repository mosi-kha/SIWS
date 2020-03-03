from waitress import serve
from app import application


def main():
    serve(application, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
