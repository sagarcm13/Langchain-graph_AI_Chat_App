from app.graph import build_graph

def main():
    graph = build_graph()

    print("🤖 Gemini AI Agent (type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        result = graph.invoke({
            "user_input": user_input
        })

        print("AI:", result["response"])

if __name__ == "__main__":
    main()
