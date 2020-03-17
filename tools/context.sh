URL1=https://mintproject.github.io/Mint-ModelCatalog-Ontology/release/1.3.0/ontology.xml
URL2=https://knowledgecaptureanddiscovery.github.io/SoftwareDescriptionOntology/release/1.4.0/ontology.xml
java -jar owl2jsonld-0.3.0-SNAPSHOT-standalone.jar $URL1 > a.json
java -jar owl2jsonld-0.3.0-SNAPSHOT-standalone.jar $URL2 > b.json
jq -s '.[0] * .[1]' a.json b.json  | jq -S > context.json
rm a.json b.json
