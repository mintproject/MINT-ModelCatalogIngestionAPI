rsync --delete -av /Users/mosorio/repos/OBA/outputs/modelcatalog/servers/python/server/ server
gco -- server/.env server/docker-compose.yml server/openapi_server/settings/config.ini server/openapi_server/test/__init__.py server/openapi_server/test/input_tests/model_configuration_without_id.json server/openapi_server/test/input_tests/model_configuration_without_id_causal_diagram_not_equal.json
rm -rf server/openapi_server/controllers/default_controller.py server/.travis.yml server/.gitignore server/queries/queries/
rsync --delete -av /Users/mosorio/repos/OBA/outputs/modelcatalog/servers/python/openapi.yaml openapi.yaml
