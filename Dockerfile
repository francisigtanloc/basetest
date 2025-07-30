FROM baserow/baserow:1.34.5

COPY ./plugins/basetest/ /baserow/plugins/basetest/
RUN /baserow/plugins/install_plugin.sh --folder /baserow/plugins/basetest
