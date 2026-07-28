FROM grafana/grafana-oss:13.0.2

RUN grafana cli plugins install grafana-mqtt-datasource
RUN grafana cli plugins install marcusolsson-json-datasource


# the <path>/. should recursively copy  - using --parent when it is officially part of docker spec might be better
COPY ./files/provisioning/. /var/lib/grafana/provisioning/
COPY ./files/grafana.ini /var/lib/grafana/grafana.ini

COPY --from=solution_config ./dashboards /var/lib/grafana/dashboards
COPY --from=solution_config ./datasources/. /var/lib/grafana/provisioning/datasources/

