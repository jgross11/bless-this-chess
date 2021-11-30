from bless_this_chess import init_app

app = init_app()
if __name__ == '__main__':
    app.run(host='localhost', port=5000)