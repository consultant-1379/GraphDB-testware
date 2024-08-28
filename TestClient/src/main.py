#!/usr/bin/env python3

import app
import services.config as config
import routes

app.register_blueprints()
app.flask_app.run(host='0.0.0.0', port=config.port())
