import requests
import json

url = "https://www.walmart.com/orchestra/home/graphql"

payload = json.dumps({
  "query": "query AdV2( $platform:Platform! $pageId:String! $pageType:PageType! $tenant:String! $moduleType:ModuleType! $pageContext:PageContextIn $locationContext:LocationContextIn $moduleConfigs:JSON $adsContext:AdsContextIn $adRequestComposite:AdRequestCompositeIn ){adV2( platform:$platform pageId:$pageId pageType:$pageType tenant:$tenant moduleType:$moduleType locationContext:$locationContext pageContext:$pageContext moduleConfigs:$moduleConfigs adsContext:$adsContext adRequestComposite:$adRequestComposite ){status adContent{type data{__typename...AdDataDisplayAdFragment __typename...AdDataSponsoredProductsFragment __typename...AdDataSponsoredVideoFragment}}}}fragment AdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment AdDataSponsoredProductsFragment on AdData{...on SponsoredProducts{adUuid adExpInfo moduleInfo products{...ProductFragment}}}fragment ProductFragment on Product{usItemId offerId badges{flags{__typename...on BaseBadge{id text key query type}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought criteria{name value}}}labels{__typename...on BaseBadge{id text key}...on PreviouslyPurchasedBadge{id text key lastBoughtOn numBought}}tags{__typename...on BaseBadge{id text key}}}priceInfo{priceDisplayCodes{rollback reducedPrice eligibleForAssociateDiscount clearance strikethrough submapType priceDisplayCondition unitOfMeasure pricePerUnitUom}currentPrice{price priceString priceDisplay}wasPrice{price priceString}priceRange{minPrice maxPrice priceString}unitPrice{price priceString}savingsAmount{priceString}comparisonPrice{priceString}}showOptions sponsoredProduct{spQs clickBeacon spTags}canonicalUrl numberOfReviews averageRating availabilityStatus imageInfo{thumbnailUrl allImages{id url}}name fulfillmentBadge classType type showAtc p13nData{predictedQuantity flags{PREVIOUSLY_PURCHASED{text}CUSTOMERS_PICK{text}}labels{PREVIOUSLY_PURCHASED{text}CUSTOMERS_PICK{text}}}brand}fragment AdDataSponsoredVideoFragment on AdData{...on SponsoredVideos{adUuid adExpInfo moduleInfo videos{video{vastXml thumbnail spqs}products{...ProductFragment}}}}",
  "variables": {
    "adRequestComposite": {
      "facets": "",
      "keyword": "70 inch television",
      "isDebug": False,
      "isManualShelf": False
    },
    "adsContext": {
      "locationContext": {
        "zipCode": "10001",
        "stateCode": "NY",
        "storeId": "3520",
        "pickupStore": "3520",
        "deliveryStore": "3520",
        "intent": "SHIPPING",
        "incatchment": False
      },
      "itemId": "",
      "categoryId": "3944_1060825_447913",
      "categoryName": "Electronics/TV & Video/All TVs",
      "brand": "",
      "productName": "",
      "productTypeId": "",
      "normKeyword": "70 inch television",
      "verticalId": "ets",
      "dedupeList": []
    },
    "pageContext": {
      "searchNormalize": {
        "verticalId": "ets",
        "normalized_query": "70 inch television",
        "original_query": "70 inch tv",
        "rewritten_query": "70 inch tv",
        "specificity": "broad",
        "top_query_cat_path": "/3944/1060825/447913",
        "top_query_cat_path_name": "/Electronics/TV & Video/All TVs",
        "product_type": [
          {
            "name": "Televisions",
            "score": 1,
            "source": "odyssey_override"
          }
        ],
        "analytics_log": {
          "fe_log": {
            "dept": "/3944/1060825/447913",
            "g": "SA",
            "s": "b",
            "trf": "ht"
          }
        }
      }
    },
    "pageId": "70 inch tv",
    "pageType": "SEARCH",
    "platform": "DESKTOP",
    "tenant": "WM_GLASS",
    "locationContext": {
      "storeId": "3520",
      "stateCode": "NY",
      "zipCode": "10001"
    },
    "moduleConfigs": {
      "moduleLocation": "bottom",
      "lazy": "1000"
    },
    "moduleType": "SponsoredProductCarousel"
  }
})
headers = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'content-type': 'application/json',
  'cookie': 'TBV=7; _pxvid=983e4b84-7212-11ed-bd7c-796d47796b56; vtc=Ye7F8Hz3m_c1U1KtVwT2yk; _pxhd=7829b574d83c7ad365f6762d8cba265c1c79190a9fdfe0f59a56c98c1b847792:985ca1b3-7212-11ed-992d-7177716b766d; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1670300403176; adblocked=false; hasLocData=1; TB_SFOU-100=; dimensionData=541; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; CID=67f167ad-6378-486d-b9e0-dce9e93206e5; hasCID=1; SPID=c896c7f77b2584836eab901a67d47490bc7db8dc066e1bd60ade890c5684d52883d85105ae2937e40d9f1c639d600b24cprof; type=REGISTERED; _vc=9Rso87QQ%2BB9dz5yiR29F0oCcdfUHRUbbitENqzvjOtI%3D; customer=%7B%22firstName%22%3A%22Ratul%22%2C%22lastNameInitial%22%3A%22T%22%7D; _m=9; assortmentStoreId=3520; userContext=eyJhZGRyZXNzRGF0YSI6bnVsbCwiaGFzSXRlbVN1YnNjcmlwdGlvbiI6ZmFsc2UsImhhc01lbWJlcnNoaXBJbmZvIjpmYWxzZSwiaXNEZWZhdWx0IjpmYWxzZSwicGF5bWVudERhdGEiOnsiY2FwaXRhbE9uZUJhbm5lclNub296ZVRTIjowLCJoYXNDYXBPbmUiOmZhbHNlLCJoYXNDYXBPbmVMaW5rZWQiOmZhbHNlLCJoYXNDcmVkaXRDYXJkIjpmYWxzZSwiaGFzRGlyZWN0ZWRTcGVuZENhcmQiOmZhbHNlLCJoYXNFQlQiOmZhbHNlLCJoYXNHaWZ0Q2FyZCI6ZmFsc2UsInNob3dDYXBPbmVCYW5uZXIiOnRydWUsIndwbHVzTm9CZW5lZml0QmFubmVyIjp0cnVlLCJwYXltZW50TWV0aG9kVGFncyI6W10sImhhc1BheXBhbEJBIjpmYWxzZX0sInByb2ZpbGVEYXRhIjp7ImlzQXNzb2NpYXRlIjpmYWxzZSwiaXNUZXN0QWNjb3VudCI6ZmFsc2UsImN1c3RvbWVyVHlwZSI6IklORElWSURVQUwiLCJtZW1iZXJzaGlwT3B0SW4iOnsiaXNPcHRlZEluIjpmYWxzZX19LCJzaG93U2lnblVwU3BsYXNoIjp0cnVlfQ%3D%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIzNTIwIiwiZGlzcGxheU5hbWUiOiJTZWNhdWN1cyBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiIwNzA5NCIsImFkZHJlc3NMaW5lMSI6IjQwMCBQYXJrIFBsIiwiY2l0eSI6IlNlY2F1Y3VzIiwic3RhdGUiOiJOSiIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiMDcwOTQtMzY1NCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6NDAuNzkyOTg3LCJsb25naXR1ZGUiOi03NC4wNDI0Mjl9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzNTIwIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl19XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjo0MC43NTA5LCJsb25naXR1ZGUiOi03My45OTc1LCJwb3N0YWxDb2RlIjoiMTAwMDEiLCJjaXR5IjoiTmV3IFlvcmsiLCJzdGF0ZSI6Ik5ZIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjM1MjAiLCJkaXNwbGF5TmFtZSI6IlNlY2F1Y3VzIFN1cGVyY2VudGVyIiwiYWNjZXNzUG9pbnRzIjpudWxsLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6W10sImludGVudCI6IlBJQ0tVUCIsInNjaGVkdWxlRW5hYmxlZCI6ZmFsc2V9LCJpbnN0b3JlIjpmYWxzZSwicmVmcmVzaEF0IjoxNjcyMTg4MjM3NjIxLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NjdmMTY3YWQtNjM3OC00ODZkLWI5ZTAtZGNlOWU5MzIwNmU1In0%3D; bstc=c2GYt0pSly2DW2ePf4iwDo; mobileweb=0; xptc=assortmentStoreId%2B3520; xpth=x-o-mverified%2Bfalse; xpa=9DCwR|Aj49u|BciIR|DSZXu|Qo6mX|W4LIu|Ym5YS|i9yTi|kvhAJ|tTQ2Y; exp-ck=DSZXu3Qo6mX1W4LIu1i9yTi1tTQ2Y1; _astc=7f3ed9da157fbce7dfb5b224fca80099; pxcts=6d867c7f-8616-11ed-b0de-6557454c5142; wmlh=b5d1c19e6ceec7bf79e2f2088fa6e7b1157b95a4086c9256863dda31c548ed17; bm_mi=3ACA45C7735DA8052738658DC3F27812~YAAQFEw5F06ZTTmFAQAABXjwVBKU/imuEShDf+jkFfTbDISTAaHEHQjPfqwIpRRkZnfm0qBl0kK9NwB+rIsmtoZZnwXTG8Zcxc6uv6mYJ/xhEZ3ScdCrW4/M/JJlcaftkW4hGME+4JFQ+aoyGYMpJuEGu48cBzkAqP2S9llsb4GrB5ADLC81iPDI4FaMvrASb18QQp3/YS+OTAI7ou8I4H9fWX/KCJAkMAo8TLLcP8v1RJ6X6X5p53v+MgQ2MXXLkI+D8Ne34amyUW5m9qCxfHI1cMJeT2uqEEPQHR367fLmDxupOV/4G1UTFUKXUM9xR+m+HfM=~1; bm_sv=2EA1ED91C94261C83FBA9440EBAFD543~YAAQFEw5F3uZTTmFAQAAo33wVBLBi4E4kTpvm1l9RuHs0pECAbzJvKXXxLt4Tr1mvGMjNqHEZ5Gy2is5P4UPz/ewtoypMJowR9pc7A6dN/6z4WxKrnvKCNjjYzv1mt1PupcclyYcZVhGcPpE6obCSKS/KERkw+YySsam0IMpoSfx6Q89NVe3r0SyI/tt1DvDNv6Xd8S19k5YplVvYBTy8lewJtAGsbHoeOTCCMXkS/K7LWa3uEmjuPyVQH3dlnQHeOM=~1; ak_bmsc=DA63897BBC9610A1C4444244DD1EE372~000000000000000000000000000000~YAAQFEw5FymdTTmFAQAAeknxVBIJTdDcYnIz8o3JaunUeH+7TDD0vgtq1m72xQLDGKVzHtZETWAex7MUOCACbbQty7HSZEWma5nM4v6LU6b//IX2N7fiU1yq/OecGJu06b27Ka0hI8JxHGCNJuJUYAVuA3yi8baTr3o6Imcntwlb0t9pw+AJ1Xg3iSk0V8LfZaiVoLv85AIrokv649WA5IFx0YLUfY6AjEOxDS5WTI7i3YD4tiunAo9ShqQbxmaE4kJfTSTXIn3Cp9WVuZS0ea30uWaDU8qIMg2+tJt+PcGYqjf53PEbNl3MLLQ6rcSpwbPXPGb1fi/re3MmdvwHMKP8Ph1NOuEWbxT7TSH92coC0GRva1zPv4nz5dwj3cxEkaPN+tSnA5ZsqV2dIN7YxeLpnG1i41GGJ4JPDw5e5nKefYOFDV3rop+qGr47eBj914tpORclcy1c5MCrSZYIWgLTaLxoa+Zh5axa8Yr8+8tSi2ngWb2I6QhzU3JTD+wYaqCcZSpws6lj8q8=; _px3=f82caba6fab61dcad9244e7941fc5e849e82fd455940ac7c29a2dac8198125c7:Ujva4lG/pil24G1aMXiO0R+Eum8SxuFGoU1AwJK6didzc9ilrciK9Zj3uPra+rB7YQZyDkV1iNnFzlo0Ed8oMg==:1000:f0IvIkwKzziarwgi8iCZjUyC+Xa8EVxxV2DmHv4suOQekWUi2KSiwPlxkKw+1UcVkvGb5F87UX6MBrZJDVDyMXPx0a5FxlDDLYkVPJePXS7aQSJWXKiFnC0GPNKL0XsLFQV5Xd9I2vBqT89frPNZmm/q/eGETagg02kAMSS1ipv2F3HoanmjFOuuLih/VbldLNdMgQToBwyb3VSzqy6xhg==; auth=MTAyOTYyMDE41EwIYXzRhiQJK3gWNv%2FAptdwlbhMZIh1B36vO4S2tL2JLk%2FQDmk1ws9aXLNisP1DZXiDIpWMfX2PK0%2FwgTp%2B6E9YXptqDS44VDez3iGKD%2FXxl773I%2B54vTjXFs8Snxk2RMvR4vpAGLQJj3IgMhxayiZgO9lwKKbgMeyPyqeNSEQj74OhBgCRtFdi%2B92ab4e8eLzeYEOkfscjU8H92nBf1FL6CZSzVZykBKTRtORKnJURySQL7SCCuAOGuvhBj5fO2IeG6ko0c6kXUwqfjr3d%2B4NScfvMf1%2F4idPYnRKjm5bcLGx45ryx5AIZ9HTwA6xpbMY%2FLpxb%2F6aaOcTIurbDeSd8tQCu2lRl6bCDsyGccLi4vWJxck%2BpgPZ6QTem%2FZeJHjWkSNVWdJoHKKB0CLdT%2ByVgMT6bIhqKDpxu2PMUdWw%3D; xptwj=rq:6108d5d6ae3dd205c062:0jx33Q3MBCkjwNCUtWF2/01Fy5b1PyUqfm57sv7ryuL+SK3RCqeNzhZsmemjUUzyxkA+iv/hQSrqTpZy9V0hMnQOOHyN7wW67K4VLdafgNByNuk8EVJ9+U+/kivtnvuWeze7ixK+UoM5Y0+7e1B5iPwlulosTw==; akavpau_p2=1672168276~id=6f74698f6eb2886a2b419632f03d23d0; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1672167675000@firstcreate:1670300403176"; xpm=0%2B1672167675%2BYe7F8Hz3m_c1U1KtVwT2yk~67f167ad-6378-486d-b9e0-dce9e93206e5%2B0; xptwg=763336309:10A2E50122B4B00:2ABAFB8:97D394E4:D7ACCE:214A3574:; TS012768cf=012aaf475069e39473e9335bb07d54e2a908d096414209589dd38412cf44b8f445594e9469369bd7eb856f07f009d3bed9aafc1eb0; TS01a90220=012aaf475069e39473e9335bb07d54e2a908d096414209589dd38412cf44b8f445594e9469369bd7eb856f07f009d3bed9aafc1eb0; TS2a5e0c5c027=0824e48b03ab2000955779c2bd0e10e807248b128e511300370e11fbe52247c1f37c8f3e5c16365208a85f4b70113000f6917ef76832653f734ba6385aa794212e7f1feaf28c655febc33611223deabc8cff7d7624c7930f579040d02828de93; SPID=c896c7f77b2584836eab901a67d47490bc7db8dc066e1bd60ade890c5684d52883d85105ae2937e40d9f1c639d600b24cprof; TB_SFOU-100=; TS01a90220=0189107c98c44e57cfd37305599541b723b7ec9a74970e9a90a6f33b4a445672713491aae4c0f2fbf10c69fda0af56d22c3d97acf1; auth=MTAyOTYyMDE41EwIYXzRhiQJK3gWNv%2FAptdwlbhMZIh1B36vO4S2tL2JLk%2FQDmk1ws9aXLNisP1DZXiDIpWMfX2PK0%2FwgTp%2B6E9YXptqDS44VDez3iGKD%2FXxl773I%2B54vTjXFs8Snxk2RMvR4vpAGLQJj3IgMhxayiZgO9lwKKbgMeyPyqeNSEQj74OhBgCRtFdi%2B92ab4e8eLzeYEOkfscjU8H92nBf1FL6CZSzVZykBKTRtORKnJURySQL7SCCuAOGuvhBj5fO2IeG6ko0c6kXUwqfjr3d%2B4NScfvMf1%2F4idPYnRKjm5bcLGx45ryx5AIZ9HTwA6xpbMY%2FLpxb%2F6aaOcTIurbDeSd8tQCu2lRl6bCDsyGccLi4vWJxck%2BpgPZ6QTem%2FZeJHjWkSNVWdJoHKKB0CLdT%2ByVgMT6bIhqKDpxu2PMUdWw%3D; bstc=c2GYt0pSly2DW2ePf4iwDo; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1672168213000@firstcreate:1670300403176"; exp-ck=DSZXu3Qo6mX1W4LIu1i9yTi1tTQ2Y1; mobileweb=0; vtc=Ye7F8Hz3m_c1U1KtVwT2yk; xpa=9DCwR|Aj49u|BciIR|DSZXu|Qo6mX|W4LIu|Ym5YS|i9yTi|kvhAJ|tTQ2Y; xpm=0%2B1672168213%2BYe7F8Hz3m_c1U1KtVwT2yk~67f167ad-6378-486d-b9e0-dce9e93206e5%2B0; xptc=assortmentStoreId%2B3520; xpth=x-o-mverified%2Bfalse; xptwg=2101733530:14B83885613A4D0:3537E6C:B876A57F:843E3963:26E87E:; TS012768cf=0189107c98c44e57cfd37305599541b723b7ec9a74970e9a90a6f33b4a445672713491aae4c0f2fbf10c69fda0af56d22c3d97acf1; TS2a5e0c5c027=085c9e3cb8ab2000005bf08ef295ee24e5645c11c005ac71c7c993f3171938407a19965d9c7deeac080b840eca11300019be13775a1d9c926f0a4c1565892a33161ea7e99c9070faf2eddc37300a06bf0b7b42400ec5ea81d02a58fbcb59db5b; _pxhd=cb6c08c6093050c6f7bb3cb85956b100db258977c56b0868b7909672869cef95:39808c6e-757f-11ed-8486-707461506f42',
  'device_profile_ref_id': '5OkOxlmPryYvTMeg1pCTsrTmzOMW5dh3MO-G',
  'origin': 'https://www.walmart.com',
  'referer': 'https://www.walmart.com/search?q=70+inch+tv&page=2&affinityOverride=default',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-5871d13800e0ea0a6e9fd5d423506d01-795d391e66da1efc-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/search?q=70+inch+tv&page=2&affinityOverride=default',
  'wm_qos.correlation_id': 'Idyl_pbHBYU0fFQReboHa6SSjf2gpz1ksBM2',
  'x-apollo-operation-name': 'AdV2',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'Idyl_pbHBYU0fFQReboHa6SSjf2gpz1ksBM2',
  'x-o-gql-query': 'query AdV2',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.35.0-1888e6-1221T1819',
  'x-o-segment': 'oaoh'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
