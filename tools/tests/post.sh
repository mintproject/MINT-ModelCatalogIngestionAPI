DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/env

if [ "$#" -ne 2 ] ; then
    echo "Illegal number of parameters"
    echo "bash post.sh datasetspecifications cycles_crop.json"
    exit 1
fi
CLASS=$1
FILE=$2
echo "Inserting a $CLASS"
payload=$(cat $FILE)
echo $TOKEN
curl -v -X POST "$SERVER/$CLASS" -H "Authorization: Bearer $TOKEN" -H "accept: */*" -H "Content-Type: application/json" -d "$payload"
