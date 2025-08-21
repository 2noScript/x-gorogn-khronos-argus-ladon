import time
from urllib.parse import urlencode

import requests
import urllib
from lib.sign import Sign
from lib.utils import getUNIX, md5stub
import json
import secrets

ts = getUNIX(False)
rticket = getUNIX(True)
random_hex = secrets.token_hex(16)

target = {
    # "user_id": "7510342465174782984",
    "sec_user_id": "MS4wLjABAAAAq01Ll9E-IpN_usNz54cfj_gv0YGxKI3P1PM7F1SgLV_XjTtOTdibSDKLzimMDs5l",
}


params = {
    **target,
    "city": "",
    "rec_type": "1-5",
    "from": "14",
    "from_pre": "-1",
    "type": "1",
    "link_sharer": "0",
    "channel_id": "23",
    "iid": "7540757869902481160",
    "device_id": "7540757128744928823",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "250904",
    "version_name": "25.9.4",
    "device_platform": "android",
    "ab_version": "25.9.4",
    "ssmix": "a",
    "device_type": "sdk_gphone64_arm64",
    "device_brand": "google",
    "language": "en",
    "os_api": "33",
    "os_version": "13",
    "openudid": "38572b261a88733e",
    "manifest_version_code": "2022509040",
    "resolution": "1080*2209",
    "dpi": "420",
    "update_version_code": "2022509040",
    "_rticket": rticket,
    "current_region": "US",
    "app_type": "normal",
    "sys_region": "US",
    "mcc_mnc": "310260",
    "timezone_name": "Asia/Ho_Chi_Minh",
    "carrier_region_v2": "310",
    "residence": "US",
    "app_language": "en",
    "carrier_region": "US",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "US",
    "timezone_offset": "25200",
    "build_number": "25.9.4",
    "host_abi": "arm64-v8a",
    "locale": "en",
    "region": "US",
    "ts": ts,
    "cdid": "0d112b87-c4df-49c9-8378-df13f164b1fd",
}

params_string = urllib.parse.urlencode(params)

baseheader = {
    "sdk-version": "2",
    "multi_login": "1",
    "passport-sdk-version":"19",
    "x-ss-req-ticket": str(getUNIX(True)),
    "x-bd-kmsv": "0",
    "x-vc-bdturing-sdk-version":"2.2.1.i18n",
    "x-tt-dm-status": "login=1;ct=1;rt=1",
    "x-tt-cmpl-token":"AgQQAPOFF-RPsIvOOCbAsNk78se_lEPJP7XZYN0YWA",
    "x-tt-store-region": "vn",
    "x-tt-store-region-src": "uid",
    "x-ss-dp": "1233",
    "user-agent": "com.zhiliaoapp.musically/2022509040 (Linux; U; Android 13; en_US; sdk_gphone64_arm64; Build/TE1A.240213.009; Cronet/TTNetVersion:ae513f3c 2022-08-08 QuicVersion:12a1d5c5 2022-06-27)",


    # "x-tt-token":"0322b33b32e60b0a861da7236e2ca938c9060bb7cc6cd27acb3c757535687dd9199279e03973a68df6e970f76d4442c808e783876e30ab30c2d0727f5c4a766def5fc1d941191536407071e06ea85248d7888af060b80764e97eed86dbbe808c7e198--0a4e0a20bc057022443ec62804acd111fa2b5259d82e972d9c50b3280f9d8bc3b4a5578712206a2295071965a383ea8631f430bcbe1c3b2fb8386da5550553ac4069accb46821801220674696b746f6b-3.0.0",
    # "cookie":"tt_chain_token=mvL/lmn17Qiz3ct10Lg8qg==; delay_guest_mode_vid=8; fbm_1862952583919182=base_domain=.www.tiktok.com; d_ticket=5bccb5b88fc8bd19a3028c99b57da81d5f09c; ttwid=1%7CKZnaIsRKXB01eDqrvBoT5-uSOcDVaLCCuvRQ93m64yU%7C1745002064%7Cbb27bce0855c2103509efb64accf2feb466f0b99377508fccf4f6373a1278d85; _ga=GA1.1.838012618.1746579444; _ga_LWWPCY99PB=GS1.1.1746581759.2.0.1746581759.0.0.774280846; _tt_enable_cookie=1; from_way=paid; tta_attr_id_mirror=0.1747383352.7504954349848969217; _yjsu_yjad=1748029415.46a3928f-c27a-4412-93eb-477add1cbd05; _gtmeec=e30%3D; ttcsid_C97F413C77U6S6FS3KBG=1748029415738::NmZbrGw8XKcET9BulKUh.1.1748029422804; ttcsid_C97F14JC77U63IDI7U40=1748029415739::H6PoZ-xRTt8FNgS-sLaJ.1.1748029422804; ttcsid_C97F65JC77UB71TGK1OG=1748029415739::Js1J5kQxC_F7HrBNksc4.1.1748029422804; ttcsid_C97F83JC77UC6ALACM60=1748029415739::7-EKoxvj-RW3asn23Tej.1.1748029422805; ttcsid_C97F9QBC77U37LFVJTOG=1748029415739::rT5pOARymoBc1tZIlyEU.1.1748029422805; ttcsid_CDICPPBC77UFUTJBVLI0=1748029415914::E8Vs5T4MRYpqS55E7mwJ.1.1748029422805; ttcsid_CS7J93RC77U6TI82IEB0=1748029415927::mGC-UZADI5i8ntOtH0Hs.1.1748029422805; ttcsid_CBUS2N3C77UB6N0891N0=1748029415937::d-8eR2Srf8TAmabHpwdU.1.1748029422806; ttcsid_CGCP5PJC77U5LCHF3VG0=1748029415941::nwd0p8zvI3dN8XA5mut8.1.1748029422806; _ga_HV1FL86553=GS1.1.1748029415.1.1.1748029443.0.0.651138025; _ga_R5EYE54KWQ=GS1.1.1748029415.1.1.1748029443.0.0.620614736; d_ticket_ads=a22f30eb1062b75746d4481855791cbd5f09c; sid_guard_ads=8f7a6742f870ca5ffe883399f9be5cbd%7C1748213056%7C5183999%7CThu%2C+24-Jul-2025+22%3A44%3A15+GMT; _fbp=fb.1.1748213205894.1481826544; living_user_id=209632895245; _ttp=2xXge4GNOarZwzujgSmsEdxRZ3X.tt.1; sid_guard_tiktokseller=c73a1344914af729243a98ba9f896a09%7C1750172867%7C3224190%7CThu%2C+24-Jul-2025+22%3A44%3A17+GMT; ttcsid_CMSS13RC77U1PJEFQUB0=1750172866412::uP37B8u2RVosxYOVBOvZ.3.1750172893965; ttcsid=1750172866413::_Uxknlhit8WIGNowVKqB.4.1750172893965; _gcl_aw=GCL.1750172905.CjwKCAjwpMTCBhA-EiwA_-MsmfmSCuFZUbFTgJsRcaLWtTYDz_CD7tl9LYRgu1GMnY8sqqTyPY5QkRoCgmQQAvD_BwE; _gcl_gs=2.1.k1$i1750172904$u51132715; _ga_BZBQ2QHQSP=GS2.1.s1750172865$o3$g1$t1750172905$j0$l0$h458571879; FPGCLAW=2.1.kCjwKCAjwpMTCBhA-EiwA_-MsmfmSCuFZUbFTgJsRcaLWtTYDz_CD7tl9LYRgu1GMnY8sqqTyPY5QkRoCgmQQAvD_BwE$i1750172906; FPGCLGS=2.1.k1$i1750172904$u51132715; _ga_NBFTJ2P3P3=GS1.1.1750172911.3.1.1750173400.0.0.1666603310; store-country-code=vn; store-country-code-src=uid; tt-target-idc=alisg; last_login_method=QRcode; tt_csrf_token=oQCcdQON-fYFgTreY1fFrxe-K5Kd1kITx3fk; s_v_web_id=verify_mdom9u10_Bm5J5Xr9_QU4X_4exK_AIWf_OGTrBhRRiTSv; passport_fe_beating_status=true; csrf_session_id=da0811a436c1c65604c4b08aa0869a74; gd_random=eyJtYXRjaCI6ZmFsc2UsInBlcmNlbnQiOjAuMzA3MjgyMjEwNTUyNTE2OH0=.pwuLhI+7Bpxy0xcb7DzD1Gn09YSm8PR/ZhInwP2Xwcw=; _tea_utm_cache_1988={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; _tea_utm_cache_594856={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; _tea_utm_cache_548444={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; _tea_utm_cache_345918={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; tiktok_webapp_theme=dark; passport_csrf_token=b9130cb9bce642cd637960936dba18da; passport_csrf_token_default=b9130cb9bce642cd637960936dba18da; multi_sids=6625030902617604098%3A0bacae4d9a1eca97e24c545d0e62a680; cmpl_token=AgQQAPOFF-RO0ovOOCbAsNk7_Zaci23Lf5YOYN3u0w; sid_guard=0bacae4d9a1eca97e24c545d0e62a680%7C1755558235%7C15552000%7CSat%2C+14-Feb-2026+23%3A03%3A55+GMT; uid_tt=70a0f71ec40f646e90a8afd0abfd7a0a89e3505c21d2cbf9b8eb8ec98c0b377a; uid_tt_ss=70a0f71ec40f646e90a8afd0abfd7a0a89e3505c21d2cbf9b8eb8ec98c0b377a; sid_tt=0bacae4d9a1eca97e24c545d0e62a680; sessionid=0bacae4d9a1eca97e24c545d0e62a680; sessionid_ss=0bacae4d9a1eca97e24c545d0e62a680; sid_ucp_v1=1.0.0-KGIxNjIxYjBmYmZjYTZkODI4YTgzNjllMDcyMWVkZTQyZTJmM2NlN2IKGgiCgIjElNC1-FsQ2-KOxQYYsws4B0D0B0gEEAMaBm1hbGl2YSIgMGJhY2FlNGQ5YTFlY2E5N2UyNGM1NDVkMGU2MmE2ODA; ssid_ucp_v1=1.0.0-KGIxNjIxYjBmYmZjYTZkODI4YTgzNjllMDcyMWVkZTQyZTJmM2NlN2IKGgiCgIjElNC1-FsQ2-KOxQYYsws4B0D0B0gEEAMaBm1hbGl2YSIgMGJhY2FlNGQ5YTFlY2E5N2UyNGM1NDVkMGU2MmE2ODA; store-idc=alisg; tt-target-idc-sign=sxj4yyNrlC8EN7d6eRT7sKdH9dJbpyb1gjpyusCh2Q4G2qUbhcYGwssWX5Cp6098HlobOHOuUfdqNykrMH1SkV2PlXHgeb_JcuQTiGBxeERbSflQKSbVES6csbJ7BzqaO6TF4Bs2FNy50WB8-S_uNQXK2oPvxDjiSStr7B9KEC1l_qxQzFoAGMrkc1g6t5fH3wVUz5uDQiqxn9nDJ0LvD0WuGZau1zbm2uzACamyaAIZZ9JbYSncEGYTf4p3TUWJn4IhgJLgY4KMP-xOUsG9tmABtTpJWmw05Jr6EZk4GYYYAQNrrxv0VhMbjhGK5xAC_3VbhZ0hRCvYs_BQ5us3Eel5kU1jfre6WkfPh7-XIYU2xNKcPJrHo6g7VftUPJOJM_gRVnXfd3Os7_cri9tlNOo3n-BL50qWOMXfrJ9HDnW-c4ZzIkCQbJzSEGE--7EEYN1VggRvlFdFTGiXXy6ArTRBUBjLy3iJ0pUFBOycZFJ0btw6vrjtAcgYv_Wg15mA; tiktok_webapp_theme_source=system; perf_feed_cache={%22expireTimestamp%22:1756868400000%2C%22itemIds%22:[%227539124343570255134%22%2C%227521337459209260296%22%2C%227520199205688937730%22]}; store-country-sign=MEIEDHEsj0zfqHrLKyfW4AQgwBcNxKFgMPcDgU1U-stSKkqPTVI_itDftPi8J042yogEEKKa2fRXe4Zt-ugl6oUWWcg; odin_tt=329395853882a2ed8dfd51345071dc68c36eb8b6eabd4270b07d4b74615f1f0b1cf5e3e05fe949dca8cd67cec6d05b5e66dd77760fa46ca6c68895e53cc686d3; msToken=cT2-cwW2YPfS_J6XIu0UZ75H8HiHFe5K9vSSV4n8iAEgJhFyi_9JBld2EQ-vcTXvTftwnDz-veGNQ4uxNqyLVhLp58ZkuMZLnsph_lqekCHYs2KyiskK-16nkEN1TCO4Zm7UjKuhbBMNf1Q9kd5Mt1-D; ttwid=1%7CKZnaIsRKXB01eDqrvBoT5-uSOcDVaLCCuvRQ93m64yU%7C1755598230%7C8cb0a70e410e85128d83d30e8c4d12d7d9b34a850dd133059ea56726467d2e6a; msToken=6ZIcmnnmWSi0HgrJBvASTpH8VCu8QqhU8QV1RYRNpVah-klfGI7xgn7RXp7OHjbUdD3k28OKDl_qxH_35_OWfpvYkiY10iSmGp5suB49ltnR3N0SZr0N4LvaGytmicc6AWGiBXUtljgX4pbp3gpS0XDq",
    # "cookie": "sessionid=3a2c6d98592cffb57cd792e3cc016323"
    "cookie": "sessionid=dd4576ffa2fff7a4992db9082558c8b7",
}
body = urlencode({})

headers = Sign(params=params_string, headers=baseheader)


# with open("submodule/x-gorogn-khronos-argus-ladon/example/headers_follow_user.json", "w", encoding="utf-8") as f:
#     json.dump(headers, f, ensure_ascii=False, indent=4)


response = requests.post(
    f"https://api22-normal-c-alisg.tiktokv.com/aweme/v1/commit/follow/user/?{params_string}",
    headers=headers,
    # proxies={'http': 'http://' + select_proxy, 'https': 'http://' + select_proxy}
)
print(response.text)
