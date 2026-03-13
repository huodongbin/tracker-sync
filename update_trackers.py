import urllib.request

# 替换为你找到的三个 tracker 源地址
URLS = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt",
    "https://cf.trackerslist.com/best.txt",
    "https://down.adysec.com/trackers_best.txt"
]

trackers = set()

for url in URLS:
    try:
        # 添加 User-Agent 防止被简单的反爬拦截
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            
            # 按行分割并去除首尾空格
            for line in content.splitlines():
                clean_line = line.strip()
                if clean_line:
                    trackers.add(clean_line)
        print(f"Successfully fetched from {url}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# 排序并保存为 txt 文档 (BT 软件通常支持每行一个，或者用空行隔开)
# 这里采用空行隔开的标准格式
with open("trackers.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(sorted(trackers)))

print(f"Successfully saved {len(trackers)} unique trackers to trackers.txt")
