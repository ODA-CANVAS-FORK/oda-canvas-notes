# OAuth2 Tests


## links

* https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/credential_injector_filter#oauth2-credential-injector-client-credential-grant
* https://github.com/envoyproxy/envoy/issues/10979#issuecomment-655851591


## watch logfile of echoservice

```
$ kubectl logs -n echoservice deployment/echoservice-deployment -f
```


## login to pod deployed in components 

```
$ kubectl exec -n components -it demo-a-prodcatapi-57868f9d7c-67fsc -- /bin/bash
```

## use curl from inside POD

```
root@demo-a-prodcatapi-57868f9d7c-67fsc:/src# curl -XPOST -d "TEST" http://echoservice.echoservice.svc.cluster.local/echo
```

LOGS:

```
----------
Host: echoservice.echoservice.svc.cluster.local
User-Agent: curl/7.64.0
Accept: */*
Content-Length: 4
Content-Type: application/x-www-form-urlencoded
X-Forwarded-Proto: http
X-Request-Id: 1e9fc470-9ecf-4aa5-96dc-4aa4bbf647ef
X-Envoy-Decorator-Operation: echoservice.echoservice.svc.cluster.local:80/*
X-Envoy-Peer-Metadata-Id: sidecar~10.88.3.242~demo-a-prodcatapi-57868f9d7c-67fsc.components~components.svc.cluster.local
X-Envoy-Peer-Metadata: ChoKCkNMVVNURVJfSUQSDBoKS3ViZXJuZXRlcwrkAQoGTEFCRUxTEtkBKtYBCigKA2FwcBIhGh9kZW1vLWEtcHJvZHVjdGNhdGFsb2dtYW5hZ2VtZW50CkQKH3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLW5hbWUSIRofZGVtby1hLXByb2R1Y3RjYXRhbG9nbWFuYWdlbWVudAo/CiNzZXJ2aWNlLmlzdGlvLmlvL2Nhbm9uaWNhbC1yZXZpc2lvbhIYGhZwcm9kdWN0Y2F0YWxvZ2FwaS0wLjIzCiMKB3ZlcnNpb24SGBoWcHJvZHVjdGNhdGFsb2dhcGktMC4yMwosCgROQU1FEiQaImRlbW8tYS1wcm9kY2F0YXBpLTU3ODY4ZjlkN2MtNjdmc2MKGQoJTkFNRVNQQUNFEgwaCmNvbXBvbmVudHMKWAoFT1dORVISTxpNa3ViZXJuZXRlczovL2FwaXMvYXBwcy92MS9uYW1lc3BhY2VzL2NvbXBvbmVudHMvZGVwbG95bWVudHMvZGVtby1hLXByb2RjYXRhcGkKJAoNV09SS0xPQURfTkFNRRITGhFkZW1vLWEtcHJvZGNhdGFwaQ==
X-Envoy-Attempt-Count: 1
----------
None
'NoneType' object has no attribute 'startswith'
PAYLOAD: ?
10.88.3.242 - - [22/Nov/2024 09:05:49] "POST /echo HTTP/1.1" 401 -
```


# Envoy config_dump

```
kubectl exec -n echoservice echoservice-deployment-5f79c45f85-8cbsb -c istio-proxy -- curl http://localhost:15000/config_dump
```

# Envoy server_info

```
kubectl exec -it -c istio-proxy -n components demo-a-prodcatapi-57868f9d7c-67fsc -- /bin/bash
```

```
istio-proxy@demo-a-prodcatapi-57868f9d7c-67fsc:/$ pilot-agent request GET server_info
```

```
{
 "version": "739644f84930a8c0d416319aea97f58c2222f7ef/1.32.2-dev/Clean/RELEASE/BoringSSL",
 "state": "LIVE",
 "uptime_current_epoch": "53185s",
 "uptime_all_epochs": "53185s",
 "hot_restart_version": "disabled",
 "command_line_options": {
  "base_id": "0",
  "concurrency": 2,
  "config_path": "etc/istio/proxy/envoy-rev.json",
  "config_yaml": "",
  "allow_unknown_static_fields": true,
  "admin_address_path": "",
  "local_address_ip_version": "v4",
  "log_level": "warning",
  "component_log_level": "misc:error",
  "log_format": "[%Y-%m-%d %T.%e][%t][%l][%n] [%g:%#] %v",
  "log_path": "",
  "service_cluster": "",
  "service_node": "",
  "service_zone": "",
  "file_flush_interval": "1s",
  "drain_time": "45s",
  "parent_shutdown_time": "900s",
  "mode": "Serve",
  "disable_hot_restart": true,
  "enable_mutex_tracing": false,
  "restart_epoch": 0,
  "cpuset_threads": false,
  "reject_unknown_dynamic_fields": false,
  "log_format_escaped": false,
  "disabled_extensions": [],
  "ignore_unknown_dynamic_fields": false,
  "use_dynamic_base_id": false,
  "base_id_path": "",
  "drain_strategy": "Immediate",
  "enable_fine_grain_logging": false,
  "socket_path": "@envoy_domain_socket",
  "socket_mode": 0,
  "enable_core_dump": false,
  "stats_tag": [],
  "skip_hot_restart_on_no_parent": false,
  "skip_hot_restart_parent_stats": false
 },
 "node": {
  "id": "sidecar~10.88.3.242~demo-a-prodcatapi-57868f9d7c-67fsc.components~components.svc.cluster.local",
  "cluster": "demo-a-productcatalogmanagement.components",
  "metadata": {
   "POD_PORTS": "[{\"name\":\"pcapi\",\"containerPort\":8080,\"protocol\":\"TCP\"}]",
   "NAMESPACE": "components",
   "APP_CONTAINERS": "demo-a-prodcatapi",
   "NAME": "demo-a-prodcatapi-57868f9d7c-67fsc",
   "ISTIO_PROXY_SHA": "739644f84930a8c0d416319aea97f58c2222f7ef",
   "ENVOY_STATUS_PORT": 15021,
   "CLUSTER_ID": "Kubernetes",
   "PLATFORM_METADATA": {
    "gcp_gce_instance_template": "projects/273015080502/regions/europe-west3/instanceTemplates/gke-ihc-dt-pool-1-1-7659fcc6",
    "gcp_gke_cluster_url": "https://container.googleapis.com/v1/projects/tmforum-oda-component-cluster/locations/europe-west3/clusters/ihc-dt",
    "gcp_gke_cluster_name": "ihc-dt",
    "gcp_gce_instance": "gke-ihc-dt-pool-1-1-7cd1e14b-gwok",
    "gcp_location": "europe-west3",
    "gcp_project": "tmforum-oda-component-cluster",
    "gcp_project_number": "273015080502",
    "gcp_gce_instance_id": "1783838691534955534",
    "gcp_gce_instance_created_by": "projects/273015080502/zones/europe-west3-a/instanceGroupManagers/gke-ihc-dt-pool-1-1-7cd1e14b-grp"
   },
   "LABELS": {
    "oda.tmforum.org/secretsmanagement": "sidecar",
    "service.istio.io/canonical-revision": "productcatalogapi-0.23",
    "version": "productcatalogapi-0.23",
    "app": "demo-a-productcatalogmanagement",
    "service.istio.io/canonical-name": "demo-a-productcatalogmanagement",
    "security.istio.io/tlsMode": "istio",
    "impl": "demo-a-prodcatapi"
   },
   "ISTIO_VERSION": "1.24.0",
   "ENVOY_PROMETHEUS_PORT": 15090,
   "NODE_NAME": "gke-ihc-dt-pool-1-1-7cd1e14b-gwok",
   "MESH_ID": "cluster.local",
   "PILOT_SAN": [
    "istiod.istio-system.svc"
   ],
   "SERVICE_ACCOUNT": "default",
   "PROXY_CONFIG": {
    "statNameLength": 189,
    "concurrency": 2,
    "terminationDrainDuration": "5s",
    "proxyAdminPort": 15000,
    "statusPort": 15020,
    "serviceCluster": "istio-proxy",
    "binaryPath": "/usr/local/bin/envoy",
    "discoveryAddress": "istiod.istio-system.svc:15012",
    "drainDuration": "45s",
    "configPath": "./etc/istio/proxy",
    "controlPlaneAuthPolicy": "MUTUAL_TLS"
   },
   "INTERCEPTION_MODE": "REDIRECT",
   "INSTANCE_IPS": "10.88.3.242",
   "WORKLOAD_NAME": "demo-a-prodcatapi",
   "OWNER": "kubernetes://apis/apps/v1/namespaces/components/deployments/demo-a-prodcatapi",
   "ANNOTATIONS": {
    "kubernetes.io/config.source": "api",
    "istio.io/rev": "default",
    "kubernetes.io/config.seen": "2024-11-21T21:18:45.030315007Z",
    "prometheus.io/path": "/stats/prometheus",
    "kubectl.kubernetes.io/default-logs-container": "demo-a-prodcatapi",
    "kubectl.kubernetes.io/default-container": "demo-a-prodcatapi",
    "prometheus.io/scrape": "true",
    "sidecar.istio.io/status": "{\"initContainers\":[\"istio-init\"],\"containers\":[\"istio-proxy\"],\"volumes\":[\"workload-socket\",\"credential-socket\",\"workload-certs\",\"istio-envoy\",\"istio-data\",\"istio-podinfo\",\"istio-token\",\"istiod-ca-cert\"],\"imagePullSecrets\":null,\"revision\":\"default\"}",
    "prometheus.io/port": "15020"
   }
  },
  "locality": {
   "region": "europe",
   "zone": "europe-west3",
   "sub_zone": ""
  },
  "user_agent_name": "envoy",
  "user_agent_build_version": {
   "version": {
    "major_number": 1,
    "minor_number": 32,
    "patch": 2
   },
   "metadata": {
    "revision.status": "Clean",
    "revision.sha": "739644f84930a8c0d416319aea97f58c2222f7ef",
    "build.type": "RELEASE",
    "build.label": "dev",
    "ssl.version": "BoringSSL"
   }
  },
  "extensions": [
   {
    "name": "envoy.route.early_data_policy.default",
    "category": "envoy.route.early_data_policy",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.early_data.v3.DefaultEarlyDataPolicy"
    ]
   },
   {
    "name": "envoy.cluster.eds",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.cluster.logical_dns",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.cluster.original_dst",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.cluster.static",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.cluster.strict_dns",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.clusters.aggregate",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.clusters.dynamic_forward_proxy",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.clusters.redis",
    "category": "envoy.clusters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.transport_sockets.alts",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.alts.v3.Alts"
    ]
   },
   {
    "name": "envoy.transport_sockets.internal_upstream",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.internal_upstream.v3.InternalUpstreamTransport"
    ]
   },
   {
    "name": "envoy.transport_sockets.quic",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.quic.v3.QuicUpstreamTransport"
    ]
   },
   {
    "name": "envoy.transport_sockets.raw_buffer",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.raw_buffer.v3.RawBuffer"
    ]
   },
   {
    "name": "envoy.transport_sockets.starttls",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.starttls.v3.UpstreamStartTlsConfig"
    ]
   },
   {
    "name": "envoy.transport_sockets.tap",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.tap.v3.Tap"
    ]
   },
   {
    "name": "envoy.transport_sockets.tls",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.tls.v3.UpstreamTlsContext"
    ]
   },
   {
    "name": "envoy.transport_sockets.upstream_proxy_protocol",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.proxy_protocol.v3.ProxyProtocolUpstreamTransport"
    ]
   },
   {
    "name": "raw_buffer",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "starttls",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "tls",
    "category": "envoy.transport_sockets.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.rate_limit_descriptors.expr",
    "category": "envoy.rate_limit_descriptors",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.rate_limit_descriptors.expr.v3.Descriptor"
    ]
   },
   {
    "name": "envoy.echo",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ext_authz",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.filters.network.connection_limit",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.connection_limit.v3.ConnectionLimit"
    ]
   },
   {
    "name": "envoy.filters.network.direct_response",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.direct_response.v3.Config"
    ]
   },
   {
    "name": "envoy.filters.network.dubbo_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.dubbo_proxy.v3.DubboProxy"
    ]
   },
   {
    "name": "envoy.filters.network.echo",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.echo.v3.Echo"
    ]
   },
   {
    "name": "envoy.filters.network.ext_authz",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.ext_authz.v3.ExtAuthz"
    ]
   },
   {
    "name": "envoy.filters.network.golang",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.golang.v3alpha.Config"
    ]
   },
   {
    "name": "envoy.filters.network.http_connection_manager",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager"
    ]
   },
   {
    "name": "envoy.filters.network.istio_stats",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "stats.PluginConfig"
    ]
   },
   {
    "name": "envoy.filters.network.local_ratelimit",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.local_ratelimit.v3.LocalRateLimit"
    ]
   },
   {
    "name": "envoy.filters.network.metadata_exchange",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.tcp.metadataexchange.config.MetadataExchange"
    ]
   },
   {
    "name": "envoy.filters.network.mongo_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.mongo_proxy.v3.MongoProxy"
    ]
   },
   {
    "name": "envoy.filters.network.mysql_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.mysql_proxy.v3.MySQLProxy"
    ]
   },
   {
    "name": "envoy.filters.network.postgres_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.postgres_proxy.v3alpha.PostgresProxy"
    ]
   },
   {
    "name": "envoy.filters.network.ratelimit",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.ratelimit.v3.RateLimit"
    ]
   },
   {
    "name": "envoy.filters.network.rbac",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.rbac.v3.RBAC"
    ]
   },
   {
    "name": "envoy.filters.network.redis_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.redis_proxy.v3.RedisProxy"
    ]
   },
   {
    "name": "envoy.filters.network.set_filter_state",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.set_filter_state.v3.Config"
    ]
   },
   {
    "name": "envoy.filters.network.sip_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.sip_proxy.v3alpha.SipProxy"
    ]
   },
   {
    "name": "envoy.filters.network.sni_cluster",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.sni_cluster.v3.SniCluster"
    ]
   },
   {
    "name": "envoy.filters.network.sni_dynamic_forward_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.sni_dynamic_forward_proxy.v3.FilterConfig"
    ]
   },
   {
    "name": "envoy.filters.network.tcp_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.tcp_proxy.v3.TcpProxy"
    ]
   },
   {
    "name": "envoy.filters.network.thrift_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.thrift_proxy.v3.ThriftProxy"
    ]
   },
   {
    "name": "envoy.filters.network.wasm",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.wasm.v3.Wasm"
    ]
   },
   {
    "name": "envoy.filters.network.zookeeper_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.zookeeper_proxy.v3.ZooKeeperProxy"
    ]
   },
   {
    "name": "envoy.http_connection_manager",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.mongo_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ratelimit",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.redis_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tcp_proxy",
    "category": "envoy.filters.network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.regex_engines.google_re2",
    "category": "envoy.regex_engines",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.regex_engines.v3.GoogleRE2"
    ]
   },
   {
    "name": "envoy.matching.actions.format_string",
    "category": "envoy.matching.action",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.core.v3.SubstitutionFormatString"
    ]
   },
   {
    "name": "filter-chain-name",
    "category": "envoy.matching.action",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "google.protobuf.StringValue"
    ]
   },
   {
    "name": "envoy.retry_host_predicates.omit_canary_hosts",
    "category": "envoy.retry_host_predicates",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.retry.host.omit_canary_hosts.v3.OmitCanaryHostsPredicate"
    ]
   },
   {
    "name": "envoy.retry_host_predicates.omit_host_metadata",
    "category": "envoy.retry_host_predicates",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.retry.host.omit_host_metadata.v3.OmitHostMetadataConfig"
    ]
   },
   {
    "name": "envoy.retry_host_predicates.previous_hosts",
    "category": "envoy.retry_host_predicates",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.retry.host.previous_hosts.v3.PreviousHostsPredicate"
    ]
   },
   {
    "name": "envoy.formatter.cel",
    "category": "envoy.formatter",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.formatter.cel.v3.Cel"
    ]
   },
   {
    "name": "envoy.formatter.metadata",
    "category": "envoy.formatter",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.formatter.metadata.v3.Metadata"
    ]
   },
   {
    "name": "envoy.formatter.req_without_query",
    "category": "envoy.formatter",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.formatter.req_without_query.v3.ReqWithoutQuery"
    ]
   },
   {
    "name": "envoy.matching.custom_matchers.trie_matcher",
    "category": "envoy.matching.network.custom_matchers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "xds.type.matcher.v3.IPMatcher"
    ]
   },
   {
    "name": "envoy.route_config_update_requester.default",
    "category": "envoy.route_config_update_requester",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.router.cluster_specifier_plugin.lua",
    "category": "envoy.router.cluster_specifier_plugin",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.router.cluster_specifiers.lua.v3.LuaConfig"
    ]
   },
   {
    "name": "envoy.path.match.uri_template.uri_template_matcher",
    "category": "envoy.path.match",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.path.match.uri_template.v3.UriTemplateMatchConfig"
    ]
   },
   {
    "name": "envoy.string_matcher.lua",
    "category": "envoy.string_matcher",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.string_matcher.lua.v3.Lua"
    ]
   },
   {
    "name": "envoy.request_id.uuid",
    "category": "envoy.request_id",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.request_id.uuid.v3.UuidRequestIdConfig"
    ]
   },
   {
    "name": "envoy.dog_statsd",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.graphite_statsd",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.metrics_service",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.open_telemetry_stat_sink",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.stat_sinks.dog_statsd",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.metrics.v3.DogStatsdSink"
    ]
   },
   {
    "name": "envoy.stat_sinks.graphite_statsd",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.stat_sinks.graphite_statsd.v3.GraphiteStatsdSink"
    ]
   },
   {
    "name": "envoy.stat_sinks.hystrix",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.metrics.v3.HystrixSink"
    ]
   },
   {
    "name": "envoy.stat_sinks.metrics_service",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.metrics.v3.MetricsServiceConfig"
    ]
   },
   {
    "name": "envoy.stat_sinks.open_telemetry",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.stat_sinks.open_telemetry.v3.SinkConfig"
    ]
   },
   {
    "name": "envoy.stat_sinks.statsd",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.metrics.v3.StatsdSink"
    ]
   },
   {
    "name": "envoy.stat_sinks.wasm",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.stat_sinks.wasm.v3.Wasm"
    ]
   },
   {
    "name": "envoy.statsd",
    "category": "envoy.stats_sinks",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.listener_manager_impl.default",
    "category": "envoy.listener_manager_impl",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.listener.v3.ListenerManager"
    ]
   },
   {
    "name": "envoy.listener_manager_impl.validation",
    "category": "envoy.listener_manager_impl",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.listener.v3.ValidationListenerManager"
    ]
   },
   {
    "name": "envoy.rds_factory.default",
    "category": "envoy.rds_factory",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.transport_sockets.alts",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.alts.v3.Alts"
    ]
   },
   {
    "name": "envoy.transport_sockets.quic",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.quic.v3.QuicDownstreamTransport"
    ]
   },
   {
    "name": "envoy.transport_sockets.raw_buffer",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.raw_buffer.v3.RawBuffer"
    ]
   },
   {
    "name": "envoy.transport_sockets.starttls",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.starttls.v3.StartTlsConfig"
    ]
   },
   {
    "name": "envoy.transport_sockets.tap",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.tap.v3.Tap"
    ]
   },
   {
    "name": "envoy.transport_sockets.tls",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.transport_sockets.tls.v3.DownstreamTlsContext"
    ]
   },
   {
    "name": "raw_buffer",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "starttls",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "tls",
    "category": "envoy.transport_sockets.downstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.network.dns_resolver.cares",
    "category": "envoy.network.dns_resolver",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.network.dns_resolver.cares.v3.CaresDnsResolverConfig"
    ]
   },
   {
    "name": "auto",
    "category": "envoy.thrift_proxy.protocols",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "binary",
    "category": "envoy.thrift_proxy.protocols",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "binary/non-strict",
    "category": "envoy.thrift_proxy.protocols",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "compact",
    "category": "envoy.thrift_proxy.protocols",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "twitter",
    "category": "envoy.thrift_proxy.protocols",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "default",
    "category": "network.connection.client",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy_internal",
    "category": "network.connection.client",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.access_loggers.file",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.file.v3.FileAccessLog"
    ]
   },
   {
    "name": "envoy.access_loggers.fluentd",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.fluentd.v3.FluentdAccessLogConfig"
    ]
   },
   {
    "name": "envoy.access_loggers.http_grpc",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.grpc.v3.HttpGrpcAccessLogConfig"
    ]
   },
   {
    "name": "envoy.access_loggers.open_telemetry",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.open_telemetry.v3.OpenTelemetryAccessLogConfig"
    ]
   },
   {
    "name": "envoy.access_loggers.stderr",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.stream.v3.StderrAccessLog"
    ]
   },
   {
    "name": "envoy.access_loggers.stdout",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.stream.v3.StdoutAccessLog"
    ]
   },
   {
    "name": "envoy.access_loggers.tcp_grpc",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.grpc.v3.TcpGrpcAccessLogConfig"
    ]
   },
   {
    "name": "envoy.access_loggers.wasm",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.wasm.v3.WasmAccessLog"
    ]
   },
   {
    "name": "envoy.file_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.fluentd_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.http_grpc_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.open_telemetry_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.stderr_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.stdout_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tcp_grpc_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.wasm_access_log",
    "category": "envoy.access_loggers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.resource_monitors.fixed_heap",
    "category": "envoy.resource_monitors",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.resource_monitors.fixed_heap.v3.FixedHeapConfig"
    ]
   },
   {
    "name": "envoy.resource_monitors.injected_resource",
    "category": "envoy.resource_monitors",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.resource_monitors.injected_resource.v3.InjectedResourceConfig"
    ]
   },
   {
    "name": "envoy.quic.proof_source.filter_chain",
    "category": "envoy.quic.proof_source",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.quic.proof_source.v3.ProofSourceConfig"
    ]
   },
   {
    "name": "envoy.upstream.local_address_selector.default_local_address_selector",
    "category": "envoy.upstream.local_address_selector",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.upstream.local_address_selector.v3.DefaultLocalAddressSelector"
    ]
   },
   {
    "name": "envoy.internal_redirect_predicates.allow_listed_routes",
    "category": "envoy.internal_redirect_predicates",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.internal_redirect.allow_listed_routes.v3.AllowListedRoutesConfig"
    ]
   },
   {
    "name": "envoy.internal_redirect_predicates.previous_routes",
    "category": "envoy.internal_redirect_predicates",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.internal_redirect.previous_routes.v3.PreviousRoutesConfig"
    ]
   },
   {
    "name": "envoy.internal_redirect_predicates.safe_cross_scheme",
    "category": "envoy.internal_redirect_predicates",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.internal_redirect.safe_cross_scheme.v3.SafeCrossSchemeConfig"
    ]
   },
   {
    "name": "envoy.path.rewrite.uri_template.uri_template_rewriter",
    "category": "envoy.path.rewrite",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.path.rewrite.uri_template.v3.UriTemplateRewriteConfig"
    ]
   },
   {
    "name": "envoy.tracers.opentelemetry.resource_detectors.dynatrace",
    "category": "envoy.tracers.opentelemetry.resource_detectors",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.tracers.opentelemetry.resource_detectors.v3.DynatraceResourceDetectorConfig"
    ]
   },
   {
    "name": "envoy.tracers.opentelemetry.resource_detectors.environment",
    "category": "envoy.tracers.opentelemetry.resource_detectors",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.tracers.opentelemetry.resource_detectors.v3.EnvironmentResourceDetectorConfig"
    ]
   },
   {
    "name": "envoy.quic.crypto_stream.server.quiche",
    "category": "envoy.quic.server.crypto_stream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.quic.crypto_stream.v3.CryptoServerStreamConfig"
    ]
   },
   {
    "name": "envoy.bandwidth_limit",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.buffer",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.cors",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.csrf",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ext_authz",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ext_proc",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.fault",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.filters.http.adaptive_concurrency",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.adaptive_concurrency.v3.AdaptiveConcurrency"
    ]
   },
   {
    "name": "envoy.filters.http.admission_control",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.admission_control.v3.AdmissionControl"
    ]
   },
   {
    "name": "envoy.filters.http.alternate_protocols_cache",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.alternate_protocols_cache.v3.FilterConfig"
    ]
   },
   {
    "name": "envoy.filters.http.aws_lambda",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.aws_lambda.v3.Config",
     "envoy.extensions.filters.http.aws_lambda.v3.PerRouteConfig"
    ]
   },
   {
    "name": "envoy.filters.http.aws_request_signing",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.aws_request_signing.v3.AwsRequestSigning",
     "envoy.extensions.filters.http.aws_request_signing.v3.AwsRequestSigningPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.bandwidth_limit",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.bandwidth_limit.v3.BandwidthLimit"
    ]
   },
   {
    "name": "envoy.filters.http.basic_auth",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.basic_auth.v3.BasicAuth",
     "envoy.extensions.filters.http.basic_auth.v3.BasicAuthPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.buffer",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.buffer.v3.Buffer",
     "envoy.extensions.filters.http.buffer.v3.BufferPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.cache",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.cache.v3.CacheConfig"
    ]
   },
   {
    "name": "envoy.filters.http.cdn_loop",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.cdn_loop.v3.CdnLoopConfig"
    ]
   },
   {
    "name": "envoy.filters.http.composite",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.composite.v3.Composite"
    ]
   },
   {
    "name": "envoy.filters.http.compressor",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.compressor.v3.Compressor",
     "envoy.extensions.filters.http.compressor.v3.CompressorPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.connect_grpc_bridge",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.connect_grpc_bridge.v3.FilterConfig"
    ]
   },
   {
    "name": "envoy.filters.http.cors",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.cors.v3.Cors",
     "envoy.extensions.filters.http.cors.v3.CorsPolicy"
    ]
   },
   {
    "name": "envoy.filters.http.credential_injector",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.credential_injector.v3.CredentialInjector"
    ]
   },
   {
    "name": "envoy.filters.http.csrf",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.csrf.v3.CsrfPolicy"
    ]
   },
   {
    "name": "envoy.filters.http.decompressor",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.decompressor.v3.Decompressor"
    ]
   },
   {
    "name": "envoy.filters.http.dynamic_forward_proxy",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.dynamic_forward_proxy.v3.FilterConfig",
     "envoy.extensions.filters.http.dynamic_forward_proxy.v3.PerRouteConfig"
    ]
   },
   {
    "name": "envoy.filters.http.ext_authz",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.ext_authz.v3.ExtAuthz",
     "envoy.extensions.filters.http.ext_authz.v3.ExtAuthzPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.ext_proc",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.ext_proc.v3.ExtProcPerRoute",
     "envoy.extensions.filters.http.ext_proc.v3.ExternalProcessor"
    ]
   },
   {
    "name": "envoy.filters.http.fault",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.fault.v3.HTTPFault"
    ]
   },
   {
    "name": "envoy.filters.http.gcp_authn",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.gcp_authn.v3.GcpAuthnFilterConfig"
    ]
   },
   {
    "name": "envoy.filters.http.golang",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.golang.v3alpha.Config",
     "envoy.extensions.filters.http.golang.v3alpha.ConfigsPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.grpc_field_extraction",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.grpc_field_extraction.v3.GrpcFieldExtractionConfig"
    ]
   },
   {
    "name": "envoy.filters.http.grpc_http1_bridge",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.grpc_http1_bridge.v3.Config"
    ]
   },
   {
    "name": "envoy.filters.http.grpc_http1_reverse_bridge",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.grpc_http1_reverse_bridge.v3.FilterConfig",
     "envoy.extensions.filters.http.grpc_http1_reverse_bridge.v3.FilterConfigPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.grpc_json_transcoder",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.grpc_json_transcoder.v3.GrpcJsonTranscoder"
    ]
   },
   {
    "name": "envoy.filters.http.grpc_stats",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.grpc_stats.v3.FilterConfig"
    ]
   },
   {
    "name": "envoy.filters.http.grpc_web",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.grpc_web.v3.GrpcWeb"
    ]
   },
   {
    "name": "envoy.filters.http.header_mutation",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.header_mutation.v3.HeaderMutation",
     "envoy.extensions.filters.http.header_mutation.v3.HeaderMutationPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.header_to_metadata",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.header_to_metadata.v3.Config"
    ]
   },
   {
    "name": "envoy.filters.http.health_check",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.health_check.v3.HealthCheck"
    ]
   },
   {
    "name": "envoy.filters.http.ip_tagging",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.ip_tagging.v3.IPTagging"
    ]
   },
   {
    "name": "envoy.filters.http.istio_stats",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "stats.PluginConfig"
    ]
   },
   {
    "name": "envoy.filters.http.json_to_metadata",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.json_to_metadata.v3.JsonToMetadata"
    ]
   },
   {
    "name": "envoy.filters.http.jwt_authn",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.jwt_authn.v3.JwtAuthentication",
     "envoy.extensions.filters.http.jwt_authn.v3.PerRouteConfig"
    ]
   },
   {
    "name": "envoy.filters.http.local_ratelimit",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.local_ratelimit.v3.LocalRateLimit"
    ]
   },
   {
    "name": "envoy.filters.http.lua",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.lua.v3.Lua",
     "envoy.extensions.filters.http.lua.v3.LuaPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.match_delegate",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.common.matching.v3.ExtensionWithMatcher",
     "envoy.extensions.common.matching.v3.ExtensionWithMatcherPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.oauth2",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.oauth2.v3.OAuth2"
    ]
   },
   {
    "name": "envoy.filters.http.on_demand",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.on_demand.v3.OnDemand",
     "envoy.extensions.filters.http.on_demand.v3.PerRouteConfig"
    ]
   },
   {
    "name": "envoy.filters.http.original_src",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.original_src.v3.OriginalSrc"
    ]
   },
   {
    "name": "envoy.filters.http.peer_metadata",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "io.istio.http.peer_metadata.Config"
    ]
   },
   {
    "name": "envoy.filters.http.ratelimit",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.ratelimit.v3.RateLimit",
     "envoy.extensions.filters.http.ratelimit.v3.RateLimitPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.rbac",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.rbac.v3.RBAC",
     "envoy.extensions.filters.http.rbac.v3.RBACPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.router",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.router.v3.Router"
    ]
   },
   {
    "name": "envoy.filters.http.set_filter_state",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.set_filter_state.v3.Config"
    ]
   },
   {
    "name": "envoy.filters.http.set_metadata",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.set_metadata.v3.Config"
    ]
   },
   {
    "name": "envoy.filters.http.stateful_session",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.stateful_session.v3.StatefulSession",
     "envoy.extensions.filters.http.stateful_session.v3.StatefulSessionPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.tap",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.tap.v3.Tap"
    ]
   },
   {
    "name": "envoy.filters.http.wasm",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.wasm.v3.Wasm"
    ]
   },
   {
    "name": "envoy.grpc_http1_bridge",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.grpc_json_transcoder",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.grpc_web",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.health_check",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ip_tagging",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.local_rate_limit",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.lua",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.rate_limit",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.router",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "istio.alpn",
    "category": "envoy.filters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "istio.envoy.config.filter.http.alpn.v2alpha1.FilterConfig"
    ]
   },
   {
    "name": "envoy.matching.inputs.application_protocol",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.ApplicationProtocolInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.destination_ip",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.DestinationIPInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.destination_port",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.DestinationPortInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.direct_source_ip",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.DirectSourceIPInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.dns_san",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.ssl.v3.DnsSanInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.filter_state",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.FilterStateInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.server_name",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.ServerNameInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.source_ip",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.SourceIPInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.source_port",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.SourcePortInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.source_type",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.SourceTypeInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.subject",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.ssl.v3.SubjectInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.transport_protocol",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.TransportProtocolInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.uri_san",
    "category": "envoy.matching.network.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.ssl.v3.UriSanInput"
    ]
   },
   {
    "name": "envoy.watchdog.abort_action",
    "category": "envoy.guarddog_actions",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.watchdog.v3.AbortActionConfig"
    ]
   },
   {
    "name": "envoy.watchdog.profile_action",
    "category": "envoy.guarddog_actions",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.watchdog.profile_action.v3.ProfileActionConfig"
    ]
   },
   {
    "name": "envoy.ssl.server_context_factory.default",
    "category": "envoy.ssl.server_context_factory",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.bootstrap.internal_listener",
    "category": "envoy.bootstrap",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.bootstrap.internal_listener.v3.InternalListener"
    ]
   },
   {
    "name": "envoy.bootstrap.wasm",
    "category": "envoy.bootstrap",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.wasm.v3.WasmService"
    ]
   },
   {
    "name": "envoy.bootstrap.workload_discovery",
    "category": "envoy.bootstrap",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "istio.workload.BootstrapExtension"
    ]
   },
   {
    "name": "envoy.extensions.network.socket_interface.default_socket_interface",
    "category": "envoy.bootstrap",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.network.socket_interface.v3.DefaultSocketInterface"
    ]
   },
   {
    "name": "envoy.filters.network.upstream.metadata_exchange",
    "category": "envoy.filters.upstream_network",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.tcp.metadataexchange.config.MetadataExchange"
    ]
   },
   {
    "name": "envoy.http.stateful_session.cookie",
    "category": "envoy.http.stateful_session",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.stateful_session.cookie.v3.CookieBasedSessionState"
    ]
   },
   {
    "name": "envoy.http.stateful_session.header",
    "category": "envoy.http.stateful_session",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.stateful_session.header.v3.HeaderBasedSessionState"
    ]
   },
   {
    "name": "envoy.connection_handler.default",
    "category": "envoy.connection_handler",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.http.original_ip_detection.custom_header",
    "category": "envoy.http.original_ip_detection",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.original_ip_detection.custom_header.v3.CustomHeaderConfig"
    ]
   },
   {
    "name": "envoy.http.original_ip_detection.xff",
    "category": "envoy.http.original_ip_detection",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.original_ip_detection.xff.v3.XffConfig"
    ]
   },
   {
    "name": "cryptomb",
    "category": "envoy.tls.key_providers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "qat",
    "category": "envoy.tls.key_providers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.http.header_validators.envoy_default",
    "category": "envoy.http.header_validators",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.header_validators.envoy_default.v3.HeaderValidatorConfig"
    ]
   },
   {
    "name": "envoy.key_value.file_based",
    "category": "envoy.common.key_value",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.key_value.file_based.v3.FileBasedKeyValueStoreConfig"
    ]
   },
   {
    "name": "envoy.filters.connection_pools.tcp.generic",
    "category": "envoy.upstreams",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.upstreams.tcp.generic.v3.GenericConnectionPoolProto"
    ]
   },
   {
    "name": "envoy.extensions.upstreams.http.v3.HttpProtocolOptions",
    "category": "envoy.upstream_options",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.upstreams.http.v3.HttpProtocolOptions"
    ]
   },
   {
    "name": "envoy.extensions.upstreams.tcp.v3.TcpProtocolOptions",
    "category": "envoy.upstream_options",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.upstreams.tcp.v3.TcpProtocolOptions"
    ]
   },
   {
    "name": "envoy.upstreams.http.http_protocol_options",
    "category": "envoy.upstream_options",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.upstreams.tcp.tcp_protocol_options",
    "category": "envoy.upstream_options",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tracers.datadog",
    "category": "envoy.tracers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.trace.v3.DatadogConfig"
    ]
   },
   {
    "name": "envoy.tracers.opentelemetry",
    "category": "envoy.tracers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.trace.v3.OpenTelemetryConfig"
    ]
   },
   {
    "name": "envoy.tracers.skywalking",
    "category": "envoy.tracers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.trace.v3.SkyWalkingConfig"
    ]
   },
   {
    "name": "envoy.tracers.xray",
    "category": "envoy.tracers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.trace.v3.XRayConfig"
    ]
   },
   {
    "name": "envoy.tracers.zipkin",
    "category": "envoy.tracers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.trace.v3.ZipkinConfig"
    ]
   },
   {
    "name": "envoy.zipkin",
    "category": "envoy.tracers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.compression.brotli.decompressor",
    "category": "envoy.compression.decompressor",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.compression.brotli.decompressor.v3.Brotli"
    ]
   },
   {
    "name": "envoy.compression.gzip.decompressor",
    "category": "envoy.compression.decompressor",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.compression.gzip.decompressor.v3.Gzip"
    ]
   },
   {
    "name": "envoy.compression.zstd.decompressor",
    "category": "envoy.compression.decompressor",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.compression.zstd.decompressor.v3.Zstd"
    ]
   },
   {
    "name": "envoy.filters.udp.dns_filter",
    "category": "envoy.filters.udp_listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.udp.dns_filter.v3.DnsFilterConfig"
    ]
   },
   {
    "name": "envoy.filters.udp_listener.udp_proxy",
    "category": "envoy.filters.udp_listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.udp.udp_proxy.v3.UdpProxyConfig"
    ]
   },
   {
    "name": "envoy.config_mux.delta_grpc_mux_factory",
    "category": "envoy.config_mux",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_mux.grpc_mux_factory",
    "category": "envoy.config_mux",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_mux.new_grpc_mux_factory",
    "category": "envoy.config_mux",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_mux.sotw_grpc_mux_factory",
    "category": "envoy.config_mux",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.health_checkers.grpc",
    "category": "envoy.health_checkers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.core.v3.HealthCheck.GrpcHealthCheck"
    ]
   },
   {
    "name": "envoy.health_checkers.http",
    "category": "envoy.health_checkers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.core.v3.HealthCheck.HttpHealthCheck"
    ]
   },
   {
    "name": "envoy.health_checkers.redis",
    "category": "envoy.health_checkers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.health_checkers.redis.v3.Redis"
    ]
   },
   {
    "name": "envoy.health_checkers.tcp",
    "category": "envoy.health_checkers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.config.core.v3.HealthCheck.TcpHealthCheck"
    ]
   },
   {
    "name": "envoy.filters.listener.http_inspector",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.listener.http_inspector.v3.HttpInspector"
    ]
   },
   {
    "name": "envoy.filters.listener.original_dst",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.listener.original_dst.v3.OriginalDst"
    ]
   },
   {
    "name": "envoy.filters.listener.original_src",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.listener.original_src.v3.OriginalSrc"
    ]
   },
   {
    "name": "envoy.filters.listener.proxy_protocol",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.listener.proxy_protocol.v3.ProxyProtocol"
    ]
   },
   {
    "name": "envoy.filters.listener.tls_inspector",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.listener.tls_inspector.v3.TlsInspector"
    ]
   },
   {
    "name": "envoy.listener.http_inspector",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.listener.original_dst",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.listener.original_src",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.listener.proxy_protocol",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.listener.tls_inspector",
    "category": "envoy.filters.listener",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.matching.matchers.consistent_hashing",
    "category": "envoy.matching.input_matchers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.input_matchers.consistent_hashing.v3.ConsistentHashing"
    ]
   },
   {
    "name": "envoy.matching.matchers.ip",
    "category": "envoy.matching.input_matchers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.input_matchers.ip.v3.Ip"
    ]
   },
   {
    "name": "envoy.buffer",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ext_proc",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.filters.http.admission_control",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.admission_control.v3.AdmissionControl"
    ]
   },
   {
    "name": "envoy.filters.http.aws_lambda",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.aws_lambda.v3.Config",
     "envoy.extensions.filters.http.aws_lambda.v3.PerRouteConfig"
    ]
   },
   {
    "name": "envoy.filters.http.aws_request_signing",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.aws_request_signing.v3.AwsRequestSigning",
     "envoy.extensions.filters.http.aws_request_signing.v3.AwsRequestSigningPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.buffer",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.buffer.v3.Buffer",
     "envoy.extensions.filters.http.buffer.v3.BufferPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.composite",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.composite.v3.Composite"
    ]
   },
   {
    "name": "envoy.filters.http.ext_proc",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.ext_proc.v3.ExtProcPerRoute",
     "envoy.extensions.filters.http.ext_proc.v3.ExternalProcessor"
    ]
   },
   {
    "name": "envoy.filters.http.header_mutation",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.header_mutation.v3.HeaderMutation",
     "envoy.extensions.filters.http.header_mutation.v3.HeaderMutationPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.match_delegate",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.common.matching.v3.ExtensionWithMatcher",
     "envoy.extensions.common.matching.v3.ExtensionWithMatcherPerRoute"
    ]
   },
   {
    "name": "envoy.filters.http.upstream_codec",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.upstream_codec.v3.UpstreamCodec"
    ]
   },
   {
    "name": "envoy.filters.http.wasm",
    "category": "envoy.filters.http.upstream",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.http.wasm.v3.Wasm"
    ]
   },
   {
    "name": "envoy.rbac.matchers.upstream_ip_port",
    "category": "envoy.rbac.matchers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.rbac.matchers.upstream_ip_port.v3.UpstreamIpPortMatcher"
    ]
   },
   {
    "name": "envoy.config_subscription.ads",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.ads_collection",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.aggregated_grpc_collection",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.delta_grpc",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.delta_grpc_collection",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.filesystem",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.filesystem_collection",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.grpc",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.config_subscription.rest",
    "category": "envoy.config_subscription",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ip",
    "category": "envoy.resolvers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.built_in_formatters.stream_info.default",
    "category": "envoy.built_in_formatters.stream_info",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.grpc_credentials.aws_iam",
    "category": "envoy.grpc_credentials",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.grpc_credentials.default",
    "category": "envoy.grpc_credentials",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.grpc_credentials.file_based_metadata",
    "category": "envoy.grpc_credentials",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "auto",
    "category": "envoy.thrift_proxy.transports",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "framed",
    "category": "envoy.thrift_proxy.transports",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "header",
    "category": "envoy.thrift_proxy.transports",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "unframed",
    "category": "envoy.thrift_proxy.transports",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.filters.thrift.header_to_metadata",
    "category": "envoy.thrift_proxy.filters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.thrift_proxy.filters.header_to_metadata.v3.HeaderToMetadata"
    ]
   },
   {
    "name": "envoy.filters.thrift.rate_limit",
    "category": "envoy.thrift_proxy.filters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.thrift_proxy.filters.ratelimit.v3.RateLimit"
    ]
   },
   {
    "name": "envoy.filters.thrift.router",
    "category": "envoy.thrift_proxy.filters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.thrift_proxy.router.v3.Router"
    ]
   },
   {
    "name": "envoy.filters.listener.original_dst.local_ip",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.filters.listener.original_dst.remote_ip",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.network.application_protocols",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.network.transport_socket.original_dst_address",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.network.upstream_server_name",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.network.upstream_subject_alt_names",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.ratelimit.hits_addend",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.string",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tcp_proxy.cluster",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tcp_proxy.disable_tunneling",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tcp_proxy.per_connection_idle_timeout_ms",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.upstream.dynamic_host",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.upstream.dynamic_port",
    "category": "filter_state.object",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.filters.dubbo.router",
    "category": "envoy.dubbo_proxy.filters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.dubbo_proxy.router.v3.Router"
    ]
   },
   {
    "name": "envoy.retry_priorities.previous_priorities",
    "category": "envoy.retry_priorities",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.retry.priority.previous_priorities.v3.PreviousPrioritiesConfig"
    ]
   },
   {
    "name": "envoy.http.injected_credentials.generic",
    "category": "envoy.http.injected_credentials",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.injected_credentials.generic.v3.Generic"
    ]
   },
   {
    "name": "envoy.http.injected_credentials.oauth2",
    "category": "envoy.http.injected_credentials",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.injected_credentials.oauth2.v3.OAuth2"
    ]
   },
   {
    "name": "envoy.tracers.opentelemetry.samplers.always_on",
    "category": "envoy.tracers.opentelemetry.samplers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.tracers.opentelemetry.samplers.v3.AlwaysOnSamplerConfig"
    ]
   },
   {
    "name": "envoy.tracers.opentelemetry.samplers.dynatrace",
    "category": "envoy.tracers.opentelemetry.samplers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.tracers.opentelemetry.samplers.v3.DynatraceSamplerConfig"
    ]
   },
   {
    "name": "envoy.extensions.http.cache.file_system_http_cache",
    "category": "envoy.http.cache",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.cache.file_system_http_cache.v3.FileSystemHttpCacheConfig"
    ]
   },
   {
    "name": "envoy.extensions.http.cache.simple",
    "category": "envoy.http.cache",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.cache.simple_http_cache.v3.SimpleHttpCacheConfig"
    ]
   },
   {
    "name": "envoy.srds_factory.default",
    "category": "envoy.srds_factory",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.matching.common_inputs.environment_variable",
    "category": "envoy.matching.common_inputs",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.environment_variable.v3.Config"
    ]
   },
   {
    "name": "envoy.load_balancing_policies.cluster_provided",
    "category": "envoy.load_balancing_policies",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.load_balancing_policies.cluster_provided.v3.ClusterProvided"
    ]
   },
   {
    "name": "envoy.load_balancing_policies.least_request",
    "category": "envoy.load_balancing_policies",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.load_balancing_policies.least_request.v3.LeastRequest"
    ]
   },
   {
    "name": "envoy.load_balancing_policies.maglev",
    "category": "envoy.load_balancing_policies",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.load_balancing_policies.maglev.v3.Maglev"
    ]
   },
   {
    "name": "envoy.load_balancing_policies.random",
    "category": "envoy.load_balancing_policies",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.load_balancing_policies.random.v3.Random"
    ]
   },
   {
    "name": "envoy.load_balancing_policies.ring_hash",
    "category": "envoy.load_balancing_policies",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.load_balancing_policies.ring_hash.v3.RingHash"
    ]
   },
   {
    "name": "envoy.load_balancing_policies.round_robin",
    "category": "envoy.load_balancing_policies",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.load_balancing_policies.round_robin.v3.RoundRobin"
    ]
   },
   {
    "name": "envoy.load_balancing_policies.subset",
    "category": "envoy.load_balancing_policies",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.load_balancing_policies.subset.v3.Subset"
    ]
   },
   {
    "name": "envoy.network.connection_balance.dlb",
    "category": "envoy.network.connection_balance",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.network.connection_balance.dlb.v3alpha.Dlb"
    ]
   },
   {
    "name": "envoy.quic.deterministic_connection_id_generator",
    "category": "envoy.quic.connection_id_generator",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.quic.connection_id_generator.v3.DeterministicConnectionIdGeneratorConfig"
    ]
   },
   {
    "name": "quic.http_server_connection.default",
    "category": "quic.http_server_connection",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.http.early_header_mutation.header_mutation",
    "category": "envoy.http.early_header_mutation",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.early_header_mutation.header_mutation.v3.HeaderMutation"
    ]
   },
   {
    "name": "dubbo.hessian2",
    "category": "envoy.dubbo_proxy.serializers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.matching.inputs.destination_ip",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.DestinationIPInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.destination_port",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.DestinationPortInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.direct_source_ip",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.DirectSourceIPInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.dns_san",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.ssl.v3.DnsSanInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.filter_state",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.FilterStateInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.request_headers",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.type.matcher.v3.HttpRequestHeaderMatchInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.request_trailers",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.type.matcher.v3.HttpRequestTrailerMatchInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.response_headers",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.type.matcher.v3.HttpResponseHeaderMatchInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.response_trailers",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.type.matcher.v3.HttpResponseTrailerMatchInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.server_name",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.ServerNameInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.source_ip",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.SourceIPInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.source_port",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.SourcePortInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.source_type",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.network.v3.SourceTypeInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.subject",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.ssl.v3.SubjectInput"
    ]
   },
   {
    "name": "envoy.matching.inputs.uri_san",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.matching.common_inputs.ssl.v3.UriSanInput"
    ]
   },
   {
    "name": "query_params",
    "category": "envoy.matching.http.input",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.type.matcher.v3.HttpRequestQueryParamMatchInput"
    ]
   },
   {
    "name": "envoy.access_loggers.extension_filters.cel",
    "category": "envoy.access_loggers.extension_filters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.access_loggers.filters.cel.v3.ExpressionFilter"
    ]
   },
   {
    "name": "envoy.matching.custom_matchers.trie_matcher",
    "category": "envoy.matching.http.custom_matchers",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "xds.type.matcher.v3.IPMatcher"
    ]
   },
   {
    "name": "envoy.udp_packet_writer.default",
    "category": "envoy.udp_packet_writer",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.udp_packet_writer.v3.UdpDefaultWriterFactory"
    ]
   },
   {
    "name": "envoy.udp_packet_writer.gso",
    "category": "envoy.udp_packet_writer",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.udp_packet_writer.v3.UdpGsoBatchWriterFactory"
    ]
   },
   {
    "name": "envoy.built_in_formatters.http.default",
    "category": "envoy.built_in_formatters.http",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.compression.brotli.compressor",
    "category": "envoy.compression.compressor",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.compression.brotli.compressor.v3.Brotli"
    ]
   },
   {
    "name": "envoy.compression.gzip.compressor",
    "category": "envoy.compression.compressor",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.compression.gzip.compressor.v3.Gzip"
    ]
   },
   {
    "name": "envoy.compression.zstd.compressor",
    "category": "envoy.compression.compressor",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.compression.zstd.compressor.v3.Zstd"
    ]
   },
   {
    "name": "envoy.filters.sip.router",
    "category": "envoy.sip_proxy.filters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.filters.network.sip_proxy.router.v3alpha.Router"
    ]
   },
   {
    "name": "envoy.http.stateful_header_formatters.preserve_case",
    "category": "envoy.http.stateful_header_formatters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": [
     "envoy.extensions.http.header_formatters.preserve_case.v3.PreserveCaseFormatterConfig"
    ]
   },
   {
    "name": "preserve_case",
    "category": "envoy.http.stateful_header_formatters",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.wasm.runtime.null",
    "category": "envoy.wasm.runtime",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.wasm.runtime.v8",
    "category": "envoy.wasm.runtime",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "dubbo",
    "category": "envoy.dubbo_proxy.protocols",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tls.cert_validator.default",
    "category": "envoy.tls.cert_validator",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   },
   {
    "name": "envoy.tls.cert_validator.spiffe",
    "category": "envoy.tls.cert_validator",
    "type_descriptor": "",
    "disabled": false,
    "type_urls": []
   }
  ],
  "client_features": [],
  "listening_addresses": [],
  "dynamic_parameters": {}
 }
}
```








# show config for pod

```
$ istioctl proxy-config all demo-a-prodcatapi-57868f9d7c-67fsc

Istio Version:       1.24.0
Istio Proxy Version: 739644f84930a8c0d416319aea97f58c2222f7ef
Envoy Version:       1.32.2-dev/Clean/RELEASE/BoringSSL

NAME                                                                                                    SERVICE FQDN                                                                    PORT      SUBSET     DIRECTION     TYPE             DESTINATION RULE
cluster/inbound|8080||                                                                                                                                                                  8080      -          inbound       ORIGINAL_DST

cluster/BlackHoleCluster                                                                                cluster/BlackHoleCluster                                                        -         -          -             STATIC

cluster/InboundPassthroughCluster                                                                       cluster/InboundPassthroughCluster                                               -         -          -             ORIGINAL_DST

cluster/PassthroughCluster                                                                              cluster/PassthroughCluster                                                      -         -          -             ORIGINAL_DST

cluster/agent                                                                                           cluster/agent                                                                   -         -          -             STATIC

cluster/outbound|9093||alertmanager-operated.grafana.svc.cluster.local                                  alertmanager-operated.grafana.svc.cluster.local                                 9093      -          outbound      ORIGINAL_DST

cluster/outbound|9094||alertmanager-operated.grafana.svc.cluster.local                                  alertmanager-operated.grafana.svc.cluster.local                                 9094      -          outbound      ORIGINAL_DST

cluster/outbound|9093||alertmanager.gmp-system.svc.cluster.local                                        alertmanager.gmp-system.svc.cluster.local                                       9093      -          outbound      ORIGINAL_DST

cluster/outbound|443||canvas-cert-manager-webhook.cert-manager.svc.cluster.local                        canvas-cert-manager-webhook.cert-manager.svc.cluster.local                      443       -          outbound      EDS

cluster/outbound|9402||canvas-cert-manager.cert-manager.svc.cluster.local                               canvas-cert-manager.cert-manager.svc.cluster.local                              9402      -          outbound      EDS

cluster/outbound|443||canvas-depapi-op-svc.canvas.svc.cluster.local                                     canvas-depapi-op-svc.canvas.svc.cluster.local                                   443       -          outbound      EDS

cluster/outbound|8083||canvas-keycloak-headless.canvas.svc.cluster.local                                canvas-keycloak-headless.canvas.svc.cluster.local                               8083      -          outbound      ORIGINAL_DST

cluster/outbound|8083||canvas-keycloak.canvas.svc.cluster.local                                         canvas-keycloak.canvas.svc.cluster.local                                        8083      -          outbound      EDS

cluster/outbound|80||canvas-keycloak2.canvas.svc.cluster.local                                          canvas-keycloak2.canvas.svc.cluster.local                                       80        -          outbound      EDS

cluster/outbound|8083||canvas-keycloak3.canvas.svc.cluster.local                                        canvas-keycloak3.canvas.svc.cluster.local                                       8083      -          outbound      EDS

cluster/outbound|5432||canvas-postgresql-hl.canvas.svc.cluster.local                                    canvas-postgresql-hl.canvas.svc.cluster.local                                   5432      -          outbound      ORIGINAL_DST

cluster/outbound|5432||canvas-postgresql.canvas.svc.cluster.local                                       canvas-postgresql.canvas.svc.cluster.local                                      5432      -          outbound      EDS

cluster/outbound|443||canvas-smanop-svc.canvas.svc.cluster.local                                        canvas-smanop-svc.canvas.svc.cluster.local                                      443       -          outbound      EDS

cluster/outbound|27017||canvas-svcinv-mongodb.canvas.svc.cluster.local                                  canvas-svcinv-mongodb.canvas.svc.cluster.local                                  27017     -          outbound      EDS

cluster/outbound|8200||canvas-vault-hc-internal.canvas-vault.svc.cluster.local                          canvas-vault-hc-internal.canvas-vault.svc.cluster.local                         8200      -          outbound      ORIGINAL_DST

cluster/outbound|8201||canvas-vault-hc-internal.canvas-vault.svc.cluster.local                          canvas-vault-hc-internal.canvas-vault.svc.cluster.local                         8201      -          outbound      ORIGINAL_DST

cluster/outbound|443||canvas-vault-hc-tls.canvas-vault.svc.cluster.local                                canvas-vault-hc-tls.canvas-vault.svc.cluster.local                              443       -          outbound      EDS
     canvas-vault-hc-dr.canvas-vault
cluster/outbound|8200||canvas-vault-hc.canvas-vault.svc.cluster.local                                   canvas-vault-hc.canvas-vault.svc.cluster.local                                  8200      -          outbound      EDS

cluster/outbound|8201||canvas-vault-hc.canvas-vault.svc.cluster.local                                   canvas-vault-hc.canvas-vault.svc.cluster.local                                  8201      -          outbound      EDS

cluster/outbound|80||canvas-vault-landing-page.canvas-vault.svc.cluster.local                           canvas-vault-landing-page.canvas-vault.svc.cluster.local                        80        -          outbound      EDS

cluster/outbound|8080||code-server.code-server.svc.cluster.local                                        code-server.code-server.svc.cluster.local                                       8080      -          outbound      EDS

cluster/outbound|443||compcrdwebhook.canvas.svc.cluster.local                                           compcrdwebhook.canvas.svc.cluster.local                                         443       -          outbound      EDS

cluster/outbound|80||default-http-backend.kube-system.svc.cluster.local                                 default-http-backend.kube-system.svc.cluster.local                              80        -          outbound      EDS

cluster/outbound|27017||demo-a-mongodb.components.svc.cluster.local                                     demo-a-mongodb.components.svc.cluster.local                                     27017     -          outbound      EDS

cluster/outbound|8080||demo-a-partyroleapi.components.svc.cluster.local                                 demo-a-partyroleapi.components.svc.cluster.local                                8080      -          outbound      EDS

cluster/outbound|8080||demo-a-prodcatapi.components.svc.cluster.local                                   demo-a-prodcatapi.components.svc.cluster.local                                  8080      -          outbound      EDS

cluster/outbound|4000||demo-a-productcatalogmanagement-sm.components.svc.cluster.local                  demo-a-productcatalogmanagement-sm.components.svc.cluster.local                 4000      -          outbound      EDS

cluster/outbound|80||echoservice.echoservice.svc.cluster.local                                          echoservice.echoservice.svc.cluster.local                                       80        -          outbound      EDS

cluster/outbound|443||gmp-operator.gmp-system.svc.cluster.local                                         gmp-operator.gmp-system.svc.cluster.local                                       443       -          outbound      EDS

cluster/outbound|8443||gmp-operator.gmp-system.svc.cluster.local                                        gmp-operator.gmp-system.svc.cluster.local                                       8443      -          outbound      EDS

cluster/outbound|80||info.canvas.svc.cluster.local                                                      info.canvas.svc.cluster.local                                                   80        -          outbound      EDS

cluster/outbound|80||istio-ingress.istio-ingress.svc.cluster.local                                      istio-ingress.istio-ingress.svc.cluster.local                                   80        -          outbound      EDS

cluster/outbound|443||istio-ingress.istio-ingress.svc.cluster.local                                     istio-ingress.istio-ingress.svc.cluster.local                                   443       -          outbound      EDS

cluster/outbound|15021||istio-ingress.istio-ingress.svc.cluster.local                                   istio-ingress.istio-ingress.svc.cluster.local                                   15021     -          outbound      EDS

cluster/outbound|443||istiod.istio-system.svc.cluster.local                                             istiod.istio-system.svc.cluster.local                                           443       -          outbound      EDS

cluster/outbound|15010||istiod.istio-system.svc.cluster.local                                           istiod.istio-system.svc.cluster.local                                           15010     -          outbound      EDS

cluster/outbound|15012||istiod.istio-system.svc.cluster.local                                           istiod.istio-system.svc.cluster.local                                           15012     -          outbound      EDS

cluster/outbound|15014||istiod.istio-system.svc.cluster.local                                           istiod.istio-system.svc.cluster.local                                           15014     -          outbound      EDS

cluster/outbound|53||kube-dns.kube-system.svc.cluster.local                                             kube-dns.kube-system.svc.cluster.local                                          53        -          outbound      EDS

cluster/outbound|8080||kube-prometheus-stack-alertmanager.grafana.svc.cluster.local                     kube-prometheus-stack-alertmanager.grafana.svc.cluster.local                    8080      -          outbound      EDS

cluster/outbound|9093||kube-prometheus-stack-alertmanager.grafana.svc.cluster.local                     kube-prometheus-stack-alertmanager.grafana.svc.cluster.local                    9093      -          outbound      EDS

cluster/outbound|9153||kube-prometheus-stack-coredns.kube-system.svc.cluster.local                      kube-prometheus-stack-coredns.kube-system.svc.cluster.local                     9153      -          outbound      ORIGINAL_DST

cluster/outbound|80||kube-prometheus-stack-grafana.grafana.svc.cluster.local                            kube-prometheus-stack-grafana.grafana.svc.cluster.local                         80        -          outbound      EDS

cluster/outbound|10257||kube-prometheus-stack-kube-controller-manager.kube-system.svc.cluster.local     kube-prometheus-stack-kube-controller-manager.kube-system.svc.cluster.local     10257     -          outbound      ORIGINAL_DST

cluster/outbound|2381||kube-prometheus-stack-kube-etcd.kube-system.svc.cluster.local                    kube-prometheus-stack-kube-etcd.kube-system.svc.cluster.local                   2381      -          outbound      ORIGINAL_DST

cluster/outbound|10249||kube-prometheus-stack-kube-proxy.kube-system.svc.cluster.local                  kube-prometheus-stack-kube-proxy.kube-system.svc.cluster.local                  10249     -          outbound      ORIGINAL_DST

cluster/outbound|10259||kube-prometheus-stack-kube-scheduler.kube-system.svc.cluster.local              kube-prometheus-stack-kube-scheduler.kube-system.svc.cluster.local              10259     -          outbound      ORIGINAL_DST

cluster/outbound|8080||kube-prometheus-stack-kube-state-metrics.grafana.svc.cluster.local               kube-prometheus-stack-kube-state-metrics.grafana.svc.cluster.local              8080      -          outbound      EDS

cluster/outbound|4194||kube-prometheus-stack-kubelet.kube-system.svc.cluster.local                      kube-prometheus-stack-kubelet.kube-system.svc.cluster.local                     4194      -          outbound      ORIGINAL_DST

cluster/outbound|10250||kube-prometheus-stack-kubelet.kube-system.svc.cluster.local                     kube-prometheus-stack-kubelet.kube-system.svc.cluster.local                     10250     -          outbound      ORIGINAL_DST

cluster/outbound|10255||kube-prometheus-stack-kubelet.kube-system.svc.cluster.local                     kube-prometheus-stack-kubelet.kube-system.svc.cluster.local                     10255     -          outbound      ORIGINAL_DST

cluster/outbound|443||kube-prometheus-stack-operator.grafana.svc.cluster.local                          kube-prometheus-stack-operator.grafana.svc.cluster.local                        443       -          outbound      EDS

cluster/outbound|9100||kube-prometheus-stack-prometheus-node-exporter.grafana.svc.cluster.local         kube-prometheus-stack-prometheus-node-exporter.grafana.svc.cluster.local        9100      -          outbound      EDS

cluster/outbound|8080||kube-prometheus-stack-prometheus.grafana.svc.cluster.local                       kube-prometheus-stack-prometheus.grafana.svc.cluster.local                      8080      -          outbound      EDS

cluster/outbound|9090||kube-prometheus-stack-prometheus.grafana.svc.cluster.local                       kube-prometheus-stack-prometheus.grafana.svc.cluster.local                      9090      -          outbound      EDS

cluster/outbound|443||kubernetes.default.svc.cluster.local                                              kubernetes.default.svc.cluster.local                                            443       -          outbound      EDS

cluster/outbound|443||metrics-server.kube-system.svc.cluster.local                                      metrics-server.kube-system.svc.cluster.local                                    443       -          outbound      EDS

cluster/outbound|9090||prometheus-operated.grafana.svc.cluster.local                                    prometheus-operated.grafana.svc.cluster.local                                   9090      -          outbound      ORIGINAL_DST

cluster/prometheus_stats                                                                                cluster/prometheus_stats                                                        -         -          -             STATIC

cluster/sds-grpc                                                                                        cluster/sds-grpc                                                                -         -          -             STATIC

cluster/outbound|5000||seccon.canvas.svc.cluster.local                                                  seccon.canvas.svc.cluster.local                                                 5000      -          outbound      EDS

cluster/xds-grpc                                                                                        cluster/xds-grpc                                                                -         -          -             STATIC


NAME                       ADDRESSES    PORT  MATCH                                                                                           DESTINATION
listener/10.92.0.10_53     10.92.0.10   53    ALL                                                                                             Cluster: outbound|53||kube-dns.kube-system.svc.cluster.local
listener/0.0.0.0_80        0.0.0.0      80    Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 80
listener/0.0.0.0_80        0.0.0.0      80    ALL                                                                                             PassthroughCluster
listener/10.92.14.187_80   10.92.14.187 80    Trans: raw_buffer; App: http/1.1,h2c                                                            Route: echoservice.echoservice.svc.cluster.local:80
listener/10.92.14.187_80   10.92.14.187 80    ALL                                                                                             Cluster: outbound|80||echoservice.echoservice.svc.cluster.local
listener/10.92.0.1_443     10.92.0.1    443   ALL                                                                                             Cluster: outbound|443||kubernetes.default.svc.cluster.local
listener/10.92.10.142_443  10.92.10.142 443   Trans: raw_buffer; App: http/1.1,h2c                                                            Route: gmp-operator.gmp-system.svc.cluster.local:443
listener/10.92.10.142_443  10.92.10.142 443   ALL                                                                                             Cluster: outbound|443||gmp-operator.gmp-system.svc.cluster.local
listener/10.92.12.37_443   10.92.12.37  443   Trans: raw_buffer; App: http/1.1,h2c                                                            Route: compcrdwebhook.canvas.svc.cluster.local:443
listener/10.92.12.37_443   10.92.12.37  443   ALL                                                                                             Cluster: outbound|443||compcrdwebhook.canvas.svc.cluster.local
listener/10.92.13.118_443  10.92.13.118 443   ALL                                                                                             Cluster: outbound|443||canvas-vault-hc-tls.canvas-vault.svc.cluster.local
listener/10.92.14.29_443   10.92.14.29  443   Trans: raw_buffer; App: http/1.1,h2c                                                            Route: metrics-server.kube-system.svc.cluster.local:443
listener/10.92.14.29_443   10.92.14.29  443   ALL                                                                                             Cluster: outbound|443||metrics-server.kube-system.svc.cluster.local
listener/10.92.4.157_443   10.92.4.157  443   ALL                                                                                             Cluster: outbound|443||kube-prometheus-stack-operator.grafana.svc.cluster.local
listener/10.92.6.233_443   10.92.6.233  443   ALL                                                                                             Cluster: outbound|443||canvas-cert-manager-webhook.cert-manager.svc.cluster.local
listener/10.92.7.31_443    10.92.7.31   443   ALL                                                                                             Cluster: outbound|443||istio-ingress.istio-ingress.svc.cluster.local
listener/10.92.7.61_443    10.92.7.61   443   ALL                                                                                             Cluster: outbound|443||canvas-smanop-svc.canvas.svc.cluster.local
listener/10.92.7.98_443    10.92.7.98   443   ALL                                                                                             Cluster: outbound|443||istiod.istio-system.svc.cluster.local
listener/10.92.8.234_443   10.92.8.234  443   ALL                                                                                             Cluster: outbound|443||canvas-depapi-op-svc.canvas.svc.cluster.local
listener/0.0.0.0_2381      0.0.0.0      2381  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 2381
listener/0.0.0.0_2381      0.0.0.0      2381  ALL                                                                                             PassthroughCluster
listener/0.0.0.0_4000      0.0.0.0      4000  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 4000
listener/0.0.0.0_4000      0.0.0.0      4000  ALL                                                                                             PassthroughCluster
listener/10.156.0.27_4194  10.156.0.27  4194  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: kube-prometheus-stack-kubelet.kube-system.svc.cluster.local:4194
listener/10.156.0.27_4194  10.156.0.27  4194  ALL                                                                                             Cluster: outbound|4194||kube-prometheus-stack-kubelet.kube-system.svc.cluster.local
listener/10.92.11.87_5000  10.92.11.87  5000  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: seccon.canvas.svc.cluster.local:5000
listener/10.92.11.87_5000  10.92.11.87  5000  ALL                                                                                             Cluster: outbound|5000||seccon.canvas.svc.cluster.local
listener/10.88.3.196_5432  10.88.3.196  5432  ALL                                                                                             Cluster: outbound|5432||canvas-postgresql-hl.canvas.svc.cluster.local
listener/10.92.11.117_5432 10.92.11.117 5432  ALL                                                                                             Cluster: outbound|5432||canvas-postgresql.canvas.svc.cluster.local
listener/0.0.0.0_8080      0.0.0.0      8080  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 8080
listener/0.0.0.0_8080      0.0.0.0      8080  ALL                                                                                             PassthroughCluster
listener/0.0.0.0_8083      0.0.0.0      8083  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 8083
listener/0.0.0.0_8083      0.0.0.0      8083  ALL                                                                                             PassthroughCluster
listener/10.88.3.203_8200  10.88.3.203  8200  ALL                                                                                             Cluster: outbound|8200||canvas-vault-hc-internal.canvas-vault.svc.cluster.local
listener/10.92.8.40_8200   10.92.8.40   8200  ALL                                                                                             Cluster: outbound|8200||canvas-vault-hc.canvas-vault.svc.cluster.local
listener/10.88.3.203_8201  10.88.3.203  8201  ALL                                                                                             Cluster: outbound|8201||canvas-vault-hc-internal.canvas-vault.svc.cluster.local
listener/10.92.8.40_8201   10.92.8.40   8201  ALL                                                                                             Cluster: outbound|8201||canvas-vault-hc.canvas-vault.svc.cluster.local
listener/10.92.10.142_8443 10.92.10.142 8443  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: gmp-operator.gmp-system.svc.cluster.local:8443
listener/10.92.10.142_8443 10.92.10.142 8443  ALL                                                                                             Cluster: outbound|8443||gmp-operator.gmp-system.svc.cluster.local
listener/0.0.0.0_9090      0.0.0.0      9090  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 9090
listener/0.0.0.0_9090      0.0.0.0      9090  ALL                                                                                             PassthroughCluster
listener/0.0.0.0_9093      0.0.0.0      9093  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 9093
listener/0.0.0.0_9093      0.0.0.0      9093  ALL                                                                                             PassthroughCluster
listener/10.88.3.25_9094   10.88.3.25   9094  ALL                                                                                             Cluster: outbound|9094||alertmanager-operated.grafana.svc.cluster.local
listener/0.0.0.0_9100      0.0.0.0      9100  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 9100
listener/0.0.0.0_9100      0.0.0.0      9100  ALL                                                                                             PassthroughCluster
listener/0.0.0.0_9153      0.0.0.0      9153  Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 9153
listener/0.0.0.0_9153      0.0.0.0      9153  ALL                                                                                             PassthroughCluster
listener/10.92.3.164_9402  10.92.3.164  9402  ALL                                                                                             Cluster: outbound|9402||canvas-cert-manager.cert-manager.svc.cluster.local
listener/0.0.0.0_10249     0.0.0.0      10249 Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 10249
listener/0.0.0.0_10249     0.0.0.0      10249 ALL                                                                                             PassthroughCluster
listener/10.156.0.27_10250 10.156.0.27  10250 ALL                                                                                             Cluster: outbound|10250||kube-prometheus-stack-kubelet.kube-system.svc.cluster.local
listener/0.0.0.0_10255     0.0.0.0      10255 Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 10255
listener/0.0.0.0_10255     0.0.0.0      10255 ALL                                                                                             PassthroughCluster
listener/0.0.0.0_10257     0.0.0.0      10257 Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 10257
listener/0.0.0.0_10257     0.0.0.0      10257 ALL                                                                                             PassthroughCluster
listener/0.0.0.0_10259     0.0.0.0      10259 Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 10259
listener/0.0.0.0_10259     0.0.0.0      10259 ALL                                                                                             PassthroughCluster
listener/virtualOutbound   0.0.0.0      15001 ALL                                                                                             PassthroughCluster
listener/virtualOutbound   0.0.0.0      15001 Addr: *:15001                                                                                   Non-HTTP/Non-TCP
listener/virtualInbound    0.0.0.0      15006 Addr: *:15006                                                                                   Non-HTTP/Non-TCP
listener/virtualInbound    0.0.0.0      15006 Trans: tls; App: istio-http/1.0,istio-http/1.1,istio-h2                                         InboundPassthroughCluster
listener/virtualInbound    0.0.0.0      15006 Trans: raw_buffer; App: http/1.1,h2c                                                            InboundPassthroughCluster
listener/virtualInbound    0.0.0.0      15006 Trans: tls; App: TCP TLS                                                                        InboundPassthroughCluster
listener/virtualInbound    0.0.0.0      15006 Trans: raw_buffer                                                                               InboundPassthroughCluster
listener/virtualInbound    0.0.0.0      15006 Trans: tls                                                                                      InboundPassthroughCluster
listener/virtualInbound    0.0.0.0      15006 Trans: tls; App: istio,istio-peer-exchange,istio-http/1.0,istio-http/1.1,istio-h2; Addr: *:8080 Cluster: inbound|8080||
listener/virtualInbound    0.0.0.0      15006 Trans: raw_buffer; Addr: *:8080                                                                 Cluster: inbound|8080||
listener/0.0.0.0_15010     0.0.0.0      15010 Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 15010
listener/0.0.0.0_15010     0.0.0.0      15010 ALL                                                                                             PassthroughCluster
listener/10.92.7.98_15012  10.92.7.98   15012 ALL                                                                                             Cluster: outbound|15012||istiod.istio-system.svc.cluster.local
listener/0.0.0.0_15014     0.0.0.0      15014 Trans: raw_buffer; App: http/1.1,h2c                                                            Route: 15014
listener/0.0.0.0_15014     0.0.0.0      15014 ALL                                                                                             PassthroughCluster
listener/0.0.0.0_15021     0.0.0.0      15021 ALL                                                                                             Inline Route: /healthz/ready*
listener/10.92.7.31_15021  10.92.7.31   15021 Trans: raw_buffer; App: http/1.1,h2c                                                            Route: istio-ingress.istio-ingress.svc.cluster.local:15021
listener/10.92.7.31_15021  10.92.7.31   15021 ALL                                                                                             Cluster: outbound|15021||istio-ingress.istio-ingress.svc.cluster.local
listener/0.0.0.0_15090     0.0.0.0      15090 ALL                                                                                             Inline Route: /stats/prometheus*
listener/10.92.3.77_27017  10.92.3.77   27017 ALL                                                                                             Cluster: outbound|27017||canvas-svcinv-mongodb.canvas.svc.cluster.local
listener/10.92.6.13_27017  10.92.6.13   27017 ALL                                                                                             Cluster: outbound|27017||demo-a-mongodb.components.svc.cluster.local

NAME                                                                       VHOST NAME                                                                            DOMAINS
                                                     MATCH                  VIRTUAL SERVICE
route/80                                                                   canvas-keycloak2.canvas.svc.cluster.local:80                                          canvas-keycloak2.canvas, 10.92.2.13
                                                     /*
route/80                                                                   canvas-vault-landing-page.canvas-vault.svc.cluster.local:80                           canvas-vault-landing-page.canvas-vault, 10.92.14.164
                                                     /*
route/80                                                                   default-http-backend.kube-system.svc.cluster.local:80                                 default-http-backend.kube-system, 10.92.10.8
                                                     /*
route/80                                                                   echoservice.echoservice.svc.cluster.local:80                                          echoservice.echoservice, 10.92.14.187
                                                     /*
route/80                                                                   info.canvas.svc.cluster.local:80                                                      info.canvas, 10.92.4.31
                                                     /*
route/80                                                                   istio-ingress.istio-ingress.svc.cluster.local:80                                      istio-ingress.istio-ingress, 10.92.7.31
                                                     /*
route/80                                                                   kube-prometheus-stack-grafana.grafana.svc.cluster.local:80                            kube-prometheus-stack-grafana.grafana, 10.92.10.140
                                                     /*
route/2381                                                                 kube-prometheus-stack-kube-etcd.kube-system.svc.cluster.local:2381                    kube-prometheus-stack-kube-etcd.kube-system, *.kube-prometheus-stack-kube-etcd.kube-system                                 /*
route/4000                                                                 demo-a-productcatalogmanagement-sm.components.svc.cluster.local:4000                  demo-a-productcatalogmanagement-sm, demo-a-productcatalogmanagement-sm.components + 1 more...                              /*
route/8080                                                                 code-server.code-server.svc.cluster.local:8080                                        code-server.code-server, 10.92.6.64
                                                     /*
route/8080                                                                 demo-a-partyroleapi.components.svc.cluster.local:8080                                 demo-a-partyroleapi, demo-a-partyroleapi.components + 1 more...                                                            /*
route/8080                                                                 demo-a-prodcatapi.components.svc.cluster.local:8080                                   demo-a-prodcatapi, demo-a-prodcatapi.components + 1 more...
                                                     /*
route/8080                                                                 kube-prometheus-stack-alertmanager.grafana.svc.cluster.local:8080                     kube-prometheus-stack-alertmanager.grafana, 10.92.8.68
                                                     /*
route/8080                                                                 kube-prometheus-stack-kube-state-metrics.grafana.svc.cluster.local:8080               kube-prometheus-stack-kube-state-metrics.grafana, 10.92.12.245                                                             /*
route/8080                                                                 kube-prometheus-stack-prometheus.grafana.svc.cluster.local:8080                       kube-prometheus-stack-prometheus.grafana, 10.92.10.45
                                                     /*
route/8083                                                                 canvas-keycloak-headless.canvas.svc.cluster.local:8083                                canvas-keycloak-headless.canvas, *.canvas-keycloak-headless.canvas                                                         /*
route/8083                                                                 canvas-keycloak.canvas.svc.cluster.local:8083                                         canvas-keycloak.canvas, 10.92.7.186
                                                     /*
route/8083                                                                 canvas-keycloak3.canvas.svc.cluster.local:8083                                        canvas-keycloak3.canvas, 10.92.1.25
                                                     /*
route/9090                                                                 kube-prometheus-stack-prometheus.grafana.svc.cluster.local:9090                       kube-prometheus-stack-prometheus.grafana, 10.92.10.45
                                                     /*
route/9090                                                                 prometheus-operated.grafana.svc.cluster.local:9090                                    prometheus-operated.grafana, *.prometheus-operated.grafana
                                                     /*
route/9093                                                                 alertmanager-operated.grafana.svc.cluster.local:9093                                  alertmanager-operated.grafana, *.alertmanager-operated.grafana                                                             /*
route/9093                                                                 alertmanager.gmp-system.svc.cluster.local:9093                                        alertmanager.gmp-system, *.alertmanager.gmp-system
                                                     /*
route/9093                                                                 kube-prometheus-stack-alertmanager.grafana.svc.cluster.local:9093                     kube-prometheus-stack-alertmanager.grafana, 10.92.8.68
                                                     /*
route/9100                                                                 kube-prometheus-stack-prometheus-node-exporter.grafana.svc.cluster.local:9100         kube-prometheus-stack-prometheus-node-exporter.grafana, 10.92.7.221                                                        /*
route/9153                                                                 kube-prometheus-stack-coredns.kube-system.svc.cluster.local:9153                      kube-prometheus-stack-coredns.kube-system, *.kube-prometheus-stack-coredns.kube-system                                     /*
route/10249                                                                kube-prometheus-stack-kube-proxy.kube-system.svc.cluster.local:10249                  kube-prometheus-stack-kube-proxy.kube-system, *.kube-prometheus-stack-kube-proxy.kube-system                               /*
route/10255                                                                kube-prometheus-stack-kubelet.kube-system.svc.cluster.local:10255                     kube-prometheus-stack-kubelet.kube-system, *.kube-prometheus-stack-kubelet.kube-system                                     /*
route/istio-ingress.istio-ingress.svc.cluster.local:15021                  istio-ingress.istio-ingress.svc.cluster.local:15021                                   *
                                                     /*
route/compcrdwebhook.canvas.svc.cluster.local:443                          compcrdwebhook.canvas.svc.cluster.local:443                                           *
                                                     /*
route/seccon.canvas.svc.cluster.local:5000                                 seccon.canvas.svc.cluster.local:5000                                                  *
                                                     /*
route/15014                                                                istiod.istio-system.svc.cluster.local:15014                                           istiod.istio-system, 10.92.7.98
                                                     /*
route/gmp-operator.gmp-system.svc.cluster.local:443                        gmp-operator.gmp-system.svc.cluster.local:443                                         *
                                                     /*
route/metrics-server.kube-system.svc.cluster.local:443                     metrics-server.kube-system.svc.cluster.local:443                                      *
                                                     /*
route/gmp-operator.gmp-system.svc.cluster.local:8443                       gmp-operator.gmp-system.svc.cluster.local:8443                                        *
                                                     /*
route/15010                                                                istiod.istio-system.svc.cluster.local:15010                                           istiod.istio-system, 10.92.7.98
                                                     /*
route/10257                                                                kube-prometheus-stack-kube-controller-manager.kube-system.svc.cluster.local:10257     kube-prometheus-stack-kube-controller-manager.kube-system, *.kube-prometheus-stack-kube-controller-manager.kube-system     /*
route/10259                                                                kube-prometheus-stack-kube-scheduler.kube-system.svc.cluster.local:10259              kube-prometheus-stack-kube-scheduler.kube-system, *.kube-prometheus-stack-kube-scheduler.kube-system                       /*
route/echoservice.echoservice.svc.cluster.local:80                         echoservice.echoservice.svc.cluster.local:80                                          *
                                                     /*
route/kube-prometheus-stack-kubelet.kube-system.svc.cluster.local:4194     kube-prometheus-stack-kubelet.kube-system.svc.cluster.local:4194                      *
                                                     /*
route/                                                                     backend                                                                               *
                                                     /healthz/ready*
route/inbound|8080||                                                       inbound|http|8080                                                                     *
                                                     /*
route/InboundPassthroughCluster                                            inbound|http|0                                                                        *
                                                     /*
route/                                                                     backend                                                                               *
                                                     /stats/prometheus*
route/InboundPassthroughCluster                                            inbound|http|0                                                                        *
                                                     /*
route/inbound|8080||                                                       inbound|http|8080                                                                     *
                                                     /*

RESOURCE NAME      TYPE           STATUS     VALID CERT     SERIAL NUMBER                        NOT AFTER                NOT BEFORE
secret/default     Cert Chain     ACTIVE     true           f134e735c7b276cde3bd9b907749dcfe     2024-11-23T09:16:17Z     2024-11-22T09:14:17Z
secret/ROOTCA      CA             ACTIVE     true           23259bc511973fede0c302de827e03f      2034-11-19T20:32:26Z     2024-11-21T20:32:26Z

NAME                                                      STATUS      LOCALITY                        CLUSTER
endpoint/10.88.3.242:8080                                 HEALTHY                                     inbound|8080||
endpoint/127.0.0.1:15020                                  HEALTHY                                     agent
endpoint/10.88.3.188:10250                                HEALTHY     europe-west3/europe-west3-a     outbound|443||canvas-cert-manager-webhook.cert-manager.svc.cluster.local
endpoint/10.88.3.191:9402                                 HEALTHY     europe-west3/europe-west3-a     outbound|9402||canvas-cert-manager.cert-manager.svc.cluster.local
endpoint/10.88.3.185:9443                                 HEALTHY     europe-west3/europe-west3-a     outbound|443||canvas-depapi-op-svc.canvas.svc.cluster.local
endpoint/10.88.3.192:8083                                 HEALTHY     europe-west3/europe-west3-a     outbound|8083||canvas-keycloak.canvas.svc.cluster.local
endpoint/10.88.3.192:8083                                 HEALTHY     europe-west3/europe-west3-a     outbound|80||canvas-keycloak2.canvas.svc.cluster.local
endpoint/10.88.3.192:8083                                 HEALTHY     europe-west3/europe-west3-a     outbound|8083||canvas-keycloak3.canvas.svc.cluster.local
endpoint/10.88.3.196:5432                                 HEALTHY     europe-west3/europe-west3-a     outbound|5432||canvas-postgresql.canvas.svc.cluster.local
endpoint/10.88.3.190:9443                                 HEALTHY     europe-west3/europe-west3-a     outbound|443||canvas-smanop-svc.canvas.svc.cluster.local
endpoint/10.88.3.195:27017                                HEALTHY     europe-west3/europe-west3-a     outbound|27017||canvas-svcinv-mongodb.canvas.svc.cluster.local
endpoint/10.88.3.203:8200                                 HEALTHY     europe-west3/europe-west3-a     outbound|443||canvas-vault-hc-tls.canvas-vault.svc.cluster.local
endpoint/10.88.3.203:8200                                 HEALTHY     europe-west3/europe-west3-a     outbound|8200||canvas-vault-hc.canvas-vault.svc.cluster.local
endpoint/10.88.3.203:8201                                 HEALTHY     europe-west3/europe-west3-a     outbound|8201||canvas-vault-hc.canvas-vault.svc.cluster.local
endpoint/10.88.3.209:80                                   HEALTHY     europe-west3/europe-west3-a     outbound|80||canvas-vault-landing-page.canvas-vault.svc.cluster.local
endpoint/10.88.3.30:8080                                  HEALTHY     europe-west3/europe-west3-a     outbound|8080||code-server.code-server.svc.cluster.local
endpoint/10.88.3.202:8443                                 HEALTHY     europe-west3/europe-west3-a     outbound|443||compcrdwebhook.canvas.svc.cluster.local
endpoint/10.88.3.17:8080                                  HEALTHY     europe-west3/europe-west3-a     outbound|80||default-http-backend.kube-system.svc.cluster.local
endpoint/10.88.3.243:27017                                HEALTHY     europe-west3/europe-west3-a     outbound|27017||demo-a-mongodb.components.svc.cluster.local
endpoint/10.88.3.237:8080                                 HEALTHY     europe-west3/europe-west3-a     outbound|8080||demo-a-partyroleapi.components.svc.cluster.local
endpoint/10.88.3.242:8080                                 HEALTHY     europe-west3/europe-west3-a     outbound|8080||demo-a-prodcatapi.components.svc.cluster.local
endpoint/10.88.3.238:4000                                 HEALTHY     europe-west3/europe-west3-a     outbound|4000||demo-a-productcatalogmanagement-sm.components.svc.cluster.local
endpoint/10.88.3.109:8080                                 HEALTHY     europe-west3/europe-west3-a     outbound|80||echoservice.echoservice.svc.cluster.local
endpoint/10.88.3.11:10250                                 HEALTHY     europe-west3/europe-west3-a     outbound|443||gmp-operator.gmp-system.svc.cluster.local
endpoint/10.88.3.187:8638                                 HEALTHY     europe-west3/europe-west3-a     outbound|80||info.canvas.svc.cluster.local
endpoint/10.88.3.135:80                                   HEALTHY     europe-west3/europe-west3-a     outbound|80||istio-ingress.istio-ingress.svc.cluster.local
endpoint/10.88.3.135:443                                  HEALTHY     europe-west3/europe-west3-a     outbound|443||istio-ingress.istio-ingress.svc.cluster.local
endpoint/10.88.3.135:15021                                HEALTHY     europe-west3/europe-west3-a     outbound|15021||istio-ingress.istio-ingress.svc.cluster.local
endpoint/10.88.3.182:15017                                HEALTHY     europe-west3/europe-west3-a     outbound|443||istiod.istio-system.svc.cluster.local
endpoint/10.88.3.182:15010                                HEALTHY     europe-west3/europe-west3-a     outbound|15010||istiod.istio-system.svc.cluster.local
endpoint/10.88.3.182:15012                                HEALTHY     europe-west3/europe-west3-a     outbound|15012||istiod.istio-system.svc.cluster.local
endpoint/10.88.3.182:15014                                HEALTHY     europe-west3/europe-west3-a     outbound|15014||istiod.istio-system.svc.cluster.local
endpoint/10.88.3.15:53                                    HEALTHY     europe-west3/europe-west3-a     outbound|53||kube-dns.kube-system.svc.cluster.local
endpoint/10.88.3.25:8080                                  HEALTHY     europe-west3/europe-west3-a     outbound|8080||kube-prometheus-stack-alertmanager.grafana.svc.cluster.local
endpoint/10.88.3.25:9093                                  HEALTHY     europe-west3/europe-west3-a     outbound|9093||kube-prometheus-stack-alertmanager.grafana.svc.cluster.local
endpoint/10.88.3.12:3000                                  HEALTHY     europe-west3/europe-west3-a     outbound|80||kube-prometheus-stack-grafana.grafana.svc.cluster.local
endpoint/10.88.3.13:8080                                  HEALTHY     europe-west3/europe-west3-a     outbound|8080||kube-prometheus-stack-kube-state-metrics.grafana.svc.cluster.local
endpoint/10.88.3.14:10250                                 HEALTHY     europe-west3/europe-west3-a     outbound|443||kube-prometheus-stack-operator.grafana.svc.cluster.local
endpoint/10.156.0.27:9100                                 HEALTHY     europe-west3/europe-west3-a     outbound|9100||kube-prometheus-stack-prometheus-node-exporter.grafana.svc.cluster.local
endpoint/10.88.3.27:8080                                  HEALTHY     europe-west3/europe-west3-a     outbound|8080||kube-prometheus-stack-prometheus.grafana.svc.cluster.local
endpoint/10.88.3.27:9090                                  HEALTHY     europe-west3/europe-west3-a     outbound|9090||kube-prometheus-stack-prometheus.grafana.svc.cluster.local
endpoint/10.156.0.2:443                                   HEALTHY                                     outbound|443||kubernetes.default.svc.cluster.local
endpoint/10.88.3.23:10250                                 HEALTHY     europe-west3/europe-west3-a     outbound|443||metrics-server.kube-system.svc.cluster.local
endpoint/127.0.0.1:15000                                  HEALTHY                                     prometheus_stats
endpoint/./var/run/secrets/workload-spiffe-uds/socket     HEALTHY                                     sds-grpc
endpoint/10.88.3.186:5000                                 HEALTHY     europe-west3/europe-west3-a     outbound|5000||seccon.canvas.svc.cluster.local
endpoint/./etc/istio/proxy/XDS                            HEALTHY                                     xds-grpc
```