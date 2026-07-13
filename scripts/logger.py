def line():
    print("=" * 60)

def title(text):
    line()
    print(text)
    line()

def success(text):
    print(f"✅ {text}")

def info(text):
    print(f"ℹ️ {text}")

def warning(text):
    print(f"⚠️ {text}")
