import os
import shutil
import tempfile

paths = [
    r"C:\Windows\Temp",
    tempfile.gettempdir()
]

for path in paths:
    print(f"\nCleaning: {path}")

    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)

                print(f"Deleted: {item}")

            except Exception as e:
                print(f"Skipped {item}: {e}")

print("\nCleanup completed.")