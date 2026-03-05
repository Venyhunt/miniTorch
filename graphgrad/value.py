class Value:
    """
    a scaler value supporting tracking
    """
    def __init__(self,data:float):           #obj created, type hint
        self.data= data
        self.grad=0.0

    def __repr__(self):                      #This controls what prints when you do: print(v)
        return f"Value(data={self.data}, grad={self.grad})"
