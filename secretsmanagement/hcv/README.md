# HashiCorp Vault with persistence

## add HashiCorp repo

```
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
```

## deploy HasiCorp Vault

```
helm upgrade --install hcv hashicorp/vault --version 0.26.1  --namespace hcv --create-namespace --values ./values.yaml --wait
```
 
## create vs

```
kubectl apply -f hcv-vs.yaml
```

# create secret

```
kubectl create secret -n hcv generic hcv-secrets --from-literal=root-token=hvs.yvXB...Kcqa --from-literal=unseal-key1=PVIK...rZkE=
```
 
# cURL commands


## status
 
```
$ export VAULT_ADDR=https://hcv.ihc-dt.cluster-3.de
$ vault status -output-curl-string

  curl -H "X-Vault-Request: true" $VAULT_ADDR/v1/sys/seal-status
 
$ curl -H "X-Vault-Request: true"  $VAULT_ADDR/v1/sys/seal-status
{
  "type":"shamir",
  "initialized":true,
  "sealed":true,
  "t":1,
  "n":1,
  "progress":0,
  "nonce":"",
  "version":"1.14.8",
  "build_date":"2023-12-04T17:45:23Z",
  "migration":false,
  "recovery_seal":false,
  "storage_type":"file"
}
```
 
## Init

```
#vault operator init -output-curl-string -key-shares=1 -key-threshold=1
export JSON_RESULT=$(curl -s -X PUT -H "X-Vault-Request: true" -d '{"secret_shares":1,"secret_threshold":1}' https://hcv.ihc-dt.cluster-3.de/v1/sys/init)
echo $JSON_RESULT | jq .

    {"keys":["e0a37ca4246048011037cf9fc24a0de4223e5c62e870fbe3452a73cb1e8742df"],"keys_base64":["4KN8pCRgSAEQN8+fwkoN5CI+XGLocPvjRSpzyx6HQt8="],"root_token":"hvs.5DfFI83XakU7VQqEqsmdrLER"}
```

retrieve token and key

```
export ROOT_TOKEN=$(echo $JSON_RESULT | jq -r '.root_token')
export UNSEAL_KEY1=$(echo $JSON_RESULT | jq -r '.keys[0]')
echo $ROOT_TOKEN
echo $UNSEAL_KEY1
```

save secret

```
kubectl create secret -n hcv generic hcv-secrets --from-literal=rootToken=$ROOT_TOKEN --from-literal=unsealKey1=$UNSEAL_KEY1 --dry-run=client -oyaml | kubectl apply -f -
```



```
export STATUS_JSON=$(curl -s -H "X-Vault-Request: true"  $VAULT_ADDR/v1/sys/seal-status || true)
echo --- STATUS ---
echo $STATUS_JSON | jq .
if echo $STATUS_JSON | jq -e '.initialized == false' >/dev/null
then
  echo --- init ---
  export JSON_RESULT=$(curl -s -X PUT -H 'X-Vault-Request:true' -d '{"secret_shares":1,"secret_threshold":1}' $VAULT_ADDR/v1/sys/init)
  echo $JSON_RESULT
  echo $JSON_RESULT | jq .
  if echo $JSON_RESULT | jq -e '.root_token != null'
  then
    export ROOT_TOKEN=$(echo $JSON_RESULT | jq -r '.root_token')
    export UNSEAL_KEY1=$(echo $JSON_RESULT | jq -r '.keys[0]')
    kubectl create secret -n canvas-vault generic canvas-vault-hc-hcv-secrets --from-literal=rootToken=$ROOT_TOKEN --from-literal=unsealKey1=$UNSEAL_KEY1 --dry-run=client -oyaml | kubectl apply -f -
  else
    echo ERROR initializing Vault $JSON_RESULT
  fi
else
  echo Vault already initialized
fi
```
 
## unseal

```
$ vault operate unseal PVIK...rZkE=
```

```
export VAULT_ADDR=https://hcv.ihc-dt.cluster-3.de
export VAULT_TOKEN=hvs.yvXB...Kcqa
export UNSEAL_KEY1=PVIK...rZkE=
curl -X PUT -H "X-Vault-Request: true" -d "{\"key\":\"$UNSEAL_KEY1\",\"reset\":false,\"migrate\":false}" $VAULT_ADDR/v1/sys/unseal
```



```
curl -X PUT -H "X-Vault-Request: true" -H "X-Vault-Token: $VAULT_TOKEN" -d "{\"key\":\"$UNSEAL_KEY1\",\"reset\":false,\"migrate\":false}" $VAULT_ADDR/v1/sys/unseal
$ curl  -H "X-Vault-Token: hvs.yvXB...Kcqa" -H "X-Vault-Request: true"  https://hcv.ihc-dt.cluster-3.de/v1/sys/seal-status
```
 
```
FOUND=$(curl -s -H "X-Vault-Request: true"  $VAULT_ADDR/v1/sys/seal-status | grep '"sealed"')

echo "getting status for vault $VAULT_ADDR"
STATUS_JSON=$(curl -s -H "X-Vault-Request: true"  $VAULT_ADDR/v1/sys/seal-status || true)
echo $STATUS_JSON
if  echo $STATUS_JSON | grep '"sealed"'
then
  if  echo $STATUS_JSON | grep '"sealed":true'
  then
    echo Vault is sealed, unsealing
    curl -X PUT -H "X-Vault-Request: true" -d "{\"key\":\"$UNSEAL_KEY1\",\"reset\":false,\"migrate\":false}" $VAULT_ADDR/v1/sys/unseal
  else
    echo alreayd unsealed, nothing to do
  fi
else
  echo "endpoint $VAULT_ADDR/v1/sys/seal-status not accessible"
fi


echo "getting status for vault $VAULT_ADDR"
STATUS_JSON=$(curl -s -H "X-Vault-Request: true"  $VAULT_ADDR/v1/sys/seal-status || true)
echo $STATUS_JSON
if  echo $STATUS_JSON | grep '"sealed"'
then
  if  echo $STATUS_JSON | grep '"sealed":true'
  then
    echo Vault is sealed, unsealing
    curl -X PUT -H "X-Vault-Request: true" -d "{\"key\":\"$UNSEAL_KEY1\",\"reset\":false,\"migrate\":false}" $VAULT_ADDR/v1/sys/unseal
  else
    echo alreayd unsealed, nothing to do
  fi
else
  echo "endpoint $VAULT_ADDR/v1/sys/seal-status not accessible"
fi



if  curl -s -H "X-Vault-Request: true"  $VAULT_ADDR/v1/sys/seal-status | grep '"sealedx"'
then
  echo OK
else
  echo NOT OK
fi


```
 
 