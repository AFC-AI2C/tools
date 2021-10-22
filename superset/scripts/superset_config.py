################################################################################
#                                                                              #
#  All the parameters and default values defined in                            #
#  https://github.com/apache/incubator-superset/blob/master/superset/config.py #
#  can be altered in your local superset_config.py                             #
#                                                                              #
################################################################################

import os

if "SUPERSET_HOME" in os.environ:
    DATA_DIR = os.environ["SUPERSET_HOME"]
else:
    DATA_DIR = os.path.join(os.path.expanduser("~"), ".superset")

# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------
ROW_LIMIT = 50000

VIZ_ROW_LIMIT = 10000

# max rows retreieved when requesting samples from datasource in explore view
SAMPLES_ROW_LIMIT = 1000

# max rows retrieved by filter select auto complete
FILTER_SELECT_ROW_LIMIT = 10000

# This is an important setting, and should be lower than your
# [load balancer / proxy / envoy / kong / ...] timeout settings.
# You should also make sure to configure your WSGI server
# (gunicorn, nginx, apache, ...) timeout setting to be <= to this setting
SUPERSET_WEBSERVER_TIMEOUT = 60

# this 2 settings are used by dashboard period force refresh feature
# When user choose auto force refresh frequency
# < SUPERSET_DASHBOARD_PERIODICAL_REFRESH_LIMIT
# they will see warning message in the Refresh Interval Modal.
# please check PR #9886
SUPERSET_DASHBOARD_PERIODICAL_REFRESH_LIMIT = 0

SUPERSET_DASHBOARD_PERIODICAL_REFRESH_WARNING_MESSAGE = None

SUPERSET_DASHBOARD_POSITION_DATA_LIMIT = 65535

CUSTOM_SECURITY_MANAGER = None

SQLALCHEMY_TRACK_MODIFICATIONS = False

# ---------------------------------------------------------
# Flask App Builder configuration
# ---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.getenv(
    "SUPERSET_SECRET_KEY", default="\2\1thisismyscretkey\1\2\\e\\y\\y\\h"
)

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
# SQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/superset.db'
SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(
    DATA_DIR, "superset.sqlite"
)

# In order to hook up a custom password store for all SQLACHEMY connections
# implement a function that takes a single argument of type 'sqla.engine.url',
# returns a password and set SQLALCHEMY_CUSTOM_PASSWORD_STORE.
#
# e.g.:
# def lookup_password(url):
#     return 'secret'
# SQLALCHEMY_CUSTOM_PASSWORD_STORE = lookup_password
SQLALCHEMY_CUSTOM_PASSWORD_STORE = None

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []

# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ""


# Allows you to use sqlite databases
PREVENT_UNSAFE_DB_CONNECTIONS = False

# Superset Improvement Proposal 15 aims to ensure that time intervals are handled in a consistent and transparent manner for both the Druid and SQLAlchemy connectors.
# Prior to SIP-15 SQLAlchemy used inclusive endpoints however these may behave like exclusive for string columns (due to lexicographical ordering) if no formatting was defined and the column formatting did not conform to an ISO 8601 date-time (refer to the SIP for details).
SIP_15_ENABLED = True


# # For chart data, Superset goes up a “timeout search path”, from a slice's configuration to the datasource’s, the database’s, then ultimately falls back to the global default defined in DATA_CACHE_CONFIG.
# DATA_CACHE_CONFIG = {
#     'CACHE_TYPE': 'redis',
#     'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24, # 1 day default (in secs)
#     'CACHE_KEY_PREFIX': 'superset_results',
#     'CACHE_REDIS_URL': 'redis://localhost:6379/0',
# }
