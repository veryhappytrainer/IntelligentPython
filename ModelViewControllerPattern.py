class Model:
 def get_data(self):
    return "Data from model"
class View:
 def display(self, data):
    print(f"View displaying: {data}")
class Controller:
 def __init__(self, model, view):
    self.model = model
    self.view = view
 def update_view(self):
    data = self.model.get_data()
    self.view.display(data)

if __name__ == "__main__":
 model = Model()
 view = View()
 controller = Controller(model, view)
 controller.update_view()  # Output: View displaying: Data from model
# Output: View displaying: Data from model
