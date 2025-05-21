def interactive_echo():
    msg = yield "Ready to receive"
    while True:
        msg = yield f"Received: {msg}"

def use_send_with_generator():
    gen = interactive_echo()
    print(next(gen))              # Prime generator
    print(gen.send("Hello!"))     # Send message
    print(gen.send("How are you?"))

if __name__ == "__main__":
    use_send_with_generator()
