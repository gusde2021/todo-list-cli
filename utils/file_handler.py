```python
import json

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump(tasks, file, indent=4)
```
