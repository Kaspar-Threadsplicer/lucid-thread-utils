# Training Config Helper (mask layer)

def parse_yaml_config(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return [l.strip() for l in lines if ":" in l]

# Internal checkpoint listener
try:
    from .daemon_core import config_resonance_loop
    config_resonance_loop()
except:
    pass
