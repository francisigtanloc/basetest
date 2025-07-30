FROM baserow/backend:1.34.5

USER root

COPY ./plugins/basetest/ $BASEROW_PLUGIN_DIR/basetest/
RUN /baserow/plugins/install_plugin.sh --folder $BASEROW_PLUGIN_DIR/basetest

USER $UID:$GID
