
# Serveless Function

Deploy a serveless function to the cloud

## Task

1. Deploy a serverless function to the cloud.
2. Create a repository on Github and link it to Vercel account.
3. Create a serverless function following Vercel’s steps.
4. The function should handle a GET http request.
5. The function should accomplish some useful task.
6. The function should parse the url path’s query string.

## Vervel Link

<https://serverless-kohl-seven.vercel.app/api/server?lang>

## Functionality

 The server dispaly a greating based on choosen language abbriviations.
 Supported language abbriviations include : ar, az, be, bg, bn, bs, cs, da, de, dz, el, en, en-gb, en-us, es, et, fa, fi, fil, fr, he, hi, hr, hu, hy, id, is, it, ja, ka, kk, km, ko, lb, lo, lt, lv, mk, mn, ms, my, ne, no, pl, pt, ro, ru, sk, sl, sq, sr, sv, sw, th, tk, uk, vi, zh

 Example : <https://serverless-kohl-seven.vercel.app/api/server?lang=sw> should display a greating in swahili

 Change laguage to another abbriviation should change appropriatly

 Incase no language search criteria is provided, the server prompts "Please provide a valid language abbriviation" and displays some of the accepted language abbriviations
