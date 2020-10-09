from main_backend import createa_app

app=createa_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)