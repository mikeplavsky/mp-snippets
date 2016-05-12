docker run -i -p 3000:3000 \
    -v $(pwd)/credentials:/usr/share/grafana/.aws/credentials \
    -e "GF_SECURITY_ADMIN_PASSWORD=secret" grafana/grafana
