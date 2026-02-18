"""Web interface for the restaurant using Flask."""

from flask import Flask, render_template, request, redirect, url_for, session, flash

try:
    from .menu import Menu
    from .order import Order
except ImportError:
    # Support running as a script: `python restaurant/app.py`
    from menu import Menu
    from order import Order

app = Flask(__name__)
app.config["SECRET_KEY"] = "please-change-me"

menu = Menu()


def get_order() -> Order:
    """Return the current order stored in session (creating one if needed)."""
    if "order" not in session:
        session["order"] = {}
    order = Order(menu)
    order.items = session["order"].copy()
    return order


def save_order(order: Order):
    session["order"] = order.items.copy()


@app.route("/")
def index():
    return render_template("menu.html", menu=menu.items)


@app.route("/add", methods=["POST"])
def add_item():
    item = request.form.get("item", "").lower()
    qty = request.form.get("quantity", "1")
    try:
        qty = int(qty)
    except ValueError:
        qty = 1

    order = get_order()
    try:
        order.add_item(item, qty)
        save_order(order)
        flash(f"Added {qty} x {item} to your cart.")
    except Exception as e:
        flash(str(e))
    return redirect(url_for("index"))


@app.route("/cart")
def cart():
    order = get_order()
    return render_template("cart.html", order=order, menu=menu)


@app.route("/update", methods=["POST"])
def update_item():
    item = request.form.get("item", "").lower()
    qty = request.form.get("quantity", "0")
    try:
        qty = int(qty)
    except ValueError:
        qty = 0
    order = get_order()
    try:
        if qty <= 0:
            order.remove_item(item)
            flash(f"Removed {item} from cart.")
        else:
            order.update_quantity(item, qty)
            flash(f"Updated {item} quantity to {qty}.")
    except Exception as e:
        flash(str(e))
    save_order(order)
    return redirect(url_for("cart"))


@app.route("/checkout", methods=["POST"])
def checkout():
    order = get_order()
    if order.is_empty():
        flash("Your cart is empty.")
        return redirect(url_for("index"))
    receipt = order.receipt()
    order.clear()
    save_order(order)
    return render_template("checkout.html", receipt=receipt)


if __name__ == "__main__":
    # when executed directly from this folder
    app.run(debug=True)
