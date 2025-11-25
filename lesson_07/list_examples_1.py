def dot_product(vector_1, vector_2):
    """
    Return dot product of 2 vectors of the same size if any and True.
    Return False otherwise
    """
    if len(vector_1) != len(vector_2):
        return False, -1
    else:
        total = 0
        for i in range(len(vector_1)):
            total = total + (vector_1[i] * vector_2[i])

        return True, total


def main():
    vec_1 = [0.3, 0.0, 0.4, 0.5]
    vec_2 = [0.2, 0.5, 0.6, 0.9]
    has_result, result = dot_product(vec_1, vec_2)
    if has_result:
        print(f"Value of dot product = {result}")
    else:
        print("Vectors are not of the same size!")
main()
