FROM grafana/grafana-oss:11.1.3


# the <path>/. should recursively copy  - using --parent when it is officially part of docker spec might be better
COPY ./files/provisioning/. /var/lib/grafana/provisioning/
COPY ./files/plugins/. /var/lib/grafana/plugins/
COPY ./files/grafana.ini /var/lib/grafana/grafana.ini

COPY --from=solution_config ./dashboards /var/lib/grafana/dashboards
COPY --from=solution_config ./datasources/. /var/lib/grafana/provisioning/datasources/

ENV GF_INSTALL_PLUGINS="marcusolsson-json-datasource,grafana-mqtt-datasource"
