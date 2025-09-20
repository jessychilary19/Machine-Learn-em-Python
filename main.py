from flask import Flask, make_response, request
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Carrega o JSON
with open("produtos.json", encoding="utf-8") as f:
    produtos = json.load(f)


@app.route("/produtos", methods=["GET"])
def get_produtos():
    response = make_response(
        json.dumps(produtos, indent=4, ensure_ascii=False),
        200
    )
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.route("/produtos", methods=["POST"])
def create_produtos():
    produto = request.json
    produtos.append(produto)

    with open("produtos.json", "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

    response = make_response(
        json.dumps(produto, indent=4, ensure_ascii=False),
        201
    )
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


if __name__ == "__main__":
    app.run(debug=True)
