# custom_getattr_class.py

class Graceful:
    def __getattr__(self, name):
        print(f"[CustomObject] '{name}' not found, returning fallback")
        return "default"

def main():
    obj = Graceful()
    print(obj.some_missing_attr)

if __name__ == "__main__":
    main()
