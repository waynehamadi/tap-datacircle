# tap-datacircle

Singer tap for the Datacircle API (https://api.datacircle.dev/v1). It lists every GTM API on https://datacircle.dev and every plan, with its score and price. No key.

Streams: `apis`, `plans`.

```
meltano add extractor tap-datacircle --from-ref https://hub.meltano.com/meltano/api/v1/plugins/extractors/tap-datacircle--waynehamadi
```
