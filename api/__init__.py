from flask import Flask

app = Flask(__name__)

import api.views.user_view
import api.models.user
