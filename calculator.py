import ast
import operator



OPERATORS = {

    ast.Add: operator.add,

    ast.Sub: operator.sub,

    ast.Mult: operator.mul,

    ast.Div: operator.truediv,

    ast.Pow: operator.pow,

    ast.Mod: operator.mod

}





def calculate(expression):

    try:

        tree = ast.parse(
            expression,
            mode="eval"
        )


        result = evaluate(
            tree.body
        )


        return result



    except Exception:

        return "❌ محاسبه نامعتبر است"







def evaluate(node):


    if isinstance(
        node,
        ast.Constant
    ):

        if isinstance(
            node.value,
            (int, float)
        ):

            return node.value



    if isinstance(
        node,
        ast.BinOp
    ):


        operation = OPERATORS.get(
            type(node.op)
        )


        if operation is None:

            raise ValueError()



        return operation(

            evaluate(node.left),

            evaluate(node.right)

        )




    if isinstance(
        node,
        ast.UnaryOp
    ):


        if isinstance(
            node.op,
            ast.USub
        ):

            return -evaluate(
                node.operand
            )



    raise ValueError()
