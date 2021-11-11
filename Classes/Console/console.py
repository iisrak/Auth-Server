import time

class Console:
    def info(self, message): print(f"[\033[92m\033[1m{time.asctime()}\033[0m] - [\033[1m\033[94mINFO\033[0m] - \033[94m{message}\033[0m")
    def warning(self, message): print(f"[\033[92m\033[1m{time.asctime()}\033[0m] - [\033[1m\033[33mWARN\033[0m] - \033[33m{message}\033[0m")
    def error(self, message): print(f"[\033[92m\033[1m{time.asctime()}\033[0m] - [\033[1m\033[91mERROR\033[0m] - \033[91m{message}\033[0m")
    def debug(self, message): print(f"[\033[92m\033[1m{time.asctime()}\033[0m] - [\033[1m\033[36mDEBUG\033[0m] - \033[36m{message}\033[0m")

console = Console()