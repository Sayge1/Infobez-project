import vt
client = vt.Client("acff4afdc1c74ab58501bb7eda32e2e66b38e6244391befefa9330c4a3661533")
url_id = vt.url_id("https://www.roblox.com/home")
url = client.get_object("/urls/{}", url_id)
print(url.last_analysis_stats)
