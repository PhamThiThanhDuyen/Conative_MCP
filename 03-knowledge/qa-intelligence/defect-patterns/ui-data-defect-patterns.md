# UI / Data Defect Patterns

| Pattern | Signal | Evidence to capture |
|---|---|---|
| UI/API mismatch | UI shows value different from API response | Screenshot, network response, expected rule |
| Report metric mismatch | Dashboard/report value differs from source data | UI value, source query/API, formula/rule ID |
| Stale cache | Update succeeds but old data remains visible | Before/after timestamps, cache headers, refresh behavior |
| Missing loading/error state | Slow/failing request leaves blank or misleading UI | Network throttle/error, screenshot/video |
| Permission leak | User sees action/data outside role | Role/account, UI screenshot, API response |
| Empty state failure | No data produces broken layout or wrong message | Seed state, screenshot, console |
| Timezone/currency mismatch | Values differ by locale or timezone | Account locale/TZ, input, expected formatting rule |
| Duplicate submission | Repeated click/request creates duplicate record | UI action video, API requests, data state |
