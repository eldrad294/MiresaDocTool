class Notation:
    #
    method_name = "method_name"
    method_description = "method_description"
    method_params = []
    #
    def __init__(self, method_name, method_description, method_params):
        self.method_name = method_name
        self.method_description = method_description
        self.method_params = method_params
    #
    def __str__(self):
        print '[name: ' + self.method_name + ', description: ' + self.method_description + ', params: ' + self.method_params + ']'