FROM baserow/web-frontend:1.34.5

USER root

COPY ./plugins/basetest/ /baserow/plugins/basetest/
RUN /baserow/plugins/install_plugin.sh --folder /baserow/plugins/basetest

USER $UID:$GID
