class Checker:
    # "We use the information of this path and its two end nodes as inputs for the Checker function"

    # 
    def __init__(self, list_of_inspectors):
        self.the_inspectors = list_of_inspectors

    def evaluate(self, node, path, n):
        return all(
            [
                self.the_inspectors(
                    node, path, n
                )
            ]
        )
