import pytest, plant_api

if __name__ == '__main__':
    app = plant_api.create_app()
    app.run(host='0.0.0.0', debug=True)
    