import requests

def latest(repo):
    url=f"https://api.github.com/repos/{repo}/releases/latest"
    r=requests.get(url).json()
    return r["tag_name"],r["assets"]

cm_ver,cm_assets=latest("MetaCubeX/ClashMetaForAndroid")
fl_ver,fl_assets=latest("chen08209/FlClash")
cv_ver,cv_assets=latest("clash-verge-rev/clash-verge-rev")
cp_ver,cp_assets=latest("mihomo-party-org/clash-party")

def find(assets,key):
    for a in assets:
        if key in a["name"]:
            return a["browser_download_url"]
    return ""

android=f"""
## 📱 Android
- ClashMeta {cm_ver}
  👉 ARMv8|点此下载 ({find(cm_assets,'arm64')})
  👉 ARMv7|点此下载 ({find(cm_assets,'armeabi')})

- FlClash {fl_ver}
  👉 ARMv8|点此下载 ({find(fl_assets,'arm64')})
  👉 ARMv7|点此下载 ({find(fl_assets,'armeabi')})
"""

windows=f"""
## 💻 Windows
- Clash Verge {cv_ver}
  👉 点此下载 ({find(cv_assets,'setup.exe')})

- FlClash {fl_ver}
  👉 点此下载 ({find(fl_assets,'windows')})

- Clash Party {cp_ver}
  👉 点此下载 ({find(cp_assets,'windows')})
"""

mac=f"""
## 🍎 MacOS
- Clash Verge {cv_ver}
  👉 Apple M芯片|点此下载 ({find(cv_assets,'aarch64')})
  👉 Intel芯片|点此下载 ({find(cv_assets,'x64.dmg')})

- FlClash {fl_ver}
  👉 Apple M芯片|点此下载 ({find(fl_assets,'macos-arm')})
  👉 Intel芯片|点此下载 ({find(fl_assets,'macos-amd')})
"""

content=f"# 客户端下载\n{android}\n---\n{windows}\n---\n{mac}"

open("README.md","w",encoding="utf8").write(content)
