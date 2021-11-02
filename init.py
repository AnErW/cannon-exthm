def main():
    return [
        (
            "container", {
                "image": "ubuntu:latest",
                "cpu": 8,
                "memory":"16G"
                }
            ),
        ("task","script")
            ]
