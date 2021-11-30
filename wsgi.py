from bless_this_chess import init_app

app = init_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0')

    # for mac use:
    # app.run(host='localhost', port=5000)