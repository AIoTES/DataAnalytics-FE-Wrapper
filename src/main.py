import logging
import sys

from flask import Flask

from src import settings
from src.controllers import wrapper_method_controller
from src.services.data_lake_service import QueryDataLake
from src.services.wrapper_method_impl import WrapperMethodImpl

application = Flask(__name__)

if not settings.ANALYTICS_SERVER:
    logging.critical('{} environment var not initialiced. The system will be closed.'.format(['ANALYTICS SERVER']))
    sys.exit(1)

wrapper_service = WrapperMethodImpl(settings.ANALYTICS_SERVER)
data_lake_service = QueryDataLake()

wrapper_method_controller.wrapperMethod = wrapper_service
wrapper_method_controller.queryDataLake = data_lake_service

application.register_blueprint(wrapper_method_controller.api, url_prefix='/wrapperMethod')

if __name__ == '__main__':
    application.run(settings.REST_URL, settings.REST_PORT)
