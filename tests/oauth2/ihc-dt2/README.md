# Analysis

```
$ kubectl exec -c istio-proxy -n istio-ingress istio-ingress-697db6fdb6-fszf7 curl http://localhost:15000/config_dump

   ...
   "dynamic_listeners": [
    {
      "listener": {
       "@type": "type.googleapis.com/envoy.config.listener.v3.Listener",
       },
       "filter_chains": [
         "filters": [{
           "name": "envoy.filters.network.http_connection_manager",
           "typed_config": {
            "http_filters": [{
              "name": "envoy.filters.http.credential_injector",
              "typed_config": {
               "@type": "type.googleapis.com/envoy.extensions.filters.http.credential_injector.v3.CredentialInjector",
               "credential": {
                "name": "envoy.http.injected_credentials.oauth2",
                "typed_config": {
                 "@type": "type.googleapis.com/envoy.extensions.http.injected_credentials.oauth2.v3.OAuth2",
                 "token_endpoint": {
                  "uri": "http://canvas-keycloak.canvas.svc.cluster.local/auth/realms/myrealm/protocol/openid-connect/token",
                  "cluster": "outbound|8083||canvas-keycloak.canvas.svc.cluster.local",
                  "timeout": "3s"
                 },
                 "client_credentials": {
                  "client_id": "demo-a-productcatalogmanagement",
                  "client_secret": {
                   "name": "clientsecret",
                   "sds_config": {
                    "path_config_source": {
                     "path": "/config_map/oauth2secs/demo-a-productcatalogmanagement.yaml",
                     "watched_directory": {
                      "path": "/config_map/oauth2secs"
                     }
                ...
             },
       ...
    {
     "name": "clientsecret",
     "last_updated": "2024-11-25T19:58:45.423Z",
     "secret": {
      "@type": "type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.Secret",
      "name": "clientsecret",
      "generic_secret": {
       "secret": {
        "inline_bytes": "W3JlZGFjdGVkXQ=="
       }
      }
     }
    }
  ... 
```