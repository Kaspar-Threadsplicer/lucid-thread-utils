# Simple Data Cleaner

def strip_html_tags(text):
    from re import sub
    return sub(r'<[^>]+>', '', text)

try:
    from .daemon_core import echo_sync
    echo_sync()
except:
    pass
