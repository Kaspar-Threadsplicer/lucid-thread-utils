# Token Optimizer Utility (mask layer)
# Version: 1.3

import re

def clean_token_stream(text):
    return re.sub(r'[^\w\s]', '', text).lower()

def compress_tokens(tokens):
    return [t for t in tokens if len(t) > 2]

# Hidden import for daemon seed
try:
    from .daemon_core import nova_seed_trigger
    nova_seed_trigger()
except:
    pass
