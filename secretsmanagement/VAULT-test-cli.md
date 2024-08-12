# Testing HashiCorp Vault with cURL

## Configure Vault address

```
VAULT_ADDR=https://canvas-vault-hc.ihc-dt.cluster-3.de
```

## Login

AS token the root login token configured in the helm charts can be used.

```
vault login

  Token (will be hidden):
  
  Success! You are now authenticated. The token information displayed below
  is already stored in the token helper. You do NOT need to run "vault login"
  again. Future Vault requests will automatically use this token.
  
  Key                  Value
  ---                  -----
  token                *****
  token_accessor       2i9x8JLm3jam0tViCyy8KEgV
  token_duration       ∞
  token_renewable      false
  token_policies       ["root"]
  identity_policies    []
  policies             ["root"]  
```

Because the root token can be used in every curl command, 
the login has not to be done in curl.
But it is also possible:

```
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: egalegal" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/auth/token/lookup-self | jq '.'

	{
	  "request_id": "518e1bd8-651c-473f-04a3-ae379abbb106",
	  "lease_id": "",
	  "renewable": false,
	  "lease_duration": 0,
	  "data": {
	    "accessor": "63jLKEdQWySjvWtyXDwW7Q8T",
	    "creation_time": 1723128175,
	    "creation_ttl": 0,
	    "display_name": "token",
	    "entity_id": "",
	    "expire_time": null,
	    "explicit_max_ttl": 0,
	    "id": "egalegal",
	    "issue_time": "2024-08-08T14:42:55.578127845Z",
	    "meta": null,
	    "num_uses": 0,
	    "orphan": true,
	    "path": "auth/token/create",
	    "policies": [
	      "root"
	    ],
	    "renewable": false,
	    "ttl": 0,
	    "type": "service"
	  },
	  "wrap_info": null,
	  "warnings": null,
	  "auth": null
	}
```

## Check JWT authentication

```
$ vault auth list

  Path             Type     Accessor               Description                Version
  ----             ----     --------               -----------                -------
  jwt-k8s-sman/    jwt      auth_jwt_0bbe57d8      n/a                        n/a
  token/           token    auth_token_fa623714    token based credentials    n/a
```

```
$ vault auth list -output-curl-string

  curl -H "X-Vault-Request: true" -H "X-Vault-Token: $(vault print token)" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/sys/auth
```

instead of `$(vault print token)` an auth token can be used, as above, the root master password configured when the vault was setup can be used. 

```
$ ROOT_TOKEN=...
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/sys/auth | jq '."jwt-k8s-sman/"'

{
  "accessor": "auth_jwt_0bbe57d8",
  "config": {
    "default_lease_ttl": 0,
    "force_no_cache": false,
    "max_lease_ttl": 0,
    "token_type": "default-service"
  },
  "deprecation_status": "supported",
  "description": "",
  "external_entropy_access": false,
  "local": false,
  "options": null,
  "plugin_version": "",
  "running_plugin_version": "v0.16.0+builtin",
  "running_sha256": "",
  "seal_wrap": false,
  "type": "jwt",
  "uuid": "18488e06-bb0d-c9b7-f71c-af2b8d737408"
}
```

## List defined roles

```
$ vault list auth/jwt-k8s-sman/role

Keys
----
sman-components-alice-productcatalogmanagement-role
```

```
$ #vault list -output-curl-string auth/jwt-k8s-sman/role
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/auth/jwt-k8s-sman/role?list=true | jq -r '.data.keys[]'

  sman-components-alice-productcatalogmanagement-role
```


## Details for one role

```
$ vault read auth/jwt-k8s-sman/role/sman-components-alice-productcatalogmanagement-role

	Key                        Value
	---                        -----
	allowed_redirect_uris      [http://canvas-vault-hc.canvas-vault.svc.cluster.local:8200/jwt-test/callback]
	bound_audiences            [https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west3/clusters/ihc-dt]
	bound_claims               map[/kubernetes.io/namespace:components /kubernetes.io/pod/name:alice-* /kubernetes.io/serviceaccount/name:default]
	bound_claims_type          glob
	bound_subject              n/a
	claim_mappings             <nil>
	clock_skew_leeway          0
	expiration_leeway          0
	groups_claim               n/a
	max_age                    0
	not_before_leeway          0
	oidc_scopes                <nil>
	role_type                  jwt
	token_bound_cidrs          []
	token_explicit_max_ttl     0s
	token_max_ttl              0s
	token_no_default_policy    false
	token_num_uses             0
	token_period               0s
	token_policies             [sman-components-alice-productcatalogmanagement-policy]
	token_ttl                  1h
	token_type                 default
	user_claim                 sub
	user_claim_json_pointer    false
	verbose_oidc_logging       false
```

as curl:

```
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/auth/jwt-k8s-sman/role/sman-components-alice-productcatalogmanagement-role

	{
	  "request_id": "c6db9e42-061b-bc24-2089-3f3acfac629b",
	  "lease_id": "",
	  "renewable": false,
	  "lease_duration": 0,
	  "data": {
	    "allowed_redirect_uris": [
	      "http://canvas-vault-hc.canvas-vault.svc.cluster.local:8200/jwt-test/callback"
	    ],
	    "	": [
	      "https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west3/clusters/ihc-dt"
	    ],
	    "bound_claims": {
	      "/kubernetes.io/namespace": "components",
	      "/kubernetes.io/pod/name": "alice-*",
	      "/kubernetes.io/serviceaccount/name": "default"
	    },
	    "bound_claims_type": "glob",
	    "bound_subject": "",
	    "claim_mappings": null,
	    "clock_skew_leeway": 0,
	    "expiration_leeway": 0,
	    "groups_claim": "",
	    "max_age": 0,
	    "not_before_leeway": 0,
	    "oidc_scopes": null,
	    "role_type": "jwt",
	    "token_bound_cidrs": [],
	    "token_explicit_max_ttl": 0,
	    "token_max_ttl": 0,
	    "token_no_default_policy": false,
	    "token_num_uses": 0,
	    "token_period": 0,
	    "token_policies": [
	      "sman-components-alice-productcatalogmanagement-policy"
	    ],
	    "token_ttl": 3600,
	    "token_type": "default",
	    "user_claim": "sub",
	    "user_claim_json_pointer": false,
	    "verbose_oidc_logging": false
	  },
	  "wrap_info": null,
	  "warnings": null,
	  "auth": null
	}
```

most interesting: "token_policies" "bound_claims" and "bound_audiences":

```
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/auth/jwt-k8s-sman/role/sman-components-alice-productcatalogmanagement-role | jq '.data | {"bound_claims": .bound_claims, "token_policies": .token_policies[], "bound_audiences":.bound_audiences[]}'
{
  "bound_claims": {
    "/kubernetes.io/namespace": "components",
    "/kubernetes.io/pod/name": "alice-*",
    "/kubernetes.io/serviceaccount/name": "default"
  },
  "token_policies": "sman-components-alice-productcatalogmanagement-policy",
  "bound_audiences": "https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west3/clusters/ihc-dt"
}
```


## Policies

```
$ vault policy list

  default
  sman-components-alice-productcatalogmanagement-policy
  root
```

as curl:

```
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/sys/policies/acl?list=true | jq -r '.data.keys[]'

  default
  sman-components-alice-productcatalogmanagement-policy
  root
```

## Details for one policy

```
$ vault policy read sman-components-alice-productcatalogmanagement-policy

  path "kv-sman-components-alice-productcatalogmanagement/data/sidecar/*" {
            capabilities = ["create", "read", "update", "delete", "patch"]   # do not support "list" for security reasons
        }
```

as curl

```
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/sys/policies/acl/sman-components-alice-productcatalogmanagement-policy | jq '.data'

  {
    "name": "sman-components-alice-productcatalogmanagement-policy",
    "policy": "\n        path \"kv-sman-components-alice-productcatalogmanagement/data/sidecar/*\" {\n          capabilities = [\"create\", \"read\", \"update\", \"delete\", \"patch\"]   # do not support \"list\" for security reasons   \n        }\n        "
  }
```

```
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/sys/policies/acl/sman-components-alice-productcatalogmanagement-policy | jq -r '.data.policy'

        path "kv-sman-components-alice-productcatalogmanagement/data/sidecar/*" {
          capabilities = ["create", "read", "update", "delete", "patch"]   # do not support "list" for security reasons
        }
```

## Get Secrets

```
$ vault kv get kv-sman-components-alice-productcatalogmanagement/sidecar

	========================= Secret Path =========================
	kv-sman-components-alice-productcatalogmanagement/data/sidecar
	
	======= Metadata =======
	Key                Value
	---                -----
	created_time       2024-08-12T12:01:02.895686151Z
	custom_metadata    <nil>
	deletion_time      n/a
	destroyed          false
	version            1
	
	====== Data ======
	Key         Value
	---         -----
	password    abc123
```

as curl:

```
$ curl -s -H "X-Vault-Request: true" -H "X-Vault-Token: $ROOT_TOKEN" https://canvas-vault-hc.ihc-dt.cluster-3.de/v1/kv-sman-components-alice-productcatalogmanagement/data/sidecar | jq '.data.data'

  {
    "password": "abc123"
  }
```
